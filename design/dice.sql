INSERT INTO Game
    VALUES ('Dice');

INSERT INTO GameRole
    VALUES ('Dice_roller',    'Dice');

INSERT INTO GameAction VALUES (1, 'Dice_RollAction');

CREATE TABLE Dice_RollAction(
    id int,
    die_1_value int,
    die_2_value int,
);
