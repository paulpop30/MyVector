import numpy as np

class MyVector:
    def __init__(self, name_id, color, type_value, values):
        self.name_id = str(name_id)
        self.color = color
        self.type_value = int(type_value)
        self.values = np.array(values, dtype=float)
    #getters
    def get_name_id(self):
        return self.name_id

    def get_color(self):
        return self._color

    def get_type_value(self):
        return self._type_value

    def get_values(self):
        return self._values.copy()

    def get_values(self):
        return self.values.copy()
#setters
    def set_name_id(self, name_id):
        self._name_id = str(name_id)

    def set_color(self, color):
        self._color = color

    def set_type_value(self, type_value):
        self._type_value = int(type_value)

    def set_values(self, values):
        self._values = np.array(values, dtype=float)

    def __str__(self):
        return f"MyVector(name_id={self.name_id}, color={self.color}, type_value={self.type_value}, values={self.values.tolist()})"
    def add_scalar(self, scalar):          #this function add a scalar given to each elements of a vector
        self.values += scalar                  #input:scalar- the scalr given
                                               #output:nothing....

    def __add__(self, other):                                                          #this function add two vectors
        if len(self.values) != len(other.values):                                       #input:other - the second vector
            raise ValueError("Vectors must have the same length for addition.")          #output: the sum of the vectors represented in a vector
        result_values = self.values + other.values
        return MyVector(f"{self.name_id}_add_{other.name_id}", self.color, self.type_value, result_values)

    def subtract(self, other):                                                              #this function substract two vectors
        if len(self.values) != len(other.values):                                                   #input:other- the vector which is substracted from the first one
            raise ValueError("Vectors must have the same length for subtraction.")                  #output: a vector resulted after substarct the vectors
        result_values = self.values - other.values
        return MyVector(f"{self.name_id}_subtract_{other.name_id}", self.color, self.type_value, result_values)

    def multiply(self, other):                                                        #this function multiply two vectors
        if len(self.values) != len(other.values):                                         #input:other - the second vector
            raise ValueError("Vectors must have the same length for multiplication.")     #output:result_value- the value resulted after multiplying
        result_value = np.sum(self.values * other.values)
        return result_value

    def sum_elements(self):               #this function get the sum of all the elements of a vector
        return np.sum(self.values)              #input:nothing...
                                                #output: the sum of the elements of the vector

    def product_elements(self):           #this function get the product of the elements of a vector
        return np.prod(self.values)         #input:nothing.....
                                            #output:the product obtained

    def average_elements(self):         #this function get the average of all the elements of a vector
        return np.mean(self.values)      #input:nothing...
                                         #output: the value of the average

    def min_element(self):             #this function get the minimum element of a vector
        return np.min(self.values)         #input:nothing
                                           #output: the minimum value

    def max_element(self):               #this function get the maximum element of a vector
        return np.max(self.values)          #input:nothing
                                            # output: the maximum value

# Example usage:
vector1 = MyVector("Vector1", "r", 3, [1.0, 2.0, 3.0])
print(vector1)
vector1_1 = MyVector("Vector1", "r", 3, [1.0, 2.0, 3.0])
print(vector1_1)
vector2 = MyVector("Vector2", "b", 2, [4.0, 5.0, 6.0])
print(vector2)

vector3 = MyVector("Vector3", "g", 1, [6.0,-6.0,-3.0,0])
print(vector3)

scalar = 11.75
vector1.add_scalar(scalar)
print(f"Vector after adding scalar {scalar}:", vector1)

vector4 = vector1_1 + vector2
print(f"Vector addition: {vector4}")

vector5 = vector1_1.subtract(vector2)
print(f"Vector subtraction: {vector5}")

scalar_product = vector1_1.multiply(vector2)
print(f"Vector multiplication: {scalar_product}")

print(f"Sum of elements: {vector1_1.sum_elements()}")
print(f"Product of elements: {vector1_1.product_elements()}")
print(f"Average of elements: {vector1_1.average_elements()}")
print(f"Minimum element: {vector3.min_element()}")
print(f"Maximum element: {vector3.max_element()}")
