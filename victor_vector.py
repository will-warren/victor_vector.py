import math
# victor_vector normal mode for W2D2
# does math...yay


class ShapeError(BaseException):
    pass


# helper function to compare equality of args
def shape_eq(*args):
    bool_list = [len(arg) == len(args[0]) for arg in args]
    if min(bool_list) != True:
        raise ShapeError
    else:
        return True

# only write code to pass the TESTS
# def __init__(vector):
#     self.x = vector[0]
#     self.y = vector[1]

# makes the vector shape
def shape(v):
    return (len(v),)


# adds vectors
def vector_add(v1, v2):
    if shape_eq(v1, v2):
        return [v1[key] + v2[key] for key, value in enumerate(v1)]


# subtracts vectors
def vector_sub(v1, v2):
    if shape_eq(v1, v2):
        return [v1[key] - v2[key] for key, value in enumerate(v1)]


# sums any number of vectors
# i hate this solution because it can't handle whatever the user sends
# it seems piecemeal because it just passes the test but doesn't function
def vector_sum(*args):
    if shape_eq(*args):
        return [sum(i) for i in zip(*args)]


# dot multiplies vectors
def dot(v1, v2):
    if shape_eq(v1, v2):
        dot_prod = sum([x * y for x, y in zip(v1, v2)])
        return dot_prod


# multiply vectors
def vector_multiply(v1, n):
    mult_vect = [v1[key]*n for key, value in enumerate(v1)]
    return mult_vect


# finds mean value for vectors
def vector_mean(*args):
    if shape_eq(*args):
        return [sum(i) / len(i) for i in zip(*args)]


# calculates magnitude
def magnitude(vect):
    return math.sqrt(sum([vect[i]**2 for i in range(len(vect))]))
