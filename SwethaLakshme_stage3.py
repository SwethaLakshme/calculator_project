name, sub1, sub2, sub3 = input().split(", ")
sub1,sub2,sub3=int(sub1),int(sub2), int(sub3)
total=sub1+sub2+sub3
per =total/3
print(name)
print("Total: ", str(total)+"/"+str(300))
print("Percentage: ", per,end="%")

if per >= 75: print("\nGrade: A")
elif per >= 60:  print("\nGrade: B")
elif per >= 40:  print("\nGrade: C")
elif per < 40:  print("\nGrade: F")