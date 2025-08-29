from dotenv import load_dotenv
import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constant import MODEL

load_dotenv()

def get_model_client():

    model_client = OpenAIChatCompletionClient(api_key=os.getenv("GOOGLE_API_KEY"),model=MODEL)

    return model_client

