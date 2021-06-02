padre(raul, ayrton).
padre(evaristo, raul).
padre(david, sandra).
madre(sandra, ayrton).
madre(rosario, raul).
madre(cristina, sandra).
abuelo(david, ayrton).
abuela(cristina, ayrton).
abuelo(evaristo, ayrton).
abuela(rosario, ayrton).
esposo(raul, sandra).

hijo(A, B):- padre(B,A).
hijo(A, B):- madre(B,A).
nieto(A, B):- abuelo(B, A).
nieto(A, B):- abuela(B, A).
suegra(A, C):- madre(A, B), esposo(B, C).
suegra(A, C):- madre(A, B), esposo(C, B).
