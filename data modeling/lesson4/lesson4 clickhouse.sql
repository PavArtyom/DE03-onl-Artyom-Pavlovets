CREATE DATABASE IF NOT EXISTS players;
USE players;

CREATE TABLE players
(
    player_id UInt32,
    name String,
    age UInt8,
    nationality String,
    position String,
    club String,
    matches UInt16,
    goals UInt16,
    assists UInt16
)
ENGINE = MergeTree
ORDER BY player_id;


INSERT INTO players VALUES
(1, 'Lionel Messi', 38, 'Argentina', 'striker', 'inter miami', 25, 18, 12),
(2, 'Kilian Mbappe', 26, 'France', 'striker', 'real madrid', 30, 22, 8),
(3, 'Kevin de Breune', 34, 'Belgium', 'midfilder', 'manchester city', 28, 6, 15);

SELECT *
FROM players;

SELECT 
    name,
    goals,
    assists,
    matches,
    round(goals / matches, 2) AS goals_per_match
FROM players
ORDER BY goals DESC;