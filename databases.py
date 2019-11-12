from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, picturelink,  description):
   
    product_object = Product(
    name=name,
    price=price,
    picturelink= picturelink,
    description= description)
    session.add(product_object)
    session.commit()


add_product("Mayuri", 2, True)

def update_product_status(name,  price, picturelink,  description):
  
   product_object = session.query(
       Product).filter_by(
       name=name).first()
   product_object.price = price
   session.commit()


update_product_status("Emily", True)

def delete_product(their_price):
  
   session.query(Product).filter_by(
      price=price ).delete()
   session.commit()


delete_product("Mayuri")

def query_all():
   
   products = session.query(
      Product).all()
   return products

print(query_all())


def query_by_name(their_name):

   product = session.query(
       Product).filter_by(
       name=name).first()
   return product


print(query_by_name("Mayuri"))


def add_to_cart(product_id):

	cart_object = Cart(
	product_id=product_id
	session.add(cart_object)
	session.commit()

add_to_cart()






