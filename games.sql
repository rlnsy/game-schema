-- Session-static --
--------------------

CREATE TABLE Game (
    id char(50) PRIMARY KEY
);

CREATE TABLE Agent(
    id char(50) PRIMARY KEY,
);

CREATE TABLE Player (
    agent_id char(50) PRIMARY KEY,
    display_name char(50) NOT NULL,
    token char(50) NOT NULL,
    FOREIGN KEY agent_id REFERENCES Agent(id) ON DELETE CASCADE
);

CREATE TABLE GameRole (
    -- Synonymous with the 'role' prefix in GDL
    id char(50) PRIMARY KEY,
    -- readable ids are more trackable and usable in logic
    game_id char(50),
    FOREIGN KEY (game_id) REFERENCES Game (id) ON DELETE CASCADE
);

CREATE TABLE GameAction (
    --
    -- Represents a generic action superclass
    --
    -- suptype_id refers in a soft sense to a subclass table
    -- created by a specific game module. Since that module creates it's action
    -- tables, it also has the reponsibility to set and manage subtype ids in
    -- module logic.
    --
    id int PRIMARY KEY,
    game_id char(50),
    subtype_id char(100) NOT NULL,
    FOREIGN KEY (game_id) REFERENCES Game (id) ON DELETE CASCADE
);

-- Session-dynamic --
---------------------

CREATE TABLE GameSession (
    id int PRIMARY KEY,
    game_id char(50),
    FOREIGN KEY (game_id) REFERENCES Game (id) ON DELETE CASCADE
);

CREATE TABLE HasRole (
    game_session_id int,
    agent_id char(50),
    game_role_id char(50),
    is_active boolean,
    PRIMARY KEY (game_session_id, player_name, game_id),
    FOREIGN KEY (game_session_id) REFERENCES GameSession (id) ON DELETE CASCADE,
    FOREIGN KEY (agent_id) REFERENCES Agent (id) ON DELETE CASCADE,
    FOREIGN KEY (game_role_id) REFERENCES GameRole (id) ON DELETE CASCADE,
);

CREATE TABLE SessionGameState (
    --
    -- Provides a unique point of reference for a specific
    -- game state, in a specific session.
    -- idx is a state index and is should be initialized
    -- at 0 and incrimented by one each time state is updated.
    -- additional tuples describing state refer to the
    -- entire primary key.
    --
    -- Deletion of the linked game session will cause
    -- this state record to be deleted.
    --
    idx int,
    game_session_id int,
    PRIMARY KEY (idx, game_session_id),
    FOREIGN KEY (game_session_id) REFERENCES GameSession (id) ON DELETE CASCADE
);

CREATE TABLE Terminal (
    --
    -- Synonymous with the 'terminal' prefix in GDL
    -- terminal(T) means that the state is terminal
    -- meaning the session state cannot progress
    -- further, this typically means a win or tie has
    -- been reached.
    --
    -- Deletion of the linked state will cause
    -- this terminal record to be deleted.
    --
    state_idx int,
    state_game_session_id int,
    PRIMARY KEY (num, game_session_id),
    FOREIGN KEY (state_idx) REFERENCES SessionGameState (idx) ON DELETE CASCADE,
    FOREIGN KEY (state_game_session_id) REFERENCES SessionGameState (game_session_id) ON DELETE CASCADE
);

CREATE TABLE DoesAction (
    state_idx int,
    game_session_id int,
    agent_id char(50),
    game_role_id char(50),
    FOREIGN KEY (state_idx) REFERENCES SessionGameState (idx) ON DELETE CASCADE,
    FOREIGN KEY (game_session_id) REFERENCES SessionGameState (game_session_id) ON DELETE CASCADE,
    FOREIGN KEY (agent_id) REFERENCES Agent (id),
    FOREIGN KEY (game_role_id) REFERENCES GameRole (id),
);
