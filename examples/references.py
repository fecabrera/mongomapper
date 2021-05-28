from mongomapper import Schema, Reference

class Person(Schema):
  __collection_name__ = 'people'

  name: str

class Phone(Schema):
  __collection_name__ = 'phones'

  owner: Reference(Person)

person = Person.create(name="John")
phone = Phone.create(owner=person)

print(person.data)
print(phone.data)