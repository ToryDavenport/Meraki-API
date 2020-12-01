### Python Menu
running = True
while running == True:
		print("Welcome to my menu: ")
		print("option1:") 
		print("option2:")
		print("option3:") 
		print("option4:")
		print()

		choice = input("Please make a choice or type 'quit' to exit program: ")

		if choice == "1":
			print("Choice 1!")
		elif choice == "2":
			print("Choice 2!")
		elif choice == "3":
			print("Choice 3!")
		elif choice == "4":
			print("Choice 4!")
		elif choice == "quit":
			exit()
		else:
			print("Invalid Option, Try again!")