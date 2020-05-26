class IGame:
	def IGame(self):
		pass
		#This is the constructor, do whatever you want to construct here

	def addPlayer(self, playerId: str) -> void:
		pass
		#This will be called when a new player joins the game

	def showTextToPlayer(self, playerId:str, text: str) -> bool:
		pass
		# I will write this, call this function when you want to show text to a specific player
		# Will return true if playerId is valid

	def askOptionsOfPlayer(self, playerId: str, questionText: str, options: [str]) -> bool:
		pass
		# Gives the player multiple options to choose from

	def askTextOfPlayer(self, playerId: str, questionText: str)-> bool:
		pass
		# Asks the player to input text

	def getResponseFromPlayer(self, response: dict) -> void:
		pass
		# Will be called when a player selects a response after an ask
		# response is a dictionary where the key is the playerId and the value is their response

	def showTextOnScreen(self, titleText: str, secondaryText: str)-> void:
		pass
		# Call this to show text on the main screen
		# I will write this


