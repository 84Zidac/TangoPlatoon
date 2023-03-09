-- https://app.quickdatabasediagrams.com/#/d/afUTNz

-- CREATE TABLE students(
--     id serial PRIMARY KEY,
--     first_name varchar(255),
--     last_name varchar(255),
--     address_id integer REFERENCES addresses(id)
--     UNIQUE (first_name,last_name)
-- )

-- CREATE TABLE addresses(
--     id serial PRIMARY KEY,
--     address_line varchar(255)
-- )



CREATE TABLE user_accounts(
    id SERIAL PRIMARY KEY,
    username varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    last_login_date timestamp

);

CREATE TABLE user_profiles(
    id SERIAL PRIMARY KEY,
    account_id int REFERENCES user_accounts(id),
    profile_pic_url varchar(255),
    personal_quote varchar(255)

);

CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    content TEXT,
    date_posted timestamp,
    profile_id int REFERENCES user_profiles(id)
);

CREATE TABLE reaction_types (
    id serial PRIMARY KEY,
    reaction varchar(255)

);

CREATE TABLE post_reactions(
    id  serial PRIMARY KEY,
    post_id int REFERENCES posts(id),
    reaction_id int REFERENCES reaction_types,
    prifile_id int REFERENCES user_profiles
);






