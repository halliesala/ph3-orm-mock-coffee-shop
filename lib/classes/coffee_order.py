from lib import CONN, CURSOR
from lib.classes.customer import Customer

class CoffeeOrder:

    # CLASS METHODS
    @classmethod
    def highest_price(cls):
        sql = """
        SELECT * FROM coffee_orders
        WHERE price = (SELECT MAX(price) FROM coffee_orders);
        """
        (id, coffee_name, price, customer_id) = CURSOR.execute(sql).fetchone()
        return CoffeeOrder(coffee_name, price, customer_id, id)

    @classmethod
    def average_price(cls):
        sql = """
        SELECT AVG(price)
        FROM coffee_orders;
        """
        (avg_price,) = CURSOR.execute(sql).fetchone()
        return avg_price

    # SQL CLASS METHODS #
    @classmethod
    def create_table(cls):
        sql="""CREATE TABLE IF NOT EXISTS coffee_orders (
        id INTEGER PRIMARY KEY,
        coffee_name COFFE_NAME,
        price INTEGER,
        customer_id NUMBER
        )
        """

        CURSOR.execute(sql) 
    
    @classmethod
    def query_all(cls):
        sql = "SELECT * FROM coffee_orders"
        coffee_orders = [CoffeeOrder(coffee_name, price, customer_id, id) 
                         for (id, coffee_name, price, customer_id) 
                         in CURSOR.execute(sql).fetchall()]
        return coffee_orders
    
    @classmethod
    def query_by_id(cls, id):
        sql = "SELECT * FROM coffee_orders WHERE id=?"
        (id, coffee_name, price, customer_id) = CURSOR.execute(sql, [id]).fetchone()
        return CoffeeOrder(coffee_name, price, customer_id, id)

    # INITIALIZERS AND PROPERTIES 

    def __init__(self, coffee_name, price, customer_id, id=None):
        self.coffee_name = coffee_name
        self.price = price
        self.customer_id = customer_id
        self.id = id

    def __repr__(self):
        return f"CoffeeOrder(id={self.id} coffee_name='{self.coffee_name}' price={self.price} customer_id={self.customer_id})"
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, val):
        if isinstance(val, int) and val > 0:
            self._price = val
        else:
            raise Exception("Price must be positive int")
        
    @property
    def customer(self):
        sql = "SELECT * FROM customers WHERE customers.id = ?"
        try:
            (id, name) = CURSOR.execute(sql, [self.customer_id]).fetchone()
        except:
            return None
        return Customer(name, id)
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            # associate CoffeeOrder with customer
            sql = """
            UPDATE coffee_orders
            SET customer_id = ?
            WHERE id = ?
            """
            CURSOR.execute(sql, [customer.id, self.id])
            CONN.commit()
        else:
            raise Exception("Can only set customer to object with class Customer")

        
    # SQL INSTANCE METHODS
    def create(self):
        sql = """INSERT INTO coffee_orders (coffee_name, price, customer_id) VALUES(?, ?, ?);"""
        CURSOR.execute(sql, [self.coffee_name, self.price, self.customer_id])
        CONN.commit()
        sql = "SELECT last_insert_rowid() FROM coffee_orders;"
        (self.id,) = CURSOR.execute(sql).fetchone()
        
    def delete(self):
        sql = """DELETE FROM coffee_orders WHERE id=?;"""
        CURSOR.execute(sql, [self.id])

    def update(self):
        sql = """
        UPDATE coffee_orders 
        SET coffee_name=?, price=?, customer_id=?
        WHERE id=?
        """
        CURSOR.execute(sql, [self.coffee_name, self.price, self.customer_id, self.id])
        CONN.commit()

    def save(self):
        if self.id:
            self.update()
        else:
            self.create()

    
