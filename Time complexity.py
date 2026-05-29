#Time complexity

#Constant
a=[10,29,39,48,38]
print(a[2]) #O(1)

#Linear complexity
n=int(input())
for i in range(n):
    print(i) #O(n)
    
#Quadratic complexity
n=5
for i in range(n):
    for j in range(n):
        print(i,j) #n*n=O(n^2)
        
#Cubic complexity
n=3
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i,j,k) #n*n*n=n^3
            
#Logarithmic ,Binary search
mid=0
high=n-1
while(low<high):
    mid=(low+high)//2 #O(logn)

#Ex1
a=4
b=9
print(a+b) #3 TC=O(1)

#Ex2
n=int(input())
for i in range(n):
    print(i) #n loop + input (n+1) #O(n)
