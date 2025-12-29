from time import time
import requests

from chain.classes.block import Block
from chain.classes.chain import Chain
from client.wallet import Wallet
from common.helper_functions import pr
from keygen import gen_keypair

base_url = 'http://localhost:5000'
    
if __name__ == '__main__':
    chain = Chain()
    wallet = Wallet()
    verified = wallet.verify(base_url)
    print(verified)