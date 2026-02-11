import pandas as pd

data = [x for x in range(0, 8, 2)]

myvar = pd.Series(data, index = ['x', 'y', 'z', 'b'])

print(myvar)