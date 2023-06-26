from config import config
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app_dir="./apis", app="server:app", host=config.get("HOST"), port=config.get("PORT"), reload=True,
                log_level="debug")
