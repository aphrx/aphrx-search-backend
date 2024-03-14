from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "online"}

@app.get("/suggestions")
async def get_suggestions():
    suggestions = [
        "About Amal",
        "Where has Amal worked?"
    ]
    return suggestions