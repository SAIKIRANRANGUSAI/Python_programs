"""
print one after another after execution one then the next line will print(inter-link with each other)
we can create one thread at a time
one after other taks will done
its decides which task should starts
"""

import asyncio

async def fetch_data(data: int)->dict:
    print("fecting data..:")
    await asyncio.sleep(3)
    return {'data':data}

async def counter():
    for i in range(10):
        await asyncio.sleep(0.5)  #sleeping for 0.5 seconds
        
        print(i)
async def main():
    await counter()
    await fetch_data(2)
asyncio.run(main())