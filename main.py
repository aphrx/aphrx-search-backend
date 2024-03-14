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
            "name": "About Amal",
            "description": """
            #Hi

            Based in Toronto, I am Amal Parameswaran, a Software Developer with a Bachelor's in Software Engineering from Ontario Tech University, where I achieved highest distinctions. My career has been dedicated to engineering innovative software solutions, with a strong background in developing resilient backends and automating cloud deployments using Python, FastAPI, Azure, AWS, and GCP. 
            
            My roles at AnalyticSmart, QA Consultants, and CIBC have honed my skills in Java, Python, JavaScript, Django, Flask, React, and database management, alongside a passion for continuous learning and embracing new technologies.I thrive on collaboration and am always looking to connect with tech enthusiasts and professionals. Feel free to reach out if you're interested in discussing technology, potential collaborations, or just sharing insights.
                """
        }, 
        {
            "id": 2,
            "name": "Where has Amal worked?",
            "description": "Analyticsmart, QA Consultants, Ontario Tech University, CIBC"
        }
    ]
    return suggestions