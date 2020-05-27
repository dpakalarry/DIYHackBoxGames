from fastapi import FastAPI
import IGame
import uuid

app = FastAPI()

game: IGame

@app.get("/initPlayer")
async def root() -> str:
	newId = str(uuid.uuid4())
	game.addPlayer(newId)
	return newId


@app.on_event("startup")
async def startup_event():
	game = IGame()          #Change to overloaded IGame

@app.get("/refresh")
async def refresh(playerId: str)  -> dict:
	return game.bufferedActions(playerId)

@app.get("/return")
async def refresh(playerId: str, value: dict)  -> void:
	game.getResponseFromPlayer(playerId, value)