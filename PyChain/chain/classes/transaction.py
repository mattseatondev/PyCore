from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Literal
from time import time

from common.types import GeneratedKey

class TransactionBase(BaseModel):
    tms: float=Field(default_factory=time)
    type: str # TBDiscriminated later???
    
class StakeTransaction(TransactionBase):
    type: Literal['stake'] = 'stake'
    user_pubkey: GeneratedKey
    usdc_amt: Decimal
    tgt_amt: Decimal
    
class P2PTransaction(TransactionBase):
    type: Literal['p2p'] = 'p2p'
    sender_pubkey: GeneratedKey
    recipient_pubkey: GeneratedKey
    tgt_amt: Decimal