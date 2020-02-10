import sg1

print(f"Please Enter 2 numbers for addition:")
num1=int(input())
num2=int(input())

result1=sg1.Add(num1,num2)

result2=sg1.Sub(num1,num2)

print(f"The result of Addition is: {result1}")
print(f"The result of Subtraction is: {result2}")