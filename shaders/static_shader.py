from .shader_program import ShaderProgram
import sys


class StaticShader(ShaderProgram):
    __VERTEX_FILE = f"{sys.path[0]}/shaders/vertexShader.txt"
    __FRAGMENT_FILE = f"{sys.path[0]}/shaders/fragmentShader.txt"

    def __init__(self):
        super().__init__(self.get_vertex_file(), self.get_fragment_file())

    def bind_attributes(self):
        super().bind_attribute(0, "position")
        super().bind_attribute(1, "texture_coords")

    @classmethod
    def get_vertex_file(cls):
        return cls.__VERTEX_FILE

    @classmethod
    def get_fragment_file(cls):
        return cls.__FRAGMENT_FILE
