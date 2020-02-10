import sg1

num1        = float(input("Enter first num :"))
num2        = float(input("Enter second num :"))
print('Select Operator')
operator    = input("Add or Sub :")


if operator.lower() == 'add':
    result = sg1.Add(num1, num2)
    print(f"Answer  = {result}")

elif operator.lower() == 'sub':
    result = sg1.Sub(num1, num2)
    print(f"Answer  = {result}")
 