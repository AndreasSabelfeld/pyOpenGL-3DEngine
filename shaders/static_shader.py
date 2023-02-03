from .shader_program import ShaderProgram
import sys


class StaticShader(ShaderProgram):
    __VERTEX_FILE = f"{sys.path[0]}/shaders/vertexShader.txt"
    __FRAGMENT_FILE = f"{sys.path[0]}/shaders/fragmentShader.txt"
    __location_transformation_matrix = 0

    def __init__(self):
        super().__init__(self.get_vertex_file(), self.get_fragment_file())

    def bind_attributes(self):
        super().bind_attribute(0, "position")
        super().bind_attribute(1, "texture_coords")

    def get_all_uniform_locations(self):
        self.set_location_transformation_matrix(super().get_uniform_location("transformation_matrix"))

    def load_transformation_matrix(self, matrix: list[list]):
        super().load_matrix(self.get_location_transformation_matrix(), matrix)

    @classmethod
    def get_vertex_file(cls):
        return cls.__VERTEX_FILE

    @classmethod
    def get_fragment_file(cls):
        return cls.__FRAGMENT_FILE

    @classmethod
    def set_location_transformation_matrix(cls, value):
        cls.__location_transformation_matrix = value

    @classmethod
    def get_location_transformation_matrix(cls):
        return cls.__location_transformation_matrix
