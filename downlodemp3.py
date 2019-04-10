import pandas as pd

l1=[100,200,300]
l2=['x','y','z']
s1=pd.Series(l1,index=l2)
print(s1)
