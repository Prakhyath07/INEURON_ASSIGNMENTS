list1=[i*j for i in ["x","y","z"]for j in range(1,5) ]
print(list1)


list2=[i*j for i in range(1,5) for j in ["x","y","z"]]
print(list2)

list3= [[i] for j in range(3) for i in range(j+2,j+5)]
print(list3)

list4=[[i for i in range(j+2,j+6)]for j in range(4)]
print(list4)

list5=[(i,j)for j in range(1,4) for i in range(1,4)]
print(list5)