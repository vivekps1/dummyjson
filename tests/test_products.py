import os 
import requests  

from endpoints import Endpoints
from dotenv import load_dotenv 

load_dotenv() 

URL = os.getenv("BASE_URL", "")

def test_get_all_products():  
    get_all_products = URL+ Endpoints.fetch_all_products 
    print(get_all_products)
    response = requests.get(get_all_products) 
    assert response.status_code == 200

