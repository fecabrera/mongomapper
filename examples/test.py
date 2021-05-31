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
print(person_a.data)
print(person_a.json())

person_b = Person.create(name="Adam", birthday="1990-01-01")
print(person_b.data)
print(person_b.json())

car = Car.create(plate="ABCD10", owner=person_a)

print(car.data)
print(car.json())

car.owner = person_b.reference
car.save()

print(car.data)
print(car.json())