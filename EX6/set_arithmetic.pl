% Arithmetic operations
add(X,Y,Z):- Z is X+Y.
sub(X,Y,Z):- Z is X-Y.
mul(X,Y,Z):- Z is X*Y.
div(X,Y,Z):- Z is X/Y.

% Membership
member(X,[X|_]).
member(X,[_|T]):- member(X,T).

% Union
union([],L,L).
union([H|T],L,R):- member(H,L), union(T,L,R).
union([H|T],L,[H|R]):- \+ member(H,L), union(T,L,R).

% Intersection
intersection([],_,[]).
intersection([H|T],L,[H|R]):- member(H,L), intersection(T,L,R).
intersection([H|T],L,R):- \+ member(H,L), intersection(T,L,R).

% Difference
difference([],_,[]).
difference([H|T],L,R):- member(H,L), difference(T,L,R).
difference([H|T],L,[H|R]):- \+ member(H,L), difference(T,L,R).