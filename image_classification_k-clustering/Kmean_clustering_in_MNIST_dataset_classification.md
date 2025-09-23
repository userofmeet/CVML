## Code
``` python
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
from sklearn.datasets import load_digits 
digits = load_digits() 
data = digits.data 
print(data.shape) 
#To improve the visualization, we invert the colors 
data = 255-data 
np.random.seed(1)
n=10 
kmeans = KMeans(n_clusters=n,init='random') 
kmeans.fit(data) 
Z = kmeans.predict(data) 
for i in range(0,n): 
    row = np.where(Z==i)[0] # row in Z for elements of cluster i 
    num = row.shape[0] # number of elements for each cluster 
    r = int(np.floor(num/10.)) # number of rows in the figure of the cluster 
    print("cluster "+str(i)) 
    print(str(num)+" elements") 
    plt.figure(figsize=(10,10)) 
    for k in range(0, num): 
        plt.subplot(r+1, 10, k+1) 
        image = data[row[k], ] 
        image = image.reshape(8, 8) 
        plt.imshow(image, cmap='gray') 
        plt.axis('off') 
    plt.show()
```

## Terminal Output
``` bash
cluster 0
182 elements
cluster 1
156 elements
cluster 2
197 elements
cluster 3
179 elements
cluster 4
180 elements
cluster 5
176 elements
cluster 6
166 elements
cluster 7
242 elements
cluster 8
93 elements
cluster 9
226 elements
```


## Output Plots
<img width="549" height="558" alt="image" src="https://github.com/user-attachments/assets/35bc1c7a-cc9c-4bad-977c-8f31774035c8" />
<img width="553" height="558" alt="image" src="https://github.com/user-attachments/assets/159467be-3052-4859-afe5-0cfd6e9fac47" />
<img width="547" height="557" alt="image" src="https://github.com/user-attachments/assets/35955b37-4a92-4e45-bd2f-e144f25bc0f4" />
<img width="550" height="558" alt="image" src="https://github.com/user-attachments/assets/e0082011-ff1d-40b0-90dc-160dd6069216" />
<img width="549" height="529" alt="image" src="https://github.com/user-attachments/assets/c66860a3-0118-4f71-865b-e0d3a1ca4b18" />
<img width="550" height="558" alt="image" src="https://github.com/user-attachments/assets/bde1cfb4-496e-4709-a61c-39a63527423d" />
<img width="552" height="558" alt="image" src="https://github.com/user-attachments/assets/93d68fe2-e185-4656-aaee-371b297638ac" />
<img width="543" height="557" alt="image" src="https://github.com/user-attachments/assets/170a993d-f2c0-484b-bf1d-b4e4dc98c0a4" />
<img width="571" height="557" alt="image" src="https://github.com/user-attachments/assets/95b2bc0a-3937-4cca-ac16-91004c7e6205" />
<img width="544" height="558" alt="image" src="https://github.com/user-attachments/assets/c3e80ec1-987c-4361-8a7a-fb15d499e0d4" />




