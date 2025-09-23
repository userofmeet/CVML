## Code
``` python
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
np.random.seed(7) 
#generate 2D random data for three clusters and represent them 
def generate_data(): 
    np.random.seed(7) 
    x1 = np.random.standard_normal((100,2))*0.6+np.ones((100,2)) 
    x2 = np.random.standard_normal((100,2))*0.5-np.ones((100,2)) 
    x3 = np.random.standard_normal((100,2))*0.4-2*np.ones((100,2))+5 
    X = np.concatenate((x1,x2,x3),axis=0) 
    return X 
#generate the k=3 initial centroids with the function 
n = 3 
X = generate_data() 
plt.plot(X[:,0],X[:,1],'k.') 
plt.show() 
k_means = KMeans(n_clusters=n) 
model = k_means.fit(X) 
centroids = k_means.cluster_centers_ 
labels= k_means.labels_ 
plt.figure() 
plt.plot(X[labels==0,0],X[labels==0,1],'r.', label='cluster 1') 
plt.plot(X[labels==1,0],X[labels==1,1],'b.', label='cluster 2') 
plt.plot(X[labels==2,0],X[labels==2,1],'g.', label='cluster 3') 
plt.plot(centroids[:,0],centroids[:,1],'mo',markersize=8, label='centroids') 
plt.legend(loc='best') 
plt.show()


```
## Output
<img width="370" height="248" alt="image" src="https://github.com/user-attachments/assets/dbc7598d-8c1c-437d-a8b3-7a3a866b20b0" />
<img width="370" height="248" alt="image" src="https://github.com/user-attachments/assets/3e97aad6-6603-4470-95bb-d85bdde0615d" />

