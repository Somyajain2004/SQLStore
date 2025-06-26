from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///store.db')
Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=False)
    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    category = relationship("Category", back_populates="products")


Base.metadata.create_all(engine)
print("Tables created\n")


Session = sessionmaker(bind=engine)
session = Session()

# Sample data
cat1 = Category(category_name="Electronics")
cat2 = Category(category_name="Clothing")

prod1 = Product(product_name="Laptop", price=75000.0, category=cat1)
prod2 = Product(product_name="Smartphone", price=25000.0, category=cat1)
prod3 = Product(product_name="Jeans", price=2000.0, category=cat2)
prod4 = Product(product_name="Shirt", price=800.0, category=cat2)

session.add_all([cat1, cat2, prod1, prod2, prod3, prod4])
session.commit()

# Query
products = session.query(Product).all()
for p in products:
    print(f"Product: {p.product_name}, Price: ₹{p.price}, Category: {p.category.category_name}")
