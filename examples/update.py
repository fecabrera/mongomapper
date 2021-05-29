from mongomapper import Schema

class User(Schema):
  __collection_name__ = 'users'

  name: str

doc = User.create(name="John")

print(doc.data)

doc.name = "Not John"
doc.save()

print(doc.data)