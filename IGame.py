class IGame:
	playerActions: dict
	screenActions: dict

	#This is the constructor, do whatever you want to construct here
	def IGame(self):
		self.playerActions = {};
		self.screenActions = {"Type": "None"};
		pass

	#This will be called when a new player joins the game
	def addPlayer(self, playerId: str) -> void:
		self.playerActions[playerId] = {"Type": "None"};

	# I will write this, call this function when you want to show text to a specific player
	# Will return true if playerId is valid
	def showTextToPlayer(self, playerId:str, text: str) -> bool:
		if(playerId in playerActions):
			self.playerActions[playerId] = {"Type":"TextShow", "Text":text}
			return True
		return False

	
	# Gives the player multiple options to choose from
	def askOptionsOfPlayer(self, playerId: str, questionText: str, options: [str]) -> bool:
		if(playerId in playerActions):
			self.playerActions[playerId] = {"Type":"OptionAsk", "Question":questionText, "Options":options}
			return True
		return False


	# Asks the player to input text
	def askTextOfPlayer(self, playerId: str, questionText: str)-> bool:
		if(playerId in playerActions):
			self.playerActions[playerId] = {"Type":"TextAsk", "Question":questionText}
			return True
		return False


	# Will be called when a player selects a response after an ask
	# response is a dictionary where the key is the playerId and the value is their response
	def getResponseFromPlayer(self, playerId: str, response: dict) -> void:
		pass


	# Call this to show text on the main screen
	def showTextOnScreen(self, titleText: str, secondaryText: str)-> void:
		self.screenActions = {"Type":"TextShow", "Title": titleText, "Secondary" : secondaryText}

	# Will return what the player needs to do next
	# I will write this
	def bufferedActions(self, playerId: str) -> dict:
		if(playerId in playerActions):
			return self.playerActions[playerId]
		elif playerId == "Screen":
			return self.screenActions
		return {"Type" : "ERROR"}

