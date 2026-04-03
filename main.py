num = int(input("Enter an integer: "))

count = 0       

temp = num

while temp:
    if temp & 1:
        count += 1
    temp >>= 1

print(f"number of ones: {count}")