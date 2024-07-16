numbers_1 = []
numbers_2 = []
numbers_3 = []
for a in range(1,101):
    if a%2 ==0 :
        numbers_1.append(a)
    elif a % 3 ==0 :
        numbers_2.append(a)
    elif a % 5 ==0 :
        numbers_3.append(a)

print(numbers_1)
print(numbers_2)
print(numbers_3)