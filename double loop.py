#이중 반복문
print("구구단을 출력합니다./n")
for x in range(2,10):
    print("------ [" + str(x) + "단]-------")
    for y in range(1,10):
        print(x,"X", y, "=", x*y)
print("--------------")


#
for i in range(1, 10) :
    for k in range(11,20):
        print(i, k)

#
m=[[1,2,3],[4,5,6],[7,8,9]]
print(m[1])

#
m=[[1,2,3],[4,5,6],[7,8,9]]
for i in m:
    print(i)

#
m=[[1,2,3],[4,5,6],[7,8,9]]
for i in m:
    for k in i:
        print(i)