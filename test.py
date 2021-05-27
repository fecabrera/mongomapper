from mongomapper import Schema, Reference

class Person(Schema):
  __collection_name__ = 'people'
  
  name: str

class Car(Schema):
  __collection_name__ = 'cars'

  plate: str
  owner: Reference(Person)

person = Person.create(name="Felipe")
car = Car.create(plate="ABCD10", owner=person)

print(person.reference)
print(car.reference)