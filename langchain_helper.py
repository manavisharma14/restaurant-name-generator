from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

# Load API Key from .env file (Recommended)
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Initialize Hugging Face Inference Client
client = InferenceClient(model="tiiuae/falcon-7b-instruct", token=HUGGINGFACE_API_KEY)

# Function to generate restaurant name & menu items
def generate_restaurant_name_and_items(cuisine):
    # Step 1: Generate a fancy restaurant name
    restaurant_prompt = f"Suggest a fancy restaurant name for {cuisine} cuisine."
    restaurant_name = client.text_generation(restaurant_prompt, max_new_tokens=50).strip()

    # Step 2: Generate menu items using the restaurant name
    menu_prompt = f"Suggest some menu dishes for {cuisine} cuisine served at {restaurant_name}. Return them as a comma-separated string."
    menu_items = client.text_generation(menu_prompt, max_new_tokens=100).strip()

    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }
