
from numpy import *
from numpy.linalg import solve


def poissonSolve(nCut):
    n = 2*nCut + 1; m = n*n; h = 2/(n-1) 
    A = eye(m); B = zeros(m)
    for i in range(1,n-1): #balaye de gauche à droite
        for j in range(1,n-1): #Balaye de haut en bas
            if i > nCut or j < nCut: #Comme on balye de gauche à droite et de haut en bas. Il faut remplit la matrice lorsque qu'on est en bas à gauche (j > nCut), en bas à droite (i> nCut et j>nCut), en haut à droitre (i>nCut)
                index = i + j*n #Indexification du tableau
                A[index,index] = 4.0
                A[index,index-1] = -1.0
                A[index,index+1] = -1.0
                A[index,index-n] = -1.0
                A[index,index+n] = -1.0
                B[index] = 1
    return solve(A,B).reshape(n,n) #Le solve(A,B) retourne un vecteur, la méthode reshape permet de reconstruire la matrice de noeud nx*ny

