# longest consecutive ones

num = int(input("Enter an integer: "))

count = 0       
temp = num
lst = []

while temp:
    if temp & 1:
        count +=1
        temp >>= 1
    else:
        lst.append(count)
        count = 0
        temp >>= 1
print(lst)

# print(f"number of consecutive ones: {count}")


# while temp:
#     if temp & 1:
#         count += 1
#     temp >>= 1
#     if count >=1:
#         if count == count:
#             break