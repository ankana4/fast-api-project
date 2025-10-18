from fastapi import FastAPI
from models import Product

app = FastAPI()

# @app.get("/")
# def greet():
#     return "Hello, World!"

products = [
    Product(id=1,  name="phone", description="budget phone",  price=99, quantity=10),
    Product(id=2, name="laptop", description="gaming laptop",  price=999, quantity=6),
    Product(id=3, name="tablet", description="android tablet",  price=199, quantity=15),
    Product(id=4, name="monitor", description="4k monitor",  price=299, quantity=8),
]    
    
@app.get("/products") 
def get_all_products():
    return  products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return "Product not found"    
    
@app.post("/product")
def add_product(product: Product):
    products.append(product)    
    return product

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)-1):
        if products[i].id == id:
            products[i] = product
            return "Product updated successfully"
    return "No product found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product is deleted"
    return "Product not found"        
    