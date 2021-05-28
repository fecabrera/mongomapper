from pymongo import MongoClient
from bson.objectid import ObjectId
from pydantic import BaseModel, PrivateAttr

from .utils import classproperty
from .config import config

client = MongoClient(f'mongodb+srv://{config.DB_USER}:{config.DB_PASS}@{config.DB_HOST}/{config.DB_NAME}?retryWrites=true&w=majority')
db = client.get_database(config.DB_NAME)

class BaseSchema(BaseModel):
  __collection_name__: str
  
  _id: ObjectId = PrivateAttr(default_factory=ObjectId)
  
  def __init__(self, **data):
    super().__init__(**data)
    
    if '_id' in data:
      self._id = data['_id']

  @property
  def data(self):
    return {'_id': self._id} | self.dict()
  
  @classproperty
  def collection(cls):
    return db.get_collection(cls.__collection_name__)
  
  @classmethod
  def get(cls, document_id):
    data = cls.collection.find_one({'_id': ObjectId(document_id)})
    doc = cls(**data)
    return doc

  @classmethod
  def create(cls, **data):
    doc = cls(**data)
    cls.collection.insert_one(doc.data)
    return doc