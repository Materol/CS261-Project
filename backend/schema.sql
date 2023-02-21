DROP TABLE IF EXISTS Project CASCADE;
DROP TABLE IF EXISTS MemberRoleHistory CASCADE;
DROP TABLE IF EXISTS ProjectRole CASCADE;
DROP TABLE IF EXISTS JobTitle CASCADE;
DROP TABLE IF EXISTS Person CASCADE;
DROP TABLE IF EXISTS ReportsTo CASCADE;
DROP TABLE IF EXISTS ProjectHistory CASCADE;

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
CREATE TABLE Project (
    projectID SERIAL PRIMARY KEY,
    createdOn TIMESTAMP NOT NULL,
    completed BOOLEAN NOT NULL
);

-- each item in ProjectHistory must refernece a project in Project table
CREATE TABLE ProjectHistory (
    historyID SERIAL PRIMARY KEY,
    projectID INTEGER REFERENCES Project(projectID),
    title VARCHAR(100) NOT NULL,
    projectDescription VARCHAR(800) NOT NULL,
    CSFs VARCHAR(100) NOT NULL,
    feedback VARCHAR(800) NOT NULL,
    editedOn TIMESTAMP NOT NULL
);

-- each defined project role in ProjectRole table is unique
CREATE TABLE ProjectRole (
    roleID SERIAL PRIMARY KEY,
    roleTitle VARCHAR(100) NOT NULL
);

-- each defined job title in JobTitle table is unique
CREATE TABLE JobTitle (
    jobTitleID SERIAL PRIMARY KEY,
    jobType VARCHAR(100) NOT NULL
);

-- each defined person is unique
CREATE TABLE Person (
    personID SERIAL PRIMARY KEY,
    jobTitleID INTEGER REFERENCES JobTitle(jobTitleID),
    email VARCHAR(100) NOT NULL,
    passwordHash VARCHAR (100)
);

-- each person assigned to a project needs to be alloocated a role
CREATE TABLE MemberRoleHistory (
    -- projectID INTEGER REFERENCES Project(projectID),
    historyID INTEGER REFERENCES ProjectHistory(historyID),
    personID INTEGER REFERENCES Person(personID),
    roleID INTEGER REFERENCES ProjectRole(roleID)
);

-- every person may need to report to many people and they also may manage many people,
-- hence no primary key in this table. 
CREATE TABLE ReportsTo (
    reporteeID INTEGER REFERENCES Person(personID),
    managerID INTEGER REFERENCES Person(personID)
);
