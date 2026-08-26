#Dictionary
users_age = {
    "Hashir": 29,
    "Umer": 25,
    "zammar": 21
    }

print(users_age["Hashir"])

#get unique roll number
roll_numbers = {101,105,102,101,108,105,110}
print(roll_numbers)

employees = [
    (1,'Hashir'),
    (2, "Naeem"),
    (3, "Mubashir")
]

userId = int(input("Enter your id: "))
for i in employees:
    if i[0] == userId:
        result = i[1]
        break
    else:
       result = "No employee found"

print(result)