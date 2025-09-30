import numpy as np
atributes = np.array([ [0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([0, 1, 1, 1])
w = [1, 1]
threshold = 0.5
bias = 0
alpha = 0.2
epoch = 50
print("learning rate: ", alpha,", threshold: ", threshold)
for i in range(0, epoch):
    print("epoch ", i+1)
    global_delta = 0
    for j in range(len(atributes)):
        actual = labels[j]
        sum = atributes[j][0]*w[0] + atributes[j][1]*w[1] + bias
        if sum > threshold:
            predicted = 1
        else:
            predicted = 0
        delta = actual - predicted
        global_delta = global_delta + abs(delta)
        for k in range(0, 2):
             w[k] = w[k] + delta * alpha
             print(atributes[j][0]," ", labels, " ", atributes[j][1], " -> actual: ", actual, ", predicted: ",predicted, " (w: ",w[0],")")
             if global_delta == 0:
                 break
             print("------------------------------")
