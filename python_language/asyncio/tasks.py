"""
A task is a wrapper of a coroutine that schedules the coroutine to run on the event loop as soon as possible.
The scheduling and execution occur in a non-blocking manner.
In other words, you can create a task and execute other code instantly while the task is running.


We can create a task using the asyncio. ensure_future() function.
"""