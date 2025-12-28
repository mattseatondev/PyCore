from pydantic import BaseModel, constr
from typing import Annotated

hash_regex = r"^[0-9a-fA-F]{64}$"
wallet_key_regex = r"^0x[a-fA-F0-9]{40}$"

# creates a custom HashStr type, validated by regex
# Annotated = pydantic knows HashStr is a str with constraint
HashStr = Annotated[str, constr(pattern=hash_regex, min_length=64, max_length=64)]

GeneratedKey = Annotated[str, constr(pattern=wallet_key_regex, min_length=42, max_length=42)]