-- List all records from second_table with score >= 10
-- Show score first, then name
-- Order results by score in descending order (highest first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
