-- ALTER table user_profiles
-- ADD CONSTRAINT fk_account_profile
--  Foreign Key (account_id)REFERENCES user_accounts(id);


-- INSERT INTO user_accounts (username, "password")
-- VALUES (
--     'person1','qwerkjl345'),
--     (
--     'person2','qwer2jl345'),
--     (
--     'person3','qwerkj3345');

UPDATE user_profiles
SET account_id = NULL;


INSERT INTO user_profiles (account_id, personal_quote)
VALUES
(2, 'World, Hello'),
(5, 'Hello World');




