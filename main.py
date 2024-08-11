#check if number divisible by 3 or 5 if 3 print fizz with no. if 5 print buzz, both print fizz buzz same line

def fb(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print(i , "fizzbuzz", sep = "_")
        elif i % 3 == 0:
            print(i ,"fizz", sep = "_")
        elif i % 5 == 0:
            print(i, "buzz", sep = "_")
        else:
            print(i)

number = int(input("Max Limit of Program: "))

fb(number)

#check if number divisible by 3 or 5 if 3 print fizz with no. if 5 print buzz, both print fizz buzz same line
#following code prints output as list       
# result = []
# def fb(n):
#     for i in range(1,n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             result.append("fizzbuzz!")
#         elif i % 3 == 0:
#             result.append("fizz")
#         elif i % 5 == 0:
#             result.append("buzz")
#         else:
#             result.append(i)

# number = int(input("Max Limit of Program: "))

# fb(number)

# print(result)

