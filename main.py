from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "online"}

@app.get("/suggestions")
async def get_suggestions():
    suggestions = [
        {
            "name": "About Amal"
        }, 
        {
            "name": "Where has Amal worked?"
        }
    ]
    return suggestions