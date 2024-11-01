from MyVector import MyVector
import matplotlib.pyplot as plt
class VectorRepository:
    def __init__(self):     #in this function i initialize the repository using the list VECTORS=[] being empty
        self.vectors = []
    def add_vector(self, vector):     # this is a function which add a vector to repository
        self.vectors.append(vector)    #input:an object of type my vector
                                       # output:nothing
    def display_vectors(self):
        for idx, vector in enumerate(self.vectors, start=1):        #this function display all the vectors
            print(f"Vector {idx}: {vector}")                            #input:nothing...
                                                                        #output:the list of all the vectors
    def get_sum_vector(self):                     # this function get the sum of all the vectors from the repository
        if not self.vectors:                          #input:nothing
            return None                               #output: sum_vector which represent a vector obtained by add all the vectors
        sum_vector_values = self.vectors[0].values
        for vector in self.vectors[1:]:
            sum_vector_values = [x + y for x, y in zip(sum_vector_values, vector.values)]
        sum_vector = MyVector("SumVector", "sum_color", 0, sum_vector_values)  # Replace with appropriate values
        return sum_vector
    def delete_vectors_by_product(self, c):                                                            #this function delete all the vectors which have the product of elements bigger than a value given
        self.vectors = [vector for vector in self.vectors if vector.product_elements() <= c]                #input: the value given - c
                                                                                                            #output:nothing
    def update_vectors_by_type(self, target_type, new_color):                    #this function update the color of the vectors wich have type_value equal with a target_type given , with a new color given
        for vector in self.vectors:                                                 #input:target_type- the type_value it is search for updating the vectors
            if vector.type_value == target_type:                                           # new_color-the new color given
                vector.color = new_color                                            #output:nothing
    def get_all_vectors(self):                #this function get all the vectors
        return self.vectors                    # input: nothing
                                               #output:the list with the vectors
    def get_vector_at_index(self, index):      #this function get a vector which is situated on a index equal to a given index
        if 0 <= index < len(self.vectors):         #input:index-the index given
            return self.vectors[index]             #output: the vector situate at the index given
        else:
            return None
    def update_vector_at_index(self, index, new_vector):       #this function update a vector at a given index
        if 0 <= index < len(self.vectors):                         #input:index - the index given
            self.vectors[index] = new_vector                              # new_vector- the new vector after obtained by updating the selected one
                                                                    #output:nothing....
    def update_vector_by_name_id(self, name_id, new_vector):     #this function update a vector wich have the name same as a name given
        for i, vector in enumerate(self.vectors):                      #input:name_id-the name given
            if (vector.name_id) == (name_id) or str(vector.name_id)==str(name_id):# new_vector- the new obtained vector
                 self.vectors[i] = new_vector                           #output:nothing......
        if (vector.name_id) != (name_id) or str(vector.name_id) != str(name_id):
            print("the name given is not in the list of vectors,try something else:")

    def delete_vector_by_index(self, index):                    #this function delete a vector at a given index
        if 0 <= index < len(self.vectors):                          #input: index- the index given
            del self.vectors[index]                                 #output:nothing....
    def delete_vector_by_name_id(self, name_id):                                                       #this function delete a vector which have the name same as a given name
        self.vectors = [vector for vector in self.vectors if vector.get_name_id() != name_id]              #input:name_id:the name given
                                                                                                           #output:nothing....
    def plot_vectors(self):                       # this function plot all the vectors in a chart based on type and color of each vector
        symbols = {1: 'o', 2: 's', 3: '^'}           #input, output:nothing
        for vector in self.vectors:
            x = vector.type_value
            y = vector.color
            plt.scatter(x, y, marker=symbols.get(vector.type_value, 'D'), label=vector.name_id)
        plt.xlabel('Type')
        plt.ylabel('Color')
        plt.show()

