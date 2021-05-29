from mongomapper import Schema, Reference
from datetime import date

class Person(Schema):
  __collection_name__ = 'people'
  
  name: str
  birthday: date

class Car(Schema):
  __collection_name__ = 'cars'

  plate: str
  owner: Reference(Person)

person_a = Person.create(name="John", birthday="1990-01-01")
person_b = Person.create(name="Adam", birthday="1990-01-01")

car = Car.create(plate="ABCD10", owner=person_a)

print(car.data)

car.owner = person_b.reference
car.save()

print(car.data)