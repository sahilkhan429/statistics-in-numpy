import numpy as np
data= [1672,2233,4675,2543,4875,6655,7766,3974,5766,3094,2093,6984,7876,4765,3764,8986,9987]
salries = np.array(data)
print("salries")
print(salries)
print("mean")
print(np.mean(salries))
print("median")
print(np.median(salries))

print("PERCENTILES")
print(np.percentile(salries,25))
print(np.percentile(salries,50))
print(np.percentile(salries,75))
print(np.percentile(salries,95))
print("QUANTILES")
print(np.quantile(salries,[0.25,0.50,0.75]))