% --------------- %
% Game Primitives %
% --------------- %

resource('Brick').
resource('Lumber').
resource('Ore').
resource('Grain').
resource('Wool').

terrain('Hills').
terrain('Forest').
terrain('Mountains').
terrain('Fields').
terrain('Pasture').
terrain('Desert').

% integ_verify_terrain(T) :- terrain(T).

produce('Hills',        'Brick').
produce('Forest',       'Wood').
produce('Mountains',    'Ore').
produce('Fields',       'Grain').
produce('Pasture',      'Wool').

% --------------- %
%   Game pieces   %
% --------------- %
% - Per the standard version of the game
% - Assigned numbers are arbitrary and have no basis in 
%   the official rulebook

tile(1,     'Hills').
tile(2,     'Hills').
tile(3,     'Hills').
tile(4,     'Forest').
tile(5,     'Forest').
tile(6,     'Forest').
tile(7,     'Forest').
tile(8,     'Mountains').
tile(9,     'Mountains').
tile(10,    'Mountains').
tile(11,    'Fields').
tile(12,    'Fields').
tile(13,    'Fields').
tile(14,    'Fields').
tile(15,    'Pasture').
tile(16,    'Pasture').
tile(17,    'Pasture').
tile(18,    'Pasture').
tile(19,    'Desert').
tile(19,    'Deserts').

% tile_produce(H,R) :- tile(H, T), produce(T, R).

% integ_tile_non_unique(H) :- tile(H, T1), tile(H, T2), T1 \= T2.
% integ_tile_unique(H) :- not(integ_tile_non_unique(H)).

% integ_verify_tile(H) :- tile(H, T), integ_verify_terrain(T).

% There are 6 sea frames, numbered 1 to 6.

sea_frame(1).
sea_frame(2).
sea_frame(3).
sea_frame(4).
sea_frame(5).
sea_frame(6).


% Sea frames have etched-in harbors described here.
% Encodes the piece, trade ratio, resource, and vertex on the piece.
% Sea frame pieces each have 6 vertices, numbered 1 to 6,
% left to right looking from the flat edge.

sea_frame_harbor(1, 3, 1, '?', 3).
sea_frame_harbor(1, 3, 1, '?', 4).

sea_frame_harbor(2, 2, 1, 'Wool', 2).
sea_frame_harbor(2, 2, 1, 'Wool', 3).
sea_frame_harbor(2, 3, 1, '?', 5).
sea_frame_harbor(2, 3, 1, '?', 6).

sea_frame_harbor(3, 2, 1, 'Ore', 3).
sea_frame_harbor(3, 2, 1, 'Ore', 4).

sea_frame_harbor(4, 2, 1, 'Grain', 2).
sea_frame_harbor(4, 2, 1, 'Grain', 3).
sea_frame_harbor(4, 3, 1, '?', 5).
sea_frame_harbor(4, 3, 1, '?', 6).

sea_frame_harbor(5, 2, 1, 'Lumber', 3).
sea_frame_harbor(5, 2, 1, 'Lumber', 4).

sea_frame_harbor(6, 2, 1, 'Brick', 2).
sea_frame_harbor(6, 2, 1, 'Brick', 3).
sea_frame_harbor(6, 3, 1, '?', 5).
sea_frame_harbor(6, 3, 1, '?', 6).
