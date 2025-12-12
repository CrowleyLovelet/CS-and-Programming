from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def get_role(self):
        pass

class User(Person):
    def __init__(self, name, age, gender, nickname):
        super().__init__(name, age, gender)
        self.nickname = nickname

    def get_role(self):
        return "User"

    def call_out(self):
        print(f"{self.name} has this username '{self.nickname}'.")

class Admin(Person):
    def get_role(self):
        return "Admin"

    def call_out(self):
        print("This is an Admin account.")

class Emote(ABC):
    def __init__(self, nameE, typeof):
        self.nameE = nameE
        self.typeof = typeof

    @abstractmethod
    def get_type(self):
        pass

class Emoji(Emote):
    def __init__(self, nameE, typeof, emojipack):
        super().__init__(nameE, typeof)
        self.emojipack = emojipack

    def get_type(self):
        return "Emoji"

    def call_out(self):
        print(f"Name of emoji: {self.nameE}.")

    def what_type(self):
        print(f"This is {self.typeof} emoji.")

    def what_pack(self):
        print(f"This emoji is from {self.emojipack} pack.")

class Gif(Emote):
    def get_type(self):
        return "Gif"

    def call_out(self):
        print(f"Name of a gif: {self.nameE}.")

    def what_type(self):
        print(f"This is {self.typeof} gif.")

class Multimedia(ABC):
    def __init__(self, namem, typeof):
        self.namem = namem
        self.typeof = typeof

    @abstractmethod
    def get_type(self):
        pass

class Sound(Multimedia):
    def get_type(self):
        return "Audio"

    def call_out(self):
        print(f"Name of an audio file: {self.namem}.")

    def what_type(self):
        print("This is an audio file.")

class Videofile(Multimedia):
    def get_type(self):
        return "Video"

    def call_out(self):
        print(f"Name of a video file: {self.namem}.")

    def what_type(self):
        print("This is a video file.")

class Social(ABC):
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    @abstractmethod
    def get_type(self):
        pass

class Contact(Social):
    def get_type(self):
        return "Contact"

    def call_out(self):
        print(f"Name of a contact: {self.name}.")

    def what_phone(self):
        print(f"Number: {self.phone}")

    def what_email(self):
        print(f"Email: {self.email}")

class Friend(Social):
    def get_type(self):
        return "Friend"

    def call_out(self):
        print(f"Name of a friend: {self.name}.")

    def what_phone(self):
        print(f"Number: {self.phone}")

    def what_email(self):
        print(f"Email: {self.email}")

class Wallet(ABC):
    def __init__(self, name, typecard, balance):
        self.name = name
        self.typecard = typecard
        self.balance = balance

    @abstractmethod
    def get_type(self):
        pass

class Card(Wallet):
    def __init__(self, name, typecard, balance):
        super().__init__(name, typecard, balance)

    def get_type(self):
        return "Card"

    def call_out(self):
        print(f"Name of a card: {self.name}.")

    def what_card(self):
        print(f"It is a {self.typecard}.")

    def what_balance(self):
        print(f"Balance: {self.balance}")

class StoreCard(Wallet):
    def __init__(self, name, typecard, balance):
        super().__init__(name, typecard, balance)

    def get_type(self):
        return "StoreCard"

    def call_out(self):
        print(f"Name of a card: {self.name}.")

    def what_card(self):
        print(f"It is a {self.typecard}.")

    def what_balance(self):
        print(f"Balance: {self.balance}")


#-----aaaaaah---logiccccc-----this-is---how---it---might-----work-----

u = User("Bibizianka", 21, "F", "BibiziankaHuliganka")
a = Admin("BigBoss", 100, "M")

u.call_out()  
print("Role:", u.get_role())

a.call_out()  
print("Role:", a.get_role())


e = Emoji("Cry", "Sad", "SagePack")
g = Gif("DancingBibizianka", "Funny")

e.call_out()
e.what_type()
e.what_pack()

g.call_out()
g.what_type()

s = Sound("VokrugShum", "Rap")
v = Videofile("PiratskiFilm", "Comady")

s.call_out()
s.what_type()

v.call_out()
v.what_type()


c = Contact("Zuchara", "8989898989", "zuchara@gmail.com")
f = Friend("MamaBibizianka", "899999999", "mama@gmail.com")

c.call_out()
c.what_phone()
c.what_email()

f.call_out()
f.what_phone()
f.what_email()


card1 = Card("BlackCard", "Visa", 10)
store1 = StoreCard("GiftCard", "Steam", 10000000)

card1.call_out()
card1.what_card()
card1.what_balance()

store1.call_out()
store1.what_card()
store1.what_balance()

        
