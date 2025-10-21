class SampleClass:

    def some_function():
        print("This is a function in the oop.py file.")

    def __init__(self, variable1="Initial Value", variable2=100):
        self.variable1 = variable1
        self.variable2 = variable2
    

    def some_function(self, a):
        return a + self.variable2
    
    def another_function(self):
        print("This is another function in the oop.py file.")




def some_function():
    print("This is a function in the oop.py file.")