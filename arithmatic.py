def Add(num1,num2):
    add=num1+num2
    return(add)
def Sub (num1,num2):
    sub = num1-num2
    return(sub)


x = int(input("Enter the num1:"))
y = int(input("Enter the num2:"))
ans = Add(x,y)
ans1 = Sub(x,y)

print(f"Sum of {x} and {y} is {ans}")
print(f"Subtraction of {x} and {y} is {ans1}")

