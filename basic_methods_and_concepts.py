import numpy as np
data= [12,23,45,23,45,65,76,34,56,34,23,64,76,45,34,86,97]
scores = np.array(data)
print("scores:",scores)
print("average:",np.mean(scores))
print("middle:",np.median(scores))
print("maximum:",np.max(scores))
print("minimum:",np.min(scores))
print("range:",np.ptp(scores))
print("variance:",np.var(scores))
print("standard deviation:",np.std(scores))
print("sum:",np.sum(scores))