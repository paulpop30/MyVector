# MyVector

A math teacher needs a program that helps students perform different vector operations.
1).
A vector (class 𝑴𝒚𝑽𝒆𝒄𝒕𝒐𝒓) is identified by the following properties:

• 𝑛𝑎𝑚𝑒_𝑖𝑑 given as a string/int

• 𝑐𝑜𝑙𝑜𝑢𝑟 given as one letter (possible values ‘r’, ‘g’, ‘b’, ‘y’ and ‘m’)

• 𝑡𝑦𝑝𝑒 given as a positive integer greater or equal to 1

• 𝑣𝑎𝑙𝑢𝑒𝑠 given as a list of numbers

The following features are offered by the program (to be implemented in class MyVector)

1st Iteration:

1. Scalar operations:

a. Add a scalar to a vector – 𝑎𝑑𝑑_𝑠𝑐𝑎𝑙𝑎𝑟
e.g. [1,2,3] + 2 = [3,4,5]

2. Vector operations:

a. Add two vectors – 𝑎𝑑𝑑
e.g. [1,2,3] + [4,5,6] = [5,7,9]

b. Subtract two vectors – subtract
e.g. [1,2,3] - [4,5,5] = [-3,-3,-2]

c. Multiplication – 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑐𝑎𝑡𝑖𝑜𝑛
e.g. [1,2,3] * [4,5,5] = 29

3. Reduction operations

a. Sum of elements in a vector
e.g. for [1,2,3] sum is 6

b. Product of elements in a vector
e.g. for [1,2,3] product is 6

c. Average of elements in a vector
e.g. for [1,2,3] average is 2

d. Minimum of a vector
e.g. for [1,-2,3] minimum is -2
e. Maximum of a vector
e.g. for [1,2,-3] maximum is 2

2nd. Iteration

The program manages several vectors (class 𝑽𝒆𝒄𝒕𝒐𝒓𝑹𝒆𝒑𝒐𝒔𝒊𝒕𝒐𝒓𝒚) and allows
operations such as:

1. Add a vector to the repository

2. Get all vectors

3. Get a vector at a given index

4. Update a vector at a given index

5. Update a vector identified by 𝑛𝑎𝑚𝑒_𝑖𝑑

6. Delete a vector by index

7. Delete a vector by 𝑛𝑎𝑚𝑒_𝑖𝑑

8. Plot all vectors in a chart based on the 𝑡𝑦𝑝𝑒 and 𝑐𝑜𝑙𝑜𝑢𝑟 of each vector (using library matplotlib). Type should be interpreted as follows: 1 – circle, 2 – square,3 – triangle, any other value – diamond. (No tests needed for this function)

3rd. Iteration

Implement all features from iteration 1 using special libraries e.g. numpy
