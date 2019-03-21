import pandas as pd
import numpy as np

df1 = pd.DataFrame([[1,2,3],[4,5,6]])
print(df1)

df2 = pd.DataFrame([[1,2,3],[4,5,6]],index=['row1','row2'],columns=['c1','c2','c3'])
print(df2)

dates = pd.date_range('2019-6-16',periods=7)
df3=pd.DataFrame(np.random.randn(7,4),index = dates ,columns = list('abcd'))
print(df3)

'jjkkggg'
'jkljhjjk'
HOW TO PULL WWW