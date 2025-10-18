from fastapi import FastAPI, Depends
from models import Product
from config import SessionLocal, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()
database_models.Base.metadata.create_all(bind=engine)

# @app.get("/")
# def greet():
#     return "Hello, World!"

products = [
    Product(id=1,  name="phone", description="budget phone",  price=99, quantity=10),
    Product(id=2, name="laptop", description="gaming laptop",  price=999, quantity=6),
    Product(id=3, name="tablet", description="android tablet",  price=199, quantity=15),
    Product(id=4, name="monitor", description="4k monitor",  price=299, quantity=8),
]  


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:    
        db.close()
    
def init_db():
    db = SessionLocal()
    count = db.query(database_models.Product).count
    if count ==0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))    
        db.commit()     
        
init_db()        
    
@app.get("/products") 
def get_all_products(db: Session = Depends(get_db)):
    
    products_from_db = db.query(database_models.Product).all()
    return  products_from_db

@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return "Product not found"    
    
@app.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/product")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product is updated"
    else:
        return "No product found"

@app.delete("/product")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product is deleted"
    return "Product not found"        
    