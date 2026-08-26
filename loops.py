# Printing all odd number from 1 to 20
# for i in range(1,20):
    # if i % 2 != 0:
        # print(i)

# print all odd number from 1 to 20 by using only range
# for i in range(1,20, 2):
#     if i % 2 != 0:
#         print(i)

# print all multiples of 3 from 1 to 50 but skip 15
for i in range(1,50, 2):
    if(i == 15 or i == 9):
        continue
    # if i % 3 == 0:
    print(i)


#Take two integers as a and b and  Find and print the first number between 1 and 1000 that is divisible by both number
a = int(input("Select 1st number: "))
b = int(input("Select 2nd number: "))

for i in range(1,1001):
    if(i % a == 0 and i % b == 0):
        print(i)
        break