from dotenv import load_dotenv
import os

load_dotenv()

HEADERS : dict = {
    "Authorization": f"Bearer {os.getenv('TOKEN')}",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "X-MAS": os.getenv('TOKEN')
}