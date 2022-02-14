import time
from typing import Callable,Any

def timer(func:Callable) -> Callable:
    """ Checking code changes with timer """
    time.sleep(3)
    return func

@timer
def chec_web_site() -> Any:
    print("Checking code changes")

for _ in range(5):
    chec_web_site()

