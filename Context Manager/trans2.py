Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class ErrorKiller:
     def __init__(self, *errors):
         self.errors = errors
 
     def __enter__(self):
         print("Looking for errors.")
         return self
 
     def __exit__(self, exc_type, exc_val, exc_tb):
         if exc_type is None:
             print("All good.")
             return False
         print(f"There's an error: {exc_type.__name__}: {exc_val}")
         if exc_type in self.errors:
             print("Error suppressed successfully.")
             return True   
         print("Can't suppress this error.")
