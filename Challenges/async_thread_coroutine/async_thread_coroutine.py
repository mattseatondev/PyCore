# You have a list of users.
# For each user, you want to:
# Fetch their profile info (simulate I/O-bound network call)
# Compute a score based on some data (CPU-bound)
# You’ll practice:
# Async for I/O-bound profile fetches
# Threads for CPU-bound scoring
# Optional: background task to log status

import os
from pydantic import BaseModel, Field
import random
import asyncio

import json
        
# For API Emulation

class User(BaseModel):
    user_id:str
    name:str
    age:int
    
    def thread_score():
        return

def shuffle_list(list):
    return random.shuffle(list)

def interval(min=0.5, max=2):
    return random.uniform(min, max)

async def server_thinking_bg(msg):
    try:
        print('Server started thinking...')
        while True:
            await asyncio.sleep(0.5)
            print(msg)    
    except asyncio.CancelledError:
        print('Server stopped thinking.')

def scan_users():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, 'users.json')
    with open(json_path, 'r') as f:
        return json.load(f)
    
users = scan_users()
    
async def scan_one(search_prop:str, search_val:str|int) -> User|None:
    think_task = asyncio.create_task(server_thinking_bg(f'Attempting to Fetch item from DB: {search_prop}: {search_val}'))
    wait_interval = random.uniform(0.5, 1.5)
    user = next((user for user in users if user[search_prop] == search_val), None)
    await asyncio.sleep(wait_interval)
    if user is None:
        return None
    return User(**user)

# Challenge Code
    
async def fetch_one_user(user_id:str) -> User|None:
    db_user = await scan_one('user_id', user_id)
    return db_user

async def score_users():
    users = scan_users()
    user1 = await fetch_one_user('u008')
    print(user1)
    
if __name__ == '__main__':
    asyncio.run(score_users())