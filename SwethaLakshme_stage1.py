num1,num2,op = input().split(", ")
num1, num2=int(num1),int(num2)
result=0
if op=="+":
    result = num1+num2
elif op=="-":
    result = num1-num2
elif op=="*":
    result=num1*num2
elif op=="/":
    result=num1/num2
print("Result =",result)