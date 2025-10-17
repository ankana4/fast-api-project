from pydantic import BaseModel

'''
Using pydantic for data validation
'''

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
    
