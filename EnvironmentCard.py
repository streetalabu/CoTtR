class EnvironmentCard():
	# base class for all environmental cards
	card_id = 0

	def __init__(self, type):
		self.card_id = EnvironmentCard.card_id + 1
		EnvironmentCard.card_id += 1
		self.type = type
	
	def displayCount(self):
		print "Total Card %d" % EnvironmentCard.card_id

	def displayCard(self):
		print "Type:", self.type


class DisasterCard(EnvironmentCard):
	# base class for disaster cards
	dis_id = 0

	def __init__(self):
		self.type = type
		self.dis_id = DisasterCard.dis_id + 1
		DisasterCard.dis_id += 1
		self.city = []
		self.disaster = []

	def addCity(self, city_name):
		name = city_name
		self.city.append(name)
		return self.city

	def addDisaster(self, disaster):
		self.disaster.append()