import operators
print"SIMPLE CALCULATOR"
print"1=Add","2=Subtract","3=Divide","4=Multipy","5=Exit"
choice=raw_input("Choice")
first=int(raw_input("Enter Number"))
second=int(raw_input("Enter Number"))
if choice=="1":
	operators.add(first,second)
elif choice=="2":
	operators.sub(first,second)
elif choice=="3":
	operators.div(first,second)
elif choice=="4":
	operators.mult(first,second)
else:
	print"Exit"




	
	
