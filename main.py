from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"] 
)

@app.get("/user")
async def read_root():
    return {
        "email": "sobowalegz2@gmail.com",
        "current_datetime": datetime.now().isoformat(),
        "github_url": "https://github.com/Matutozi/HNG-week1"
    }