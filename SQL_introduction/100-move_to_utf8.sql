-- Select the database to work on
USE hbtn_0c_0;

-- Convert the database hbtn_0c_0 to UTF8 (utf8mb4)
ALTER DATABASE hbtn_0c_0
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

-- Convert the table first_table to UTF8 (utf8mb4)
-- All columns will inherit the table charset, including 'name'
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
