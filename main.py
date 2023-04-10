from fastapi import FastAPI
import bot

app = FastAPI()
bot.polling()

@app.get("/")
async def root():
    return {"message": "Hello World"}