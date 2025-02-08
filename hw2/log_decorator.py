import datetime
import functools

def function_logger(log_file):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            
            with open(log_file, "a") as f:
                f.write(f"{func.__name__}\n")
                f.write(f"{start_time.strftime('%Y-%m-%d %H:%M:%S.%f')}\n")
                
                if args:
                    f.write(f"{args}\n")
                if kwargs:
                    f.write(f"{kwargs}\n")
                    
                result = func(*args, **kwargs)
                
                end_time = datetime.datetime.now()
                duration = end_time - start_time
                
                if result is not None:
                    f.write(f"{result}\n")
                else:
                    f.write("-\n")
                    
                f.write(f"{end_time.strftime('%Y-%m-%d %H:%M:%S.%f')}\n")
                f.write(str(duration) + "\n")
            return result
        return wrapper
    return decorator