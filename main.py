from MyVector import MyVector
from VectorRepo import VectorRepository
import matplotlib.pyplot as plt
import numpy as np

def test():
    # Test MyVector class
    vector1 = MyVector("Vector1", "r", 3, [1.0, 2.0, 3.0])
    vector2 = MyVector("Vector2", "b", 2, [4.0, 5.0, 6.0])

    # Test add_scalar
    scalar = 5.0
    vector1.add_scalar(scalar)
    assert np.all(vector1.get_values() == np.array([6.0, 7.0, 8.0])),\
        "add_scalar test failed"

    # Test __add__ (vector addition)
    result_vector = vector1 + vector2
    assert np.all(result_vector.get_values() == np.array([10.0, 12.0, 14.0])), \
        "__add__ test failed"

    # Test subtract (vector subtraction)
    result_vector = vector1.subtract(vector2)
    assert np.all(result_vector.get_values() == np.array([2.0, 2.0, 2.0])), \
        "subtract test failed"

    # Test multiply (vector multiplication)
    scalar_product = vector1.multiply(vector2)
    assert scalar_product == 107.0, \
        "multiply test failed"

    # Test sum_elements
    assert vector1.sum_elements() == 21.0, \
        "sum_elements test failed"

    # Test product_elements
    assert vector1.product_elements() == 336.0, \
        "product_elements test failed"

    # Test average_elements
    assert vector1.average_elements() == 7.0, \
        "average_elements test failed"

    # Test min_element
    assert vector1.min_element() == 6.0, \
        "min_element test failed"

    # Test max_element
    assert vector1.max_element() == 8.0, \
        "max_element test failed"

    # Test VectorRepository class
    vector_repository = VectorRepository()
    vector_repository.add_vector(vector1)
    vector_repository.add_vector(vector2)

    # Test add_vector
    new_vector = MyVector("Vector3", "g", 1, [6.0, 7.0, 8.0])
    vector_repository.add_vector(new_vector)
    assert new_vector in vector_repository.get_all_vectors(), \
        "add_vector test failed"

    # Test get_sum_vector
    sum_vector = vector_repository.get_sum_vector()
    assert np.all(sum_vector.get_values() == np.array([16.0, 19.0, 22.0])), \
        "get_sum_vector test failed"

    # Test delete_vectors_by_product
    c = 50.0
    vector_repository.delete_vectors_by_product(c)
    assert all(vector.product_elements() <= c for vector in vector_repository.get_all_vectors()), \
        "delete_vectors_by_product test failed"

    # Test update_vectors_by_type
    target_type = 2
    new_color = "y"
    vector_repository.update_vectors_by_type(target_type, new_color)
    assert all(vector.color == new_color for vector in vector_repository.get_all_vectors() if vector.type_value == target_type), \
        "update_vectors_by_type test failed"


    print("All tests passed!")
test()
def validate_color(color):
    valid_colors = ['r', 'g', 'b', 'y', 'm']
    if color not in valid_colors:
        raise ValueError(f"Invalid color. Choose from {valid_colors}")

def print_menu():
    print("\nMENU:")
    print("1. Display Vectors")
    print("2. Add Vector")
    print("3. Get Sum Vector")
    print("4. Delete Vectors by Product")
    print("5. Update Vectors by Type")
    print("6. Get All Vectors")
    print("7. Get Vector at Index")
    print("8. Update Vector at Index")
    print("9. Update Vector by Name ID")
    print("10. Delete Vector by Index")
    print("11. Delete Vector by Name ID")
    print("12. Plot Vectors")
    print("0. Exit")

def main():
    vector_repository = VectorRepository()
    vectors = [
        MyVector("Vector1", "r", 3, [1.0, 2.0, 3.0]),
        MyVector("Vector2", "b", 2, [4.0, 3.0, 2.0]),
        MyVector("Vector3", "g", 1, [6.0, 7.0, 8.0]),
        MyVector("Vector4", "y", 4, [1.0, 4.0, 6.0]),
        MyVector("Vector5", "m", 2, [1.0, 3.0, 5.0]),
        MyVector("Vector6", "r", 1, [1.0, 5.0, 4.0]),
        MyVector("Vector7", "b", 2, [1.0, 6.0, 4.0]),
        MyVector("Vector8", "g", 3, [1.0, 1.0, 1.0]),
        MyVector("Vector9", "y", 1, [5.0, 5.0, 5.0]),
        MyVector("Vector10", "m", 2, [2.0, 4.0, 6.0]),
    ]
    for vector in vectors:
        vector_repository.add_vector(vector)

    while True:
        print_menu()
        choice = input("Enter your choice (0-12): ")

        if choice == "0":
            print("Exiting the program.")
            break
        elif choice == "1":
            vector_repository.display_vectors()
        elif choice == "2":
            try:
                name_id = input("Enter name_id: ")
                color = input("Enter color: ")
                type_value = int(input("Enter type_value: "))
                values = list(map(float, input("Enter values separated by spaces: ").split()))

                if type_value < 1:
                    raise ValueError("Type value must be a positive integer greater or equal to 1")
                validate_color(color)
                new_vector = MyVector(name_id, color, type_value, values)
                vector_repository.add_vector(new_vector)
                print("Vector added successfully.")
            except ValueError as e:
                print(f"Error: {e}. Please enter valid data.")
        elif choice == "3":
            sum_vector = vector_repository.get_sum_vector()
            print(f"Sum Vector: {sum_vector}")
        elif choice == "4":
            try:
                c = float(input("Enter the c value for deletion: "))
                vector_repository.delete_vectors_by_product(c)
                print("Vectors deleted successfully.")
            except ValueError:
                print("Error: Please enter a valid numerical value for 'c'.")
        elif choice == "5":
            try:
                target_type = int(input("Enter target type for update: "))
                new_color = input("Enter new color: ")
                vector_repository.update_vectors_by_type(target_type, new_color)
                print("Vectors updated successfully.")
            except ValueError:
                print("Error: Please enter a valid numerical value for 'target_type'.")
        elif choice == "6":
            all_vectors = vector_repository.get_all_vectors()
            print("\nAll Vectors:")
            for vector in all_vectors:
                print(vector)
        elif choice == "7":
            try:
                index = int(input("Enter index to get the vector: "))
                vector_at_index = vector_repository.get_vector_at_index(index)
                print(f"Vector at index {index}: {vector_at_index}")
            except ValueError:
                print("Error: Please enter a valid numerical value for 'index'.")
        elif choice == "8":
            try:
                index = int(input("Enter index to update the vector: "))
                new_name_id = input("Enter new name_id: ")
                new_color = input("Enter new color: ")
                new_type_value = int(input("Enter new type_value: "))
                new_values = list(map(float, input("Enter new values separated by spaces: ").split()))
                if new_type_value < 1:
                    raise ValueError("Type value must be a positive integer greater or equal to 1")
                validate_color(new_color)
                new_vector = MyVector(new_name_id, new_color, new_type_value, new_values)
                vector_repository.update_vector_at_index(index, new_vector)
                print("Vector updated successfully.")
            except ValueError as e:
                print(f"Error: {e}. Please enter valid data.")
        elif choice == "9":
                name_id = input("Enter name_id to update the vector: ")
                new_name_id = input("Enter new name_id: ")
                new_color = input("Enter new color: ")
                new_type_value =int(input("Enter new type_value, as an int: "))
                new_values = list(map(float, input("Enter new values separated by spaces, as int values: ").split()))
                if  new_type_value < 1:
                    raise ValueError("Type value must be a positive integer greater or equal to 1")
                if type(new_type_value)==type(" "):
                    print("enter another type value")
                validate_color(new_color)
                new_vector = MyVector(new_name_id, new_color, new_type_value, new_values)
                vector_repository.update_vector_by_name_id(name_id, new_vector)

        elif choice == "10":
            try:
                index = int(input("Enter index to delete the vector: "))
                vector_repository.delete_vector_by_index(index)
                print("Vector deleted successfully.")
            except ValueError:
                print("Error: Please enter a valid numerical value for 'index'.")
        elif choice == "11":
            name_id = input("Enter name_id to delete the vector: ")
            vector_repository.delete_vector_by_name_id(name_id)
            print("Vector deleted successfully.")
        elif choice == "12":
            vector_repository.plot_vectors()
        else:
            print("Invalid choice. Choose another number between 0 and 12.")

if __name__ == "__main__":
    main()
