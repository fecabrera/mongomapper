from .utils import classproperty

from .base import BaseSchema
from .reference import Reference
from .query import Query

class Schema(BaseSchema):
  @property
  def reference(self):
    return Reference(self.__class__)(self._id)
  
  @classproperty
  def query(self):
    return Query(model=self)