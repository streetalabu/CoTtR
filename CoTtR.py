# ----- Setup -----

from pymongo import MongoClient
from Database import *
from random import choice, sample

# Database variables
link_collection = db.CityCollection
city_collection = db.cities

# ----- Create Card Deck -----

# ** Create variables from database data**
# Get all links
all_links_cursor = link_collection.find()
all_links = []
for link in all_links_cursor:
	all_links.append(link)

# Count of all total links 
all_links_count = len(all_links)

# Get all cities
all_cities_cursor = city_collection.find()
all_cities = []
for city in all_cities_cursor:
	all_cities.append(city)

# count of all cities
all_cities_count = len(all_cities)

# ** Set constants for card deck creation **
# Setup ratios of card type
link_ratio = .9
city_ratio = .1
card_deck_count = 100
link_count = round(card_deck_count * link_ratio)
city_count = card_deck_count - link_count

# ** Create the card deck **
# Build collection of links
link_cards = []
while len(link_cards) < link_count:
	new_link = sample(all_links, 1)
	link_cards.append(new_link)

# Build collection of cities
city_cards = []
while len(city_cards) < city_count:
	new_city = sample(all_cities, 1)
	city_cards.append(new_city)

# Combine collections into card deck
card_deck = link_cards + city_cards

# Set constants for positive/negative results
pos = .33
neg = .67

# ----- Gameplay -----

# ** Opening Instructions **
# Sets input direction strings that will be printed to user
opening_statement = '''
Welcome to Collaborative Ticket to Ride'''
opening_instructions = '''
Instructions:
At the given prompts, simply press Enter to get a new card.  
If the game is finished type "end" before pressing Enter to quit the program.'''
instruction_input_string = '''Would you like instructions? 
Type "yes" then press Enter, otherwise just press Enter: '''
new_card_input_string = 'Press Enter to draw a new card or type "end" to end the program: '

# Display opening statement
print opening_statement

# Ask and give instructions if needed
user_input = raw_input(instruction_input_string)
if user_input == 'yes':
	print opening_instructions

# ** Draw Cards **
# Sets strings for card display
drawn_card_string = '''You've drawn a card:'''
first_draw_string = '''Press Enter to draw the first card'''
drawn_link_string = '''
	You've drawn a disaster card between {0} and {1}
'''
drawn_city_string = '''
	You've drawn a disaster card for the city of {0}
'''

# Loop to draw cards
drawn_card_deck = [1]
while raw_input(new_card_input_string) != 'end':
# Draws a card from the deck
	drawn_card_raw = sample(card_deck, 1)
	drawn_card = drawn_card_raw[0][0]
	while drawn_card in drawn_card_deck:
		drawn_card_raw = sample(card_deck, 1)
		drawn_card = drawn_card_raw[0][0]
	#card_type = drawn_card.get('city one', drawn_card.get('city_name'))
	#display =  drawn_card.get('city one', drawn_card.get('city_name'))
	city_name = drawn_card.get('city_name')
	if city_name == None:
		city_one = drawn_card['city one']
		city_two = drawn_card['city two']
		print (drawn_link_string.format(city_one, city_two))
	else:
		print (drawn_city_string.format(city_name))
	drawn_card_deck.append(drawn_card)