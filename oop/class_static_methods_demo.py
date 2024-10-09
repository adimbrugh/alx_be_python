

#Calculator Class
class Calculator:

    #class Attribute
    calculation_type = "Arithmetic Operations"

    #static method
    @staticmethod
    def add(a, b):
        return a + b 
    
    #class method
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b