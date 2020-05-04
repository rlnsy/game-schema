game(1, 'settlers').

game_name(N) :- game(_,N).
game_id(I) :- game(I,_).

