Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class GameStarter:
     def __init__(self, name: str):
         self.name = name
         self.game = None
 
     def __enter__(self):
         print(f"Starting game '{self.name}'")
         self.game = f"GameObject({self.game_name})"
        return self.game
 
     def __exit__(self, exc_type, exc_val, exc_tb):
         print(f"Error occurred: Stoping game '{self.game_name}'")
         self.game = None
        
