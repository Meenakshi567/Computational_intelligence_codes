% Gender

male(marthanda_varma).
male(rama_varma).
male(balarama_varma).
male(ravi_varma).

female(gowri_lakshmi_bayi).
female(gowri_parvathi_bayi).
female(sethu_lakshmi_bayi).
female(sethu_parvathi_bayi).

% Parent relationships

parent(marthanda_varma, gowri_lakshmi_bayi).
parent(marthanda_varma, gowri_parvathi_bayi).

parent(gowri_lakshmi_bayi, rama_varma).
parent(gowri_lakshmi_bayi, balarama_varma).

parent(gowri_parvathi_bayi, sethu_lakshmi_bayi).
parent(gowri_parvathi_bayi, sethu_parvathi_bayi).

parent(sethu_lakshmi_bayi, ravi_varma).

% Father rule

father(X,Y) :-
    male(X),
    parent(X,Y).

% Mother rule

mother(X,Y) :-
    female(X),
    parent(X,Y).

% Brother

brother(X,Y) :-
    male(X),
    parent(Z,X),
    parent(Z,Y),
    X \= Y.

% Sister

sister(X,Y) :-
    female(X),
    parent(Z,X),
    parent(Z,Y),
    X \= Y.

% Grandparent

grandparent(X,Y) :-
    parent(X,Z),
    parent(Z,Y).

% Grandfather

grandfather(X,Y) :-
    male(X),
    grandparent(X,Y).

% Grandmother

grandmother(X,Y) :-
    female(X),
    grandparent(X,Y).

% Uncle

uncle(X,Y) :-
    brother(X,Z),
    parent(Z,Y).

% Aunt

aunt(X,Y) :-
    sister(X,Z),
    parent(Z,Y).