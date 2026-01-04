-- List the number of records for each score in second_table
-- Display the score and the count labeled as 'number'
-- Sort the results by the count descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
