import random
def hangman(choice):
	key=True
	key2=True
	key3='n'
	turn=9
	key4='Y'
	word=['ball','banana','cheat','friend','missrobot']
	theword=random.choice(word)
	if not choice.isalpha():
		print("Sorry You enter a special character,try again")
	else:
		while key:
			if key3 =='Y':
				print("Enter you Expect:")
				choice=input()
			if choice in theword:
				print("Congratulations You were right $_$")
				print("Do you want to play again:Y/N")
				while key2:
					choice2=input()
					choice2.lower()
					if choice2=='y':
						key2=False
						key4='n'
						main()
					elif choice2=='n':
						key4='n'
						print("                 By Miss.Robot")
						break
					else:
						print("Enter Y OR N")										
			else:
				turn=turn-1
				if turn == 8:
					print(' 0 ')
					key3='Y'
				elif turn ==7:
					print(' 0 ')
					print(' | ')
				elif turn ==6:
					print(' 0 ')
					print(' |\\')
				elif turn ==5:
					print(' 0 ')
					print('/|\\')
				elif turn ==4:
					print(' 0 ')
					print('/|\\')
					print(' | ')
				elif turn ==3:
					print(' 0 ')
					print('/|\\')
					print(' | ')
					print('  \\')
				elif turn ==2:
					print(' 0 ')
					print('/|\\')
					print(' | ')
					print('/ \\')
				elif turn ==1:
					print(' 0 ')
					print('/|\\')
					print(' | ')	
					print('/_\\')
					print("Aa OWAW The hangman is there")
					break
			if key4=='n':
				break
def main():
	print("Hello There! You are playing the Hangman game if you Know it that ok if not here what you have to do:^_^")
	print("Expect a Letter from a word we The machine choose Have Fun")
	print("please Enter you Expect:")
	choice=input()
	hangman(choice)
main()
