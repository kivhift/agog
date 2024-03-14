from abc import ABC, abstractmethod

class Agent(ABC):
    @abstractmethod
    def select_move(self, state):
        pass
