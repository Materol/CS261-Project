DROP TABLE IF EXISTS project CASCADE;
DROP TABLE IF EXISTS member_role_history CASCADE;
DROP TABLE IF EXISTS project_role CASCADE;
DROP TABLE IF EXISTS job_title CASCADE;
DROP TABLE IF EXISTS people CASCADE;
DROP TABLE IF EXISTS reports_to CASCADE;
DROP TABLE IF EXISTS project_history CASCADE;

/*
    Table design based on Entity Relationship Diagram provided in the Design Document

    CONSTRAINTS:
    - createdOn cannot be later than current date
    - editedOn cannot be earlier than createdOn date
    - editedOn cannot be later than current date
    - completed boolean cariable NOT NULL???
    - all project history must be after the start date
    - don't have a reportee reporting to manager while the manager reports to the reportee
    -- a reportee can also not manage themselves???
*/

/*
    as a user, consider what is needed fro the database to understand what is going on
    Look at the UI diagram to get any ideas of this and maybe any of the other diagrams
*/


-- edited_on time cannot be earlier than created_on time
CREATE OR REPLACE FUNCTION check_edit_on() RETURNS trigger AS $$
DECLARE 
    projectid INTEGER;
BEGIN
    SELECT PH.id FROM project P INNER JOIN project_history PH ON P.id = PH.project_id INTO projectid WHERE NEW.edited_on < P.created_on;
    IF found THEN
        RETURN NULL;
    END IF;
    RETURN NEW;
END
$$ LANGUAGE plpgsql;

-- a reportee cannot report to a manager of the manager reports to the reportee
-- a reportee can also no tmanage themselves
CREATE OR REPLACE FUNCTION valid_report_manage() RETURNS trigger AS $$
DECLARE
    reportee INTEGER;
    manager INTEGER;
BEGIN
    SELECT RT.reportee_id, RT.manager_id FROM reports_to RT INTO reportee, manager WHERE NEW.reportee_id = RT.manager_id AND NEW.manager_id = RT.reportee_id OR NEW.manager_id = NEW.reportee_id;
    IF found THEN
        RETURN NULL;
    END IF;
    RETURN NEW;
END 
$$ LANGUAGE plpgsql;


 
-- Every project is unique 
CREATE TABLE project (
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP NOT NULL,
    completed BOOLEAN NOT NULL
);

-- each item in ProjectHistory must refernece a project in Project table
CREATE TABLE project_history (
    id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES project(id),
    title VARCHAR(100) NOT NULL,
    project_description VARCHAR(800) NOT NULL,
    csf VARCHAR(100) NOT NULL,
    feedback VARCHAR(800) NOT NULL,
    edited_on TIMESTAMP NOT NULL
);

-- each defined project role in ProjectRole table is unique
CREATE TABLE project_role (
    id SERIAL PRIMARY KEY,
    role_title VARCHAR(100) NOT NULL
);

-- each defined job title in JobTitle table is unique
CREATE TABLE job_title (
    id SERIAL PRIMARY KEY,
    job_type VARCHAR(100) NOT NULL
);

-- each defined person is unique
CREATE TABLE people (
    id SERIAL PRIMARY KEY,
    job_title_id INTEGER REFERENCES job_title(id),
    email VARCHAR(100) NOT NULL,
    password_hash VARCHAR (100)
);

-- each person assigned to a project needs to be alloocated a role
CREATE TABLE member_role_history (
    -- projectID INTEGER REFERENCES Project(projectID),
    history_id INTEGER REFERENCES project_history(id),
    people_id INTEGER REFERENCES people(id),
    role_id INTEGER REFERENCES project_role(id)
);

-- every person may need to report to many people and they also may manage many people,
-- hence no primary key in this table. 
CREATE TABLE reports_to (
    reportee_id INTEGER REFERENCES people(id),
    manager_id INTEGER REFERENCES people(id)
);

------------------------------------------------------------------------------------------------
-- VIEWS
------------------------------------------------------------------------------------------------
-- get person passwords
CREATE OR REPLACE VIEW get_passwords AS
SELECT P.id, P.password_hash FROM people P; 

-- get icompleted projects
CREATE OR REPLACE VIEW uncomplete_project AS
SELECT P.id, P.created_on FROM project P WHERE completed = 'false';

-- get completed projects
CREATE OR REPLACE VIEW complete_project AS
SELECT P.id, P.created_on FROM project P WHERE completed = 'true';

-- get emails of people on a project name with the role of each person
CREATE OR REPLACE VIEW project_people AS
SELECT project_id, title, people_id, email, role_title FROM 
(SELECT project_id, title, members.people_id, role_title FROM
(SELECT PH.project_id, PH.title, MH.people_id, role_id FROM project_history PH INNER JOIN member_role_history MH ON PH.id = MH.history_id) as members
INNER JOIN 
(SELECT id, role_title FROM project_role) as PR
ON members.role_id = PR.id) AS table1
INNER JOIN
(SELECT id, email FROM people) AS table2
ON table1.people_id = table2.id; 

-----------------------------------------------------------------------------------------------------

-- trigger used to check that the edit_on date for a new project_history field is not before the project's created date
CREATE TRIGGER check_edit_date BEFORE INSERT OR UPDATE ON project_history
FOR EACH ROW
EXECUTE PROCEDURE check_edit_on();

-- trigger used to check that a manager doesn't manage a reportee while the reportee manages the manager at the same time
-- bug with first data entry failing to check (reportee_id == manager_id)???
CREATE TRIGGER check_manage_people BEFORE INSERT OR UPDATE ON reports_to
FOR EACH ROW
EXECUTE PROCEDURE valid_report_manage();
