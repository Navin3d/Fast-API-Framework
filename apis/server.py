from fastapi import FastAPI
from config import config
app = FastAPI()


@app.get("/")
def get_server_status():
    return f'Server is started and running successfully in port: {config.get("PORT")}'
