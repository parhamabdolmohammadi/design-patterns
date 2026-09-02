"""
Interface is a contract that specifies the capabilities
that a class should provide 

if make sure that the structure of the child class dont change the 
contract therefore reducing recoupling and chance of recompilation
"""

from abc import ABC, abstractmethod


class TaxCalculator(ABC):

    @abstractmethod
    def calculate_tax(self) -> float:
        pass
