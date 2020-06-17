import numpy as np
import matplotlib.pyplot as plt

f=open('iris.csv')

datalist = []

head = f.readline()                           # 첫 줄 빠짐
head = head.strip().split(',')[:4]
print(head)

for line in f:
  I = line.strip().split(',')             # 첫 줄 빼고 나머지 150줄을 data 리스트에 집어 넣었다.
  I[0] = int(I[0])
  I[1] = float(I[1])         # for문으로 해보기
  I[2] = float(I[2])
  I[3] = float(I[3])
  I[4] = float(I[4])

  if I[5] == 'Iris-setosa':       # 딕셔너리를 이용해 해보기
    I[5] = 0
  elif I[5] == 'Iris-versicolor':
    I[5] = 1
  else:
    I[5] = 2

  datalist.append(I)

f.close()

#for row in datalist:
#  print(row)

# 리스트 안에는 1차원의 형태로 리스트, 딕셔너리, 숫자, 문자 섞어서 모두 들어갈 수 있다.
# numpy는 2차원의 형태이므로, 행렬처럼 직사각형 모양으로 안에 들어가는 형태와 크기가 같아야 한다.

iris = np.array(datalist)
print(iris.shape)
print(iris[-1])
print(iris[1])

print(len(iris), iris[1,1])
print(iris[:3])
print(iris[-3:])

# 리스트와 array 차이
alist = [1,2,3]
print(alist)
# 리스트를 3개
print('alist*3', alist*3)

arrlist = np.array(alist)
print(arrlist)
# array 각 원소에 3을 곱하는
print('arrlist*3', arrlist*3)

# 두개 리스트를 결합
blist = [2,3,4]
print('alist + blist', alist + blist)

# 같은 위치의 원소끼리 덧셈
arrblist = np.array(blist)
print('arrlist + arrblist', arrlist + arrblist)

#  
a = np.zeros([2,2]) # np.zeros((2,2))
print(a)
print(a.shape)

np.ones([2,2])

# 대각행렬
np.eye(5)

# 1부터 99까지 1차원적 나열
np.arange(50)

# 40부터 49까지
np.arange(40,50)

#조건식을 적용하면 데이터 결과 값이 bool이 된다.
print(iris > 1)

print((iris>1).sum())



