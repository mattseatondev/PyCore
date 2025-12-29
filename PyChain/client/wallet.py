from decimal import Decimal
from pydantic import BaseModel, Field, PrivateAttr
from typing import Optional
from eth_keys.datatypes import PrivateKey, PublicKey
import requests

from common.types import GeneratedKey
from keygen import gen_keypair

class Wallet(BaseModel):
    address: GeneratedKey|None=None
    _private_key: PrivateKey = PrivateAttr()
    _public_key: PublicKey = PrivateAttr()
    usdc_balance: Decimal=Field(default=Decimal("0.00"))
    tgt_balance: Decimal=Field(default=Decimal("0.00"))
    
    def __init__(self, **data):
        super().__init__(**data)
        if not hasattr(self, 'private_key') or not hasattr(self, 'public_key'):
            address, private_key, public_key = gen_keypair()
            self.address = address
            self._private_key = private_key
            self._public_key = public_key
            
    def challenge(self, url):
        nonce = requests.post(f'{url}/auth/challenge', json={'address': self.address})
        challenge = nonce.json()['challenge']
        return challenge.encode('utf-8')
    
    def sign(self, msg_bytes:bytes) -> str:
        return self._private_key.sign_msg(msg_bytes).to_hex()
    
    def verify(self, url:str) -> str:
        msg_bytes = self.challenge(url)
        signed = self.sign(msg_bytes)
        token = requests.post(
            f'{url}/auth/verify',
            json={
                'address': self.address,
                'signature': signed
            }
        )
        return token.json()