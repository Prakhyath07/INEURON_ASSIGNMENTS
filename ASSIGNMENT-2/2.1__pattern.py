n=5
# for j in range(1,n+1,1):
#     print("*"*j)
# for i in range(n-1,0,-1):
#     print("*"*i)

# for i in range(1,(2*n)+1):
#     if i<=n:
#         for j in range(i+1):
#             pass
#     elif i>n:
#         for j in range(2*(n)+1,(2*n)-i-1,-1):
#             pass
#     print("*"*j)

# for i in range(1,(2*n)+1):
#     if i<=n:
#         j=i
#     elif i>n: 
#         j=2*n-i
#     print("*"*j)

for i in range(1,(2*n)+1):
    if i<=n:
        for j in range(i):
            print("*",end=" ")
        print("")
    if i>n:
        for j in range((2*n)-i,0,-1):
            print("*",end=" ")
        print("")