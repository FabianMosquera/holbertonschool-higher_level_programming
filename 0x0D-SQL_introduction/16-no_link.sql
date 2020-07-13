-- Script that lists all records of the table
-- Don’t list rows without a name value
-- display the score and the name
-- listed by descending score
SELECT score , name 
FROM second_table WHERE name
IS NOT NULL ORDER BY score DESC;