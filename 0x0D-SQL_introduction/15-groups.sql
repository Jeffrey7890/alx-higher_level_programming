-- lists number of recoreds with the same score
SELECT score, COUNT(score) number FROM second_table GROUP BY score HAVING COUNT(score) > 0 ORDER BY number DESC;
