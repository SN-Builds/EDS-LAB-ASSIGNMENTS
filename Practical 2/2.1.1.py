list1=["Add","Remove","Display","Quit"]
list=[]
while True:
	for i in range(len(list1)):
		print(f"{i+1}. {list1[i]}")
	choice = int(input("Enter choice: "))
	if choice==1:
		try:
			a=int(input("Integer: "))
			list.append(a)
			print("List after adding:",list)
		except int:
			print("Invalid input")
	elif choice ==2:
		if list==[]:
			print("List is empty")
			continue
		a=int(input("Integer: "))
		if a in list:
			list.remove(a)
			print("List after removing:",list)
		else:
			print("Element not found")
	elif choice==3:
		if list ==[]:
			print("List is empty")
		else:
			print(list)
	elif choice==4:
		break
	else:
		print("Invalid choice")
		
