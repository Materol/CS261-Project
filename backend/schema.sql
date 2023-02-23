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
*/

/*
    as a user, consider what is needed fro the database to understand what is going on
    Look at the UI diagram to get any ideas of this and maybe any of the other diagrams
*/

-- Every project is unique 
CREATE TABLE project (
    id SERIAL PRIMARY KEY,
    createdOn TIMESTAMP NOT NULL,
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
