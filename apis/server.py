from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import config
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
def get_server_status():
    return f'Server is started and running successfully in port: {config.get("PORT")}'
