# Phase 3 ORM Challenge - NAME GOES HERE

For this mock challenge, we'll be working with a domain for a c2.

We have two models: `C1` which shows the c1s who belong to a `C2`.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- lists and list Methods
- SQL queries
- ORM methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Only one of the tables, `c2s` has been created so far. Additionally the `C2`
class already has its required functionality and you won't have to build
additional methods for it.

Build out all of the methods listed in the deliverables for `C1`. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

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

- `C1 classmethod create_table()`
  - Creates an `c1s` table with these columns: id (INTEGER), field_one (TEXT),
  field_two (INTEGER), c2_id (INTEGER)
- `C1 __init__(field_one, field_two, c2_id, id=None)`
  - `C1` is initialized with a field_one (string) and an field_two (integer)
  - When initialized an C1 should have an id of None
  - Assume that C1s will always be initialized with the proper data types
- `C1 __repr__()`
  - Returns the C1 instance in the format below:
  - `C1(id={id} field_one={field_one}, field_two={field_two}, c2_id={c2_id})`
- `C1 property field_two()`
  - Returns the `C1`'s field_two
  - The field_two must be an integer ADD CONSTRAINTS

### SQL Methods

- `C1 create()`
  - Creates a C1 in the database with the instance's attributes
- `C1 update()`
  - Updates a C1 in the database based on the instance's attributes
- `C1 save()`
  - Will either create or update the C1 in the database depending on whether the C1 has an id
- `C1 delete()`
  - Deletes the C1 from the database
  - No return value is necessary for this method
- `C1 classmethod query_all()`
  - Returns a list of C1 instances based on rows in the database
  - The return value ought to be a list of C1 instances

### Association Properties

- `C1 property c2()`
  - Returns the C2 that the C1 is associated with as an instance
  - If the C1 is not associated with a C2 returns `None`
  - When setting the c2, if the argument is a `C2` instance it associates the
  C1 with the c2
  - The database is already seeded with a pair of c2s for testing purposes
    - C2(id=1, name=???)
    - C2(id=2, name=???)

TODO: Seed database

### BONUS Methods

- `C1 classmethod query_max_or_min()`
  - Returns the max C1 by field_two from the database as an instance
- `C1 classmethod average()`
  - Returns the average field_two of c1s in the database
