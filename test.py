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

person = Person.create(name="Felipe", birthday="1995-12-02")
car = Car.create(plate="ABCD10", owner=person)

print(person.reference)
print(car.reference)