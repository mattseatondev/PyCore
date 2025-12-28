import hashlib
from typing import Any

from common.types import HashStr

def compute_entity_hash(data:Any) -> HashStr:
    h_str = str(data).encode()
    return hashlib.sha256(h_str).hexdigest()

def validate_hash(against:HashStr, newData:Any) -> bool:
    return compute_entity_hash(newData) == against

