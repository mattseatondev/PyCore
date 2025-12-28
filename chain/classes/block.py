from pydantic import BaseModel, Field
from typing import Any, Optional
from time import time
import json

from chain.util.hashing import compute_entity_hash
from common.types import HashStr

class Block(BaseModel):
    index: int
    tms: Optional[float]=Field(default_factory=time)
    data: Any # TODO: Add custom type for data
    prev_hash: HashStr
    hash: HashStr=Field(default="", repr=False)
    
    class Config:
        frozen = True
        
    def __init__(self, **data):
        super().__init__(**data)
        if not self.hash:
            object.__setattr__(self, 'hash', compute_entity_hash(self.model_dump(exclude={"hash"})))
            
    @property
    def model(self) -> dict:
        return self.model_dump()