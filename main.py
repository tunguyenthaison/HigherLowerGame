from art import logo, vs
from game_data import data
import random

print(logo)
# Randomly pick 2 items from the data set
# An entry has the form 
# {'name': 'Kevin Hart', 'follower_count': 89, 'description': 'Comedian and actor', 'country': 'United States'}
	
def print_from(entry, _name):
	"""
	print out name (A or B) and its entry except the number of follower_count
	"""
	name = entry['name']
	description = entry['description']
	country = entry['country']
	print(f"Compare {_name}: {name}, a {description}, from {country}.")
	#print("Compare A: {name}, a {description}, from {country}.".format(name = entry['name'], description = entry['description'], country = entry['country']))

def max2Items(A,B):
	"""
	return item with max of followers
	"""
	if A['follower_count'] > B['follower_count']:
		return A 
	else:
		return B

#print_from(A,'A')	

def game():
	score = 0
	# first round
	firstItem = random.choice(data)
	is_true = True
	while is_true:
		print("-----------------------")
		secondItem = random.choice(data)
		print_from(firstItem, 'A')
		print(vs)
		print_from(secondItem, 'B')
		guess = input("Who has more followers? Type 'A' or 'B': ")
		# Processing
		# Find the item with bigger followers
		winner = max2Items(firstItem, secondItem)
		# Assign the item correspond to the guess as a letter A or B
		if guess == "A":
			guessItem = firstItem
		else:
			guessItem = secondItem
		# Now do compare to see if the guess is correct or not
		if guessItem != winner:
			print(f"Sorry, that's wrong. Final score {score}.")
			is_true = False
			return
		else:
			score+=1
			print(f"You're right! Current score {score}.")
			firstItem = winner

game()




