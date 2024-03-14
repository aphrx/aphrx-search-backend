from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "online"}

@app.get("/suggestions")
async def get_suggestions():
    suggestions = [
        {
            "id": 1,
            "name": "About Amal"
        }, 
        {
            "id": 2,
            "name": "Where has Amal worked?"
        }
    ]
    return suggestions