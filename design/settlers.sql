INSERT INTO Game
    VALUES ('settlers');

INSERT INTO GameRole
    VALUES ('settlers_player-blue',    'settlers');

INSERT INTO GameRole
    VALUES ('settlers_player-orange',  'settlers');

INSERT INTO GameRole
    VALUES ('settlers_player-red',     'settlers');

INSERT INTO GameRole
    VALUES ('settlers_player-white',   'settlers');

INSERT INTO GameAction VALUES (1, 'settlers_RollAction');

CREATE TABLE settlers_RollAction(
    id int,
    die_1_value int,
    die_2_value int,
);
