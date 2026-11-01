import numpy as np
data= [
    [56,87,56],
    [76,34,23],
    [75,34,23],
    [86,45,23],
    [64,23,12],
    [75,34,12]
]
scores = np.array(data)
print("scores:",scores)
print("average:",np.mean(scores))
print("average:",np.mean(scores,axis=0))
print("middle:",np.median(scores))
print("middle:",np.median(scores,axis=0))
print("maximum:",np.max(scores))
print("maximum:",np.max(scores,axis=0))
print("minimum:",np.min(scores))
print("minimum:",np.min(scores,axis=0))
print("range:",np.ptp(scores))
print("variance:",np.var(scores))
print("standard deviation:",np.std(scores))
print("standard deviation:",np.std(scores,axis=1))
print("standard deviation:",np.std(scores,axis=0)) 
print("sum:",np.sum(scores))