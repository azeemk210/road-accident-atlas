from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import deaths

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev, later restrict to frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include router
app.include_router(deaths.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Road Safety Atlas API is running"}
