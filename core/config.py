import dotenv
import os


class Settings():

    dotenv.load_dotenv()

    app_port = os.getenv("PORT")
    app_host = os.getenv("HOST")
    huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

settings = Settings()

