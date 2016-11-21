
# coding: utf-8

# In[12]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[13]:

files=pd.read_table("clusterlists.dat", header=None)
files


# In[14]:

data={}
for i, file in enumerate(files[0]):
    data[str(file)]=np.loadtxt(str(file))
datafr=pd.DataFrame.from_dict(data, orient='index')
datafr=datafr.transpose()
datafr=datafr.rename(columns={'Clustersi1000000.dat':'1000000',
              'Clustersi100000.dat':'100000',
              'Clustersi10000.dat':'10000',
              'Clustersi1000.dat':'1000',
              'Clustersi100.dat':'100',
              'Clustersi2000000.dat':'2000000',
              'Clustersi3000000.dat':'3000000',
              'Clustersi4000000.dat':'4000000',
              'Clustersi5000000.dat': '5000000',
              'Clustersi6000000.dat': '6000000',
              'Clustersi7000000.dat': '7000000',
              'Clustersi8000000.dat': '8000000',
              'Clustersi9000000.dat':'9000000'})
datafr=datafr.sort_index(axis=1)


# In[15]:

datafr.plot.box(showfliers=False, rot=30)
#plt.xticks(x, labels, rotation='vertical')


# In[22]:

maxes=datafr.max(axis=0).tolist()
list=datafr.columns.values.tolist()
fig=plt.figure()
ax=fig.add_subplot(1, 1, 1)
ax.scatter(list, maxes, label="maximal cluster size")
ax.set_xlabel("time step")
ax.set_ylabel("cluster size")
plt.show()
#ax.set_xscale('log')


# In[ ]:



