# Phase 3 ORM Mock Challenge - Coffee Shop

For this mock challenge, we'll be working with a domain for a coffee shop.

We have two models: `CoffeeOrder` which shows the coffee orders which belong to a `Customer`.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- lists and list Methods
- SQL queries
- ORM methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Only one of the tables, `customers` has been created so far. Additionally the `Customer`
class already has its required functionality and you won't have to build
additional methods for it.

Build out all of the methods listed in the deliverables for `CoffeeOrder`. The methods are listed in a suggested order, but you can feel free to tackle the ones you think
are easiest. Be careful: some of the later methods rely on earlier ones.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects. There are no formal tests to run with this code so be
sure to test it in the `debug.py` often.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

- `CoffeeOrder classmethod create_table()`
  - Creates a `coffee_orders` table with these columns: id (INTEGER), coffee_name (TEXT),
  price (INTEGER), customer_id (INTEGER)
- `CoffeeOrder __init__(coffee_name, price, customer_id, id=None)`
  - `CoffeeOrder` is initialized with a coffee_name (string) and an price (integer)
  - When initialized an CoffeeOrder should have an id of None
  - Assume that CoffeeOrders will always be initialized with the proper data types
- `CoffeeOrder __repr__()`
  - Returns the CoffeeOrder instance in the format below:
  - `CoffeeOrder(id={id} coffee_name={coffee_name}, price={price}, customer_id={customer_id})`
- `CoffeeOrder property price()`
  - Returns the `CoffeeOrder`'s price
  - The price must be an integer ADD CONSTRAINTS

### SQL Methods

- `CoffeeOrder create()`
  - Creates a CoffeeOrder in the database with the instance's attributes
- `CoffeeOrder update()`
  - Updates a CoffeeOrder in the database based on the instance's attributes
- `CoffeeOrder save()`
  - Will either create or update the CoffeeOrder in the database depending on whether the CoffeeOrder has an id
- `CoffeeOrder delete()`
  - Deletes the CoffeeOrder from the database
  - No return value is necessary for this method
- `CoffeeOrder classmethod query_all()`
  - Returns a list of CoffeeOrder instances based on rows in the database
  - The return value ought to be a list of CoffeeOrder instances

### Association Properties

- `CoffeeOrder property customer()`
  - Returns the C2 that the CoffeeOrder is associated with as an instance
  - If the CoffeeOrder is not associated with a C2 returns `None`
  - When setting the customer, if the argument is a `C2` instance it associates the
  CoffeeOrder with the customer
  - The database is already seeded with a pair of customers for testing purposes
    - C2(id=1, name=???)
    - C2(id=2, name=???)

TODO: Seed database

### BONUS Methods

- `CoffeeOrder classmethod query_max_or_min()`
  - Returns the max CoffeeOrder by price from the database as an instance
- `CoffeeOrder classmethod average()`
  - Returns the average price of coffee orders in the database
