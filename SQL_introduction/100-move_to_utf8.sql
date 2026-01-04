-- Convert the database, table, and column to UTF8 (utf8mb4) with collation utf8mb4_unicode_ci

-- Select the database first
USE hbtn_0c_0;

-- Convert the database hbtn_0c_0
ALTER DATABASE hbtn_0c_0
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

-- Convert the table first_table
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert the column 'name' in first_table
ALTER TABLE first_table
MODIFY name VARCHAR(256) 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
