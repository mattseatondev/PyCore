import os
from eth_keys.datatypes import PrivateKey
from eth_utils.crypto import keccak

def gen_keypair() -> tuple:
    private_key = PrivateKey(os.urandom(32))
    public_key = private_key.public_key
    address_bytes = keccak(public_key.to_bytes())[12:]
    address = '0x' + address_bytes.hex()
    
    return address, private_key, public_key