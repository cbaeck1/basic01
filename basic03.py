import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display

f = open('iris.csv')

# 첫번째 줄
line = f.readline()
features = line.strip().split(',')[:4]

labels = ['Iris-setosa', 'Iris-versicolor', 'Iris virginica']

data = []
    
for line in f:
    I = line.strip().split(',')
    I[0] = int(I[0])
    I[1] = float(I[1])         # for문으로 해보기
    I[2] = float(I[2])
    I[3] = float(I[3])
    I[4] = float(I[4])

    I[5] = labels.index(I[5])
    data.append(I)
    
f.close()


'''
    I[0] = int(I[0])
    I[1:4] = [float(i) for i in I[1:4]]
'''
# X축값 1,2,3과 Y축값 110,130,120을 가지고 라인 플롯
# plt.plot([1,2,3], [110,130,120])
# plt.show()

iris = np.array(data)
display(type(iris), iris.shape, len(iris), iris[0])

display(iris[:,1])
display(plt.plot(iris[:,0], iris[:,1]))
plt.plot(iris[:,0], iris[:,1])
plt.show()

plt.plot(iris[:,0],iris[:,1])
plt.plot(iris[:,0],iris[:,2])
plt.plot(iris[:,0],iris[:,3])
plt.plot(iris[:,0],iris[:,4])

plt.title('Iris features', fontsize = 15)
plt.legend(['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'])
plt.show()

