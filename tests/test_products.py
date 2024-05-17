import os 
import requests  
import jsonschema 
import json
import pytest

from endpoints import Endpoints
from dotenv import load_dotenv 

load_dotenv() 


URL = os.getenv("BASE_URL", "") 

def get_schema_directory(file_name): 
    file_path = os.path.join(os.getcwd(), "json_files", file_name)  
    with open(file_path, "r") as file:  
        # print(file)
        json_file = json.load(file)   
    return json_file


@pytest.mark.positive
def test_get_all_products():  

    """Send a GET request to the `/products` endpoint and verify that the response status code is 200
    and the response body contains the expected structure and content, such as a list of products with
    the necessary fields (e.g., `id`)"""

    get_all_products = URL+ Endpoints.fetch_all_products 
    response = requests.get(get_all_products) 
    assert response.status_code == 200 

    schema = get_schema_directory("get_products.json")   
    jsonschema.validate(response.json(), schema)  

@pytest.mark.negative
def test_passing_query_params_get_products():  
    """Send a non-required parameter which does not affect the response of the endpoint"""
    get_all_products = URL+ Endpoints.fetch_all_products 
    params = {"key": "value"}
    response = requests.get(get_all_products, params= params)  
    assert response.status_code == 200 

    schema = get_schema_directory("get_products.json")   
    jsonschema.validate(response.json(), schema)  


@pytest.mark.positive
def test_get_a_single_product():  
    """
    Send a GET request to the `/products/{id}` endpoint with a valid product ID and verify that the response status code is 200 
    validate that the response body contains the correct product details, matching the specified ID.
    """

    id = 1
    get_single_product = URL+ Endpoints.fetch_product.format(id)
    response = requests.get(get_single_product) 
    print(get_single_product)
    assert response.status_code == 200 

    schema = get_schema_directory("get_single_product.json")   
    jsonschema.validate(response.json(), schema)  

@pytest.mark.negative
def test_invalid_product_id():  
    """
    Send a GET request to the `/products/{id}` endpoint with an invalid or non-existent product ID and verify that the response status code is 404
    """


    get_single_product = URL+ Endpoints.fetch_product.format('test')
    response = requests.get(get_single_product) 
    print(get_single_product)
    assert response.status_code == 404  


@pytest.mark.positive
def test_add_a_new_product():  

    """
     Send a POST request to the `/products/add` endpoint with valid product data and verify that the response status code is 200 
     and confirm that it has been correctly added to the database.
    """

    add_a_product_url = URL+ Endpoints.add_new_product
    request_body = get_schema_directory("request_a_new_product.json")
    headers = {'Content-Type': 'application/json'}

    response = requests.post(add_a_product_url,headers=headers, data=json.dumps(request_body))  
    product_id = response.json()["id"]
    assert response.status_code == 200 

    assert response.json()["id"] == product_id 
    assert response.json()["title"] == request_body["title"]  


@pytest.mark.negative
def test_no_data():  

    """
    Send a POST request to the `/products/add` endpoint with incomplete or invalid product data  and verify that the response status code is 400.

    """

    add_a_product_url = URL+ Endpoints.add_new_product
    headers = {'Content-Type': 'application/json'}
    request_body = 1

    response = requests.post(add_a_product_url,headers=headers, data = json.dumps(request_body))  

    assert response.status_code == 400 



@pytest.mark.positive
def test_update_a_product():  

    """
    Send a PUT request to the `/products/{id}` endpoint with valid update data for an existing product and verify that the response status code is 200 
    and confirm that the product details have been correctly updated in the database.

    """
    id = 1
    update_a_product_url = URL+ Endpoints.fetch_product.format(id)
    request_body = get_schema_directory("request_a_new_product.json") 
    request_body["title"] = "This is for testing purpose only"
    new_title = request_body["title"]
    print(request_body)
    headers = {'Content-Type': 'application/json'}

    response = requests.put(update_a_product_url,headers=headers, data=json.dumps(request_body))  
    product_id = response.json()["id"]
    print(product_id)

    assert response.status_code == 200 
    assert response.json()["id"] == product_id 
    assert response.json()["title"] == new_title 

@pytest.mark.negative
def test_update_invalid_product_id():  

    """
    Send a PUT request to the `/products/{id}` endpoint with an invalid or non-existent product ID and verify that the response status code is 404.
    """

    id = 101
    update_a_product_url = URL+ Endpoints.fetch_product.format(id)
    headers = {'Content-Type': 'application/json'}
    request_body = get_schema_directory("request_a_new_product.json")

    response = requests.put(update_a_product_url,headers=headers, data = json.dumps(request_body))  

    assert response.status_code == 404 

@pytest.mark.positive
def test_delete_a_product():  

    """
    Send a DELETE request to the `/products/{id}` endpoint with a valid product ID and verify that the response status code is 200 
    and retrieve the product using a GET request to confirm that it has been correctly deleted from the database.
    """

    id = 1
    delete_a_product_url = URL+ Endpoints.fetch_product.format(id)
    

    response = requests.delete(delete_a_product_url)  
    product_id = response.json()["id"]
    print(product_id)

    assert response.status_code == 200 
    assert response.json()["id"] == product_id 

@pytest.mark.negative
def test_delete_invalid_product():  

    """
    Send a DELETE request to the `/products/{id}` endpoint with an invalid or non-existent product ID and verify that the response status code is 404.
    """

    id = 101
    delete_a_product_url = URL+ Endpoints.fetch_product.format(id)

    response = requests.delete(delete_a_product_url)
    assert response.status_code == 404 

    
     


