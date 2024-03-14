from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:30000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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