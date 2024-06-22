import dotenv
import os


class Settings():

    dotenv.load_dotenv()

    app_port = os.getenv("PORT")
    app_host = os.getenv("HOST")
    openai_api_key = os.getenv("OPENAI_API_KEY")


settings = Settings()

