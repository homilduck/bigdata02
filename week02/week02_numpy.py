# 넘파이 (Numpy)
# 써드파티 라이브러리 (별도의 설치가 필요, 단 colab에는 기본 설치가 되어 있음)
# 파이썬에서 수치 계산을 위한 핵심 라이브러리
# 다차원 배열 객체와 이를 다루기 위한 다양한 함수 제공

import numpy as np

np.random.seed(50) # 시드 설정

x = np.random.random(5) # 0 ~ 1 사이의 실수 5개 랜덤 추출
print(x)
y = np.random.randint(1,10,5) # 1 ~ 9 사이의 정수 5개 랜덤 추출
print(y)
z = np.random.normal(0, 1, 5)  # 정규분포
print(z)

# q = np.arange(1, 6)
# choice = np.random.choice(q, 3)
# print(choice)

q = np.array(["가위", "바위", "보"])
choice = np.random.choice(q, 2)
print(choice)


# 조건부 선택과 필터링
#h = np.arange(1, 6)

#mask = h > 2
#print(h[mask])

#result = np.where(h > 3, h, 0)  # 3보다 큰 값은 그 값 그대로 3이하의 값은 0으로 처리
#print(result)

#g = np.array([
#    [3, 2, 1],
#    [6, 5, 4]
#])
#print(np.sum(g))
#print(np.sum(g, axis=0))  # 열 기준을 축으로 더함
#print(np.sum(g, axis=1))  # 행 기준을 축으로 더함

#print(np.mean(g))  # 산술평균  21/6
#print(np.max(g))
#print(np.min(g))
#print(np.std(g))  # 표준편차 standard deviation

#c = np.arange(1,13)

#r = c.reshape(2,2,3) # 3차원 배열형태로 변환
#r = c.reshape(4,3) # 2차원 배열형태로 변환
#print(c)
#print(r)
#f = r.flatten() # 2차원 배열형을 1차원 배열로 변환
#print(f)

## 전치행렬
#t = r.T
#print(t)

# 단위행렬
#e1 = np.eye(4)
#print(e1)

#a = np.array([3,2,1])
#b = np.array([6,5,4])

# 산술연산
#print(a+b)
#print(a+b)
#print(b**2)
#print(a*10)
#print(b*2)


#arr = np.arange(1,6)
#print(arr)

# indexing
#print(arr[2])
#print(arr[4],arr[-1],arr[(arr)-1])

#a = np.array([1,2,3,4,5])
#b = np.array([6,7,8,9,10])
from numpy.ma.core import zeros

#zeros = np.zeros((3,4))
#zeros = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]], dtype=float)
#print(zeros)

#ones = np.ones((3,5))
#ones = np.array([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1,]], dtype=float )
#print(ones)

#range_array = np.arange(0,20,2)
#range_array = np.arange(1,10)
#range_array = list()
#for i in range(1,10):
#    range_array.append(i)
#print(range_array)

#space_array = np.linspace(0,1,5) # 0부터 1까지 숫자 5개로 구간 설정
#print(space_array)

#arr = np.array(["korean","English","Matmatics"])
#arr = np.array([[1,2,3,],[4,5,9]])
#arr = np.array(
#    [
#
#        [
#            [1.0,2.0,3.1],
#            [4.2,5.9,9.1]
#        ],
#        [
#            [1.1,0.8,2.1],
#            [6.3,1.9,77.1]
#        ]
#
#
#    ]
#)
#
#print(arr)
#print(arr.shape, arr.dtype, arr.ndim, arr.size)
# 위 3차원 배열에서 1.9만 출력
#print(arr[1][1][1])
#print(arr[1,1,1])  #Numpy

# 리스트를 대신 배열을 사용하는 이유
#list1 = [1,2,3,4,5]
#array1 = np.array(list1) # 파이썬 리스트를 넘파이 배열로 변환
#print(list1, type(list1))
#print(array1, type(array1))

#array2 = np.array([1,2,3],[4,5,6])
#print(array2, type(array2))
#print(list1)
#arr1 = np.array(list1)
#print(arr1)