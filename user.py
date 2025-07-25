from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,username, role):
        self.username = username
        self._role = role
        
    @ abstractmethod
    def display_dashboard(self):
        pass