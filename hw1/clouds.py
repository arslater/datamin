import numpy as np
np.set_printoptions(threshold=np.nan)

def center(matrix):
    centeredMatrix = []
    i=0
    j=0
    row=[]
    rows=matrix.shape[0]
    cols=matrix.shape[1]
    mean=matrix.mean()

    print(matrix.shape)
    while i < rows:
        while j < cols:
            row.append(matrix[i][j]-mean)
            j+=1
        j=0
        i+=1
        centeredMatrix.append(row)
        row=[]

    return np.matrix(centeredMatrix)

def covar(matrix):
    matrix -= matrix.mean(axis=0)
    n=matrix.shape[1]

    fract= float(n-1)
    return(np.dot(matrix,matrix.T.conj())/fract)

def eign(matrix):
    evals,evects=np.linalg.eigh(np.resize(matrix,[10,10]))
    return(evals,evects)

data = np.loadtxt("cloud.data")
#print(center(data))
#eign(center(data))
#print(covar(center(data)))
