n = int(input("Enter a Number : "))
sum = 0
curFac = 1

for i in range(1, n+1):
    curFac = curFac*i
    sum = sum + curFac

print(sum)
