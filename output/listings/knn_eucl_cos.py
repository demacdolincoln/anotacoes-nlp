import numpy as np

def dist_eucl(a, b):
    return np.linalg.norm(a-b)

def cos_siml(a, b):
    return np.sum(np.dot(a, b))/ (np.sqrt(np.sum(np.dot(a, a))) * np.sqrt(np.sum(np.dot(b, b))))

def norm(x):
    return x/np.sqrt(np.sum(np.square(x)))

def knn(matrix, n=5, func="cos", **kw):
    data_norm, coord_norm = None, None
    
    if "coord" in kw.keys():
        data = np.concatenate((matrix, np.array([kw["coord"]])))
        data_norm = norm(matrix)
        coord_norm = data_norm[-1, :]
    else:
        data_norm = norm(matrix)
        coord_norm = data_norm[kw["pos"]]
    
    res = []
    for i in data_norm:
        if func=="cos":
            res.append(cos_siml(coord_norm, i))
        else:
            res.append(dist_eucl(coord_norm, i))
    if func=="cos":
        return np.array(res).argsort()[::-1][:n], res
    else:
        return np.array(res).argsort()[:n], res