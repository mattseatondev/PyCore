import datetime
from typing import List


users_db = {
    'matt': 'Matt',
    'maya': 'Maya',
    'ranger': 'Ranger',
    'molly': 'Molly',
    'bartholamew': 'Bart',
    'steven': 'Steve',
    'henrietta': 'Henrietta'
}

# Docstrings
def add_user(user_id:str, name:str) -> dict:
    """
    Adds a User to the Datastore
    
    Args:
        user_id (str): _description_
        name (str): _description_

    Returns:
        dict: _description_
        
    Raises:
        ValueError: If user is already in DB
    """
    if user_id in users_db:
        raise ValueError(f"User {user_id} already exists")
    users_db[user_id] = name
    return {'user_id': user_id, 'name': name}


print(add_user('river', 'River'))
# print(add_user('matt', 'Matt'))

# Schema in comments
def create_user(user_id:str, name:str) -> dict:
    """
    Create a user object.
    
    Schema: 
        {
            "user_id": "<str>",
            "name": "<str>",
            "created_at": "<datetime>"
        }
    """
    return {'user_id': user_id, 'name': name, 'created_at': datetime.datetime.now()}

print(create_user('schmidt', "Ol' Schmiddy"))

# WHY, not WHAT - e.g.:
# Assumes list is sroted; will fail silently if unsorted
# Increment counter to avoid overwriting previous index in merged list

# Perfect Example?
def binary_search(sorted_list: List[int], target:int) -> int:
    """
    Perform Binary Search on a sorted list

    Args:
        sorted_list (List[int]): A list of ints, **must be sorted in ascending order**
        target (int): The number for which the process will search

    Returns:
        int: Index of the target in the list
    
    Raises:
        ValueError: If target num is not found
        
    Notes:
        Time Complexity: O(log n)
        Space Complexity: O(1)
        Uses iterative approach to avoid recursion stack overflow
    """