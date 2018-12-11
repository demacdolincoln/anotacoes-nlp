import numpy as np
from scipy.spatial.distance import euclidean, cosine

def norm(x):
    return x/np.sqrt(np.sum(np.square(x)))

def knn(matrix, n=5, func="cos", **kw):
    data_norm, coord_norm = None, None
    
    if "coord" in kw.keys():
        data = np.concatenate((matrix, np.array([kw["coord"]])))
        ata_norm = norm(matrix)
        coord_norm = data_norm[-1, :]
    else:
        data_norm = norm(matrix)
        coord_norm = data_norm[kw["pos"]]
    
    res = []
    for i in data_norm:
        if func=="cos":
            res.append(cosine(coord_norm, i))
        else:
            res.append(euclidean(coord_norm, i))
    
    if func=="cos":
        return np.array(res).argsort()[1:n+1], sorted(res)[1:n+1]
    else:
        return np.array(res).argsort()[1:n+1], sorted(res)[1:n+1]