from pycgtypes import vec3, mat4
import math


class Maths:
    """
    Class for computing all the needed maths
    """
    @staticmethod
    def create_transformation_matrix(translation: list[float], rx: float, ry: float, rz: float, scale: float):
        matrix = mat4(1.0)
        matrix = matrix.translate(vec3(translation))              # apply translation (position changes)
        if rx > 0: matrix = matrix.rotate(math.radians(rx), vec3(rx, ry, rz))   # apply rotation along the x-axis
        if ry > 0: matrix = matrix.rotate(math.radians(ry), vec3(rx, ry, rz))   # apply rotation along the y-axis
        if rz > 0: matrix = matrix.rotate(math.radians(rz), vec3(rx, ry, rz))   # apply rotation along the z-axis
        matrix = matrix.scale(vec3(scale, scale, scale))          # apply scaling
        return list(matrix)                                       # list so OpenGL can use the values
