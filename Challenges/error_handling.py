import asyncio

# Note "from e" here: This preserves the original traceback.
# Great for debugging
def process(value):
    try:
        return 10 / value
    except ZeroDivisionError as e:
        raise ValueError("Processing failed") from e

# Async error handling
# Note return_exceptions=True
async def fetch_value(x):
    if x == 0:
        raise ValueError('Zero not allowed')
    return 10 / x

async def main():
    tasks = [fetch_value(i) for i in [1, 2, 3, 4, 5, 0]]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for r in results:
        if isinstance(r, Exception):
            print(f'Error occurred: {r}')
        else:
            print(f"Result: {r}")

# Custom Exceptions
class DivisionError(Exception):
    pass

def divide(a, b):
    if b == 0:
        raise DivisionError('Attempted to divide by zero!')
    return a / b

if __name__ == '__main__':
    asyncio.run(main())