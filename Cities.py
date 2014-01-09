all_cities = ("Lisboa", 'Cadiz')

class EuroCity():
	city_id = 0
	
	def __init__(self, name):
		self.city_id = EuroCity.city_id + 1
		EuroCity.city_id += 1
		self.city_connection = []
		self.city_name = name

	def connectCity(self, city_name, distance, color, type = 'normal'):
		connection = {"city": city_name, "distance": distance, "color": color, "type": type}
		self.city_connection.append(connection)