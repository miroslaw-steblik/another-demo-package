import pandas as pd

class ClassModule:
    def __init__(self):
        pass

    def read_csv(self, path):
        return pd.read_csv(path)
    
    def say_hello(self):
        print("Hello from another_package!")

    def say_bye(self, x):
        for i in range(x):
            print("Goodbye from another_package!")

    def say_hello(self):
        print("Hello from another_package!")

    def calculate(self, x, y):
        return x + y
    
    def data_frame(self, data):
        return pd.DataFrame(data)