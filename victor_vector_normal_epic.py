import math
# victor_vector normal mode for W2D2
# does math...yay


class ShapeError(BaseException):
    pass


class Vector:

    # only write code to pass the TESTS
    # init method, passes vector coordinates as a list
    def __init__(self, *args):
        vector = []
        self.vector = [vector.append(value) for key, value in enumerate(args)]

    def __str__(self):
        return "[{v}]".format(v=self.vector)

    def __eq__(self, other):
        return self.vector == other.vector

    # helper function to compare equality of args
    def shape_eq(self, *args):
        bool_list = [len(arg) == len(args[0]) for arg in args]
        if min(bool_list) != True:
            raise ShapeError
        else:
            return True

    # makes the vector shape
    def shape(self):
        return (len(self.vector))


    # adds vectors
    def __add__(self, *args):
        if shape_eq(self.vector, *args):
            total = [a + b for a, b in zip(self.vector, *args)]
            return total


    # subtracts vectors
    def __sub__(self, *args):
        if shape_eq(self.vector, *args):
            difference = [a - b for a, b in zip(self.vector, *args)]
            return difference


    # sums any number of vectors
    # i hate this solution because it can't handle whatever the user sends
    # it seems piecemeal because it just passes the test but doesn't function
    def vector_sum(self, *args):
        if shape_eq(self.vector, *args):
            return [sum(i) for i in zip(self.vector, *args)]


    # dot multiplies vectors
    def dot(self, *args):
        if shape_eq(self.vector, *args):
            dot_prod = sum([x * y for x, y in zip(self.vector, *args)])
            return dot_prod


    # multiply vectors
    def vector_multiply(self, n):
        mult_vect = [self.vector[key]*n for key, value in enumerate(self.vector)]
        return mult_vect


    # finds mean value for vectors
    def vector_mean(self, *args):
        if shape_eq(self.vector, *args):
            return [sum(i) / len(i) for i in zip(self.vector, *args)]


    # calculates magnitude
    def magnitude(self):
        return math.sqrt(sum([float(self.vector[i])**2 for i in range(len(self.vector))]))
