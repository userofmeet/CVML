## Code
```python
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
    x4 = np.random.standard_normal((100,2))*0.8-np.ones((100,2))+10 
    X = np.concatenate((x1,x2,x3,x4),axis=0) 
    return X 
#generate the k=3 initial centroids with the function 
n = 4 
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
plt.plot(X[labels==3,0],X[labels==3,1],'b.', label='cluster 4') 
plt.plot(centroids[:,0],centroids[:,1],'mo',markersize=8, label='centroids') 
plt.legend(loc='best') 
plt.show()
```
## Output
<img width="370" height="248" alt="image" src="https://github.com/user-attachments/assets/f6554e86-b4fb-46db-b7b3-50f2e6765182" />
<img width="370" height="248" alt="image" src="https://github.com/user-attachments/assets/9500ba37-48ff-4de7-b7e4-050a028ea4e7" />
