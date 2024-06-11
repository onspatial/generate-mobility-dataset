SELECT strftime('%m-%d', simulationTime, 'unixepoch') as date , COUNT(*) 
FROM 'table'
WHERE "foodNeed:status"='BecameFull'
GROUP BY strftime('%m-%d', simulationTime, 'unixepoch');

SELECT strftime('%m-%d', simulationTime, 'unixepoch') as date , COUNT(*) 
FROM 'table'
WHERE currentMode='AtRestaurant'
GROUP BY strftime('%m-%d', simulationTime, 'unixepoch');

SELECT *
FROM 'table'
WHERE agentId IN (1000,2000,3000,4000,5000,7055,459,4101,2419,5446,7269);

SELECT strftime('%m-%d', simulationTime, 'unixepoch') as date , COUNT(*) 
FROM 'table'
WHERE currentMode='AtHome' AND agentId IN (459)
GROUP BY strftime('%m-%d', simulationTime, 'unixepoch');

SELECT *
FROM 'table'
WHERE agentId IN (1000, 2000, 3000, 4000, 5000, 3484, 2781, 7055, 459, 3720, 2100, 4945, 5607, 4101, 2419, 3341, 6146, 4467, 338, 5446, 7269, 3816, 4610);

ALTER TABLE old_table_name
RENAME TO new_table_name;

SELECT agentId, date( simulationTime), COUNT(*)
from state
WHERE date( simulationTime) == '2019-07-4' AND currentMode == "AtWork"
GROUP BY agentId;

