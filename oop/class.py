#/usr/bin/python3

# declare new class
class employee:
    # 'pass' allows to ignore
    # pass
    
    # constructor - init 
    # functions in classes receive the object 
    # instance automatically as a parameter self
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # class function to print name
    def print_name(self):
        # return '{} {}'.format(self.first_name, self.last_name);
        return self.first_name + ' ' + self.last_name

# declare and instantiate new object
# pass default arguments to constructor
empl_1 = employee('Harry','Potter')

# invoke class function with object reference
print(empl_1.print_name())


