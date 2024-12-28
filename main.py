ls=[7,2,10,5,3,9,4,8]
print("unsorted list: ",ls)
n=len(ls)
for i in range(n):
    for j in range(0,n-i-1):
        if ls[j]>ls[j+1]:
            ls[j] , ls[j+1] = ls[j+1] , ls[j]

print("sorted list: ", ls)