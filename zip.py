import pandas as pd 
i3=pd.read_csv('3bi.csv',header=None)
o3=pd.read_csv('3bo.csv',header=None)
b4=pd.read_csv('4b.csv',header=None)
fi=pd.read_csv('fi.csv',header=None)
rank=pd.read_csv('ranks.csv',header=None)
b4c=pd.read_csv('4b_call.csv',header=None)

#print(b4c.shape)
#print(b4c.pivot(index=[0,1], columns=2)[3])
#zipp=rank.merge(o3,how='outer',on=0).merge(i3,how='outer',on=0).merge(b4,how='outer',on=0).merge(fi,how='outer',on=0)
#zipp.to_csv('zip_ranks.csv')
b4c['new']=b4c[0]+b4c[1]+b4c[2].astype('str')
b4c=b4c[['new',3]]
print(b4c)
b4c.to_csv('b4c_n.csv', index=False)