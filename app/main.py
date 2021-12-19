from fastapi import FastAPI
from . import config  #, models
from .database import engine
from .routers import post, users, auth, votes
from fastapi.middleware.cors import CORSMiddleware
# App init
app = FastAPI()

# app config
settings = config.Settings

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# models.Base.metadata.create_all(bind=engine)

# end of app config

# app routing

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)


# end of routes

@app.get("/")
def root():
    return {"msg":"Hello World"}