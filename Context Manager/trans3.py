Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class CacheManager:
     cache = {}
 
     def __enter__(self):
         print("Cache of this manager:", CacheManager.cache)
         return CacheManager.cache
 
     def __exit__(self, exc_type, exc_val, exc_tb):
         print("Saving cache of this manager:", CacheManager.cache)
         return False
     
 def multiply(a, b):
     print(f"{a} * {b}")
     return a * b
 
 with CacheManager() as cache:
     if "product" not in cache:
         cache["product"] = multiply(3, 7)
     print("First manager value:", cache["product"])
 
 with CacheManager() as cache:
