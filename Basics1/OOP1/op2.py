from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def get_role(self):
        pass

class MedCard(ABC):
    def __init__(self, card_number, patient_name):
        self.card_number = card_number
        self.patient_name = patient_name

    @abstractmethod
    def display_record(self):
        pass

class Patient(Person):
    def __init__(self, name, age, gender, patient_id, ailment):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.ailment = ailment

    def get_role(self):
        return "Patient"

    def appointment(self):
        print(f"{self.name} has an appointment.")


class Doctor(Person):
    def __init__(self, name, age, gender, specialty):
        super().__init__(name, age, gender)
        self.specialty = specialty

    def get_role(self):
        return "Doctor"

    def diagnose(self, diagnosis):
        print(f"Dr. {self.name} diagnoses {diagnosis}.")

class Nurse(Person):
    def __init__(self, name, age, gender, assignedDoctor):
        super().__init__(name, age, gender)
        self.assignedDoctor = assignedDoctor

    def get_role(self):
        return "Nurse"

    def help(self, assignedDoctor):
        print(f"Nurse {self.name} is helping Dr. {assignedDoctor}.")


