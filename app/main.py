from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_args = []
    saved_results = []

    def wrapper(*args: Any) -> Any:
       for i in range(len(saved_args)):
           if args == saved_args[i]:
               print("Getting from cache")
               return saved_results[i]

       result = func(*args)
       print("Calculating new result")
       saved_args.append(args)
       saved_results.append(result)
       return result

    return wrapper

@cache
def delay_addition(a, b):
    import time
    time.sleep(3)
    return a + b