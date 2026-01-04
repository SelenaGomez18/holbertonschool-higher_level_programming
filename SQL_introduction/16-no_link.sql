-- List all records from second_table where name is not empty or NULL
-- Show score first, then name
-- Order the results by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
