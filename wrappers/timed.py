import logging
import time
from typing import Callable


def timed(logger: logging.Logger = None) -> Callable:
    """Times the duration of a function and logs it to a file. Will accept a log instance as a
    parameter, or it will create a new log file using the wrapped method as a log file name.

    Args:
        logger (logging.Logger): Logger instance used by the wrapper function
    Returns:
        function: Decorator function
    """

    def log_time_decorator(wrapped_function: Callable):
        def wrapper(*args, **kwargs) -> None:
            log = logger
            if log is None:
                # Output the timing result to a file with the name of the function
                log = logging.getLogger(wrapped_function.__name__)

            start_time = time.perf_counter()
            wrapped_function(*args, **kwargs)
            elapsed_time = time.perf_counter() - start_time
            log.info(f"[+] Completed in {elapsed_time:.3f} seconds")

        return wrapper

    return log_time_decorator
