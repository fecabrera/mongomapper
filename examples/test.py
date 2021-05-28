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

person = Person.create(name="John", birthday="1990-01-01")
car = Car.create(plate="ABCD10", owner=person)

print(person.data)
print(car.data)