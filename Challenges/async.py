import asyncio
import random
import json

def pr(data):
    if isinstance(data, list) or isinstance(data, dict):
        print(json.dumps(data, indent=2))
    else:
        print(data)

async def bg_log():
    try:
        while True:
            await asyncio.sleep(.5)
            print('status: Working...')
    except asyncio.CancelledError:
        print('Background logger cancelled')

async def fetch_data(name:str) -> str:
    interval = random.uniform(.5, 5)
    await asyncio.sleep(interval)
    return f'Waited {interval}s for {name} to respond'
    
async def main():
    
    apis = [f'api_{x + 1}' for x in range(3)]
    logger = asyncio.create_task(bg_log())
    # Explicitly create tasks so we can use them as task objects
    # Allows methods like task.done(), task.cancelled(), etc.
    # Also allows background tasks alongside other async logic
    # Allows tasks to run independently of current await! < THIS IS IMPORTANT
    # Also allows better exception handling
    # Suboptimal: fetch_tasks = [fetch_data(api) for api in apis]
    # OPTIMAL:
    fetch_tasks = [asyncio.create_task(fetch_data(api)) for api in apis]
    # * is a SPLAT operator
    # It expands an iterable into separate positional arguments
    # So asyncio.gather([task1, task2, task3]) [INVALID] becomes asyncio.gather(task1, task2, task3) [VALID]
    task_responses = await asyncio.gather(*fetch_tasks)
    results_dict = dict(zip(apis, task_responses))
    if task_responses:
        logger.cancel()
    pr(results_dict)
    return results_dict
    
if __name__ == '__main__':
    asyncio.run(main())