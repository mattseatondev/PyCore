# import asyncio
# import random
# import pytest

# def add(a, b):
#     return a + b

# def divide(a, b):
#     if b == 0:
#         raise ValueError('No division by zero!')
#     return a / b

# def test_add():
#     assert add(2, 3) == 5
#     assert add(-1, 1) == 0
    
# def test_divide():
#     assert divide(10, 2) == 5
    
# def test_div_by_zero():
#     with pytest.raises(ValueError):
#         divide(10, 0)
        
# test_div_by_zero()
        
# # Testing async code
# async def fetch_data(name:str):
#     await asyncio.sleep(random.uniform(0.1, 0.3))
#     return f'{name} data'

# async def test_fetch_data():
#     res = await fetch_data('api1')
#     assert 'api1' in res
    
# # Fixtures
# @pytest.fixture
# async def async_sample():
#     await asyncio.sleep(0.1)
#     return [1, 2, 3]

# @pytest.mark.asyncio
# async def test_async_fixture(async_sample):
#     assert sum(async_sample) == 6
    
# # Paramatrizing
# @pytest.mark.parametrize('a, b, expected', [
# 	(1, 2, 3),
# 	(5, 5, 10),
# 	(10, -5, 5)
# ])
# def test_param(a, b, expected):
# 	assert a + b == expected
 
 
# # Exception Testing
# def test_divide_by_zero():
#     with pytest.raises(ZeroDivisionError):
#         divide(1, 0)
# # Or with async
# async def test_async_error():
#     async def fail():
#         await asyncio.sleep(0.1)
#         raise ValueError('shit...')
#     with pytest.raises(ValueError):
#         await fail()