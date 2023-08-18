import numpy as np
a=np.array([[1,2,4],[5,8,7]],dtype='float')
print("array created using passed list:\n",a)

b=np.array((1,3,2))
print("\n array created using passed tuple:\n",b)

c=np.zeros((3,4))
print("\n an array initialized with all zeros:\n",c)

d=np.full((3,3),6,dtype='complex')
print("\n an array initialized with all 6s","array type is complex:\n",d)

e=np.random.random((2,2))
print("\n a random array:\n",e)

f=np.arange(0,30,5)
print("\n a sequencial array with steps of 5:\n",f)

g=np.linspace(0,5,10)
print("\n a sequencial array with with 10 values between""0 and 5:\n",g)

arr=np.array([[1,2,3,4],[5,2,4,2],[1,2,0,1]])
newarr=arr.reshape(2,2,3)
print("\n original array:\n",arr)
print("reshaped array:\n",newarr)

arr=np.array([[1,2,3],[4,5,6]])
flarr=arr.flatten()
print("\n original array:\n",arr)
print("flatten array:\n",flarr)
