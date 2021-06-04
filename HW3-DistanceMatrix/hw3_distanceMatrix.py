# Vincent Purcell
# Data Mining 1 - Summer21 - HW3

import numpy as np
from numpy.ma import zeros
from math import sqrt
import matrixData

# Print Stat
def printMatrix(mat):
    print_mat = np.vstack((matrixData.names,np.around(mat,decimals=2)))
    print_mat = np.hstack((matrixData.row_names,print_mat))
    print(print_mat)

def genSimMatrix(mat, algo):
    _, col = mat.shape
    sim_mat = zeros((len(mat), len(mat)))
    for feature in range(col):
        for x in range(len(sim_mat)):
            for y in range(len(sim_mat)):
                if algo == 'matching':
                    if mat[x][feature] == mat[y][feature]:
                        sim_mat[x][y] = sim_mat[x][y] + 1
                if algo == 'euclidean':
                    dist = 1 - sqrt((mat[x][feature]-mat[y][feature])**2)
                    sim_mat[x][y] = sim_mat[x][y] + dist
                if algo == 'jaccard':
                    if x==y:
                            sim_mat[x][y] = 1
                    else:
                        a,b,c = zeros(3)
                        for i in range(0,col):
                            if mat[x][i] == 1 and mat[y][i] == 1:
                                a = a + 1
                        if a != 0:
                            for i in range(0,col):
                                if mat[x][i] == 0 and mat[y][i] == 1:
                                    b = b + 1
                            for i in range(0,col):
                                if mat[x][i] == 1 and mat[y][i] == 0:
                                    c = c + 1
                            sim_mat[x][y] = a/(a+b+c)
                        else:
                            sim_mat[x][y] = 0
    if algo == 'jaccard':
        return sim_mat
    else:
        return sim_mat / col


gender_sim = genSimMatrix(matrixData.gender_data, 'matching')
print("Binary Gender Data Similarity Matrix")
printMatrix(gender_sim)

nominal_sim = genSimMatrix(matrixData.nomimal_data, 'matching')
print("Nominal Data (Color/Blood Type) Similarity Matrix")
printMatrix(nominal_sim)

general_health_sim = genSimMatrix(matrixData.general_health_data, 'euclidean')
print("General Health Data (Ordinal) Similarity Matrix")
printMatrix(general_health_sim)

test1_sim = genSimMatrix(matrixData.test1_data, 'euclidean')
print("Test1 Data (Numerical) Similarity Matrix")
printMatrix(test1_sim)

asym_sim = genSimMatrix(matrixData.asym_data, 'jaccard')
print("Asymmetrical Data (Cough/H. Blood Pressure) Similarity Matrix")
printMatrix(asym_sim)

total_sim_matrix = (gender_sim + (2*nominal_sim) + general_health_sim + test1_sim + (2*asym_sim))/7
print("Total Similarity Matrix (All Data)")
printMatrix(total_sim_matrix)

