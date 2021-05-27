from typing import Optional
from .errors import DocumentNotFoundError

class Query:
  model:      ...
  filter:     dict
  projection: dict
  
  def __init__(self, model, filter: Optional[dict] = {}, projection: Optional[dict] = {}):
    self.model      = model
    self.filter     = filter
    self.projection = projection
  
  def where(self, **filter):
    self.filter = self.filter | filter
    return self
  
  def get(self, limit: int = 0, skip: int = 0):
    docs = self.model.collection.find(self.filter, self.projection or None, skip, limit)
    return [self.model(**doc) for doc in docs]
  
  def get_one(self):
    doc = self.model.collection.find_one(self.filter, self.projection or None)

    if doc is None:
      raise DocumentNotFoundError(model=self.model, filter=self.filter)

    return self.model(**doc)