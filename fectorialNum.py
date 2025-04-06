num = int(input("enter number:"))

# def  toFindFectorial(num):
#     if num == 0 or num ==1:
#         return 1
#     else:
#         return num*toFindFectorial(num-1)

# result = toFindFectorial(num)
# print(result)    


                          # without using recursion
fect = 1
i =1
while i<=num:
    fect *= i
    i +=1
    
print(fect)    
