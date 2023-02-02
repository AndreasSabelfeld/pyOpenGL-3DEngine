from OpenGL.GL import *
from OpenGL.GLUT import *
from abc import abstractmethod  # for abstract methods


class ShaderProgram:
    """
    Class for loading and linking all shaders to the program.
    """
    def __init__(self, vertex_file: str, fragment_file: str):
        self.__vertex_shader_id = self.load_shader(vertex_file, GL_VERTEX_SHADER)
        self.__fragment_shader_id = self.load_shader(fragment_file, GL_FRAGMENT_SHADER)
        self.__program_id = glCreateProgram()                           # create program
        glAttachShader(self.__program_id, self.__vertex_shader_id)      # attach the shader to the program
        glAttachShader(self.__program_id, self.__fragment_shader_id)    # attach the shader to the program
        self.bind_attributes()
        glLinkProgram(self.__program_id)                                # link the program to the shaders
        glValidateProgram(self.__program_id)                            # validate the program

    def start(self):
        glUseProgram(self.get_program_id())

    @staticmethod
    def stop():
        glUseProgram(0)

    def clean_up(self):
        self.stop()
        glDetachShader(self.get_program_id(), self.get_vertex_shader_id())
        glDetachShader(self.get_program_id(), self.get_fragment_shader_id())
        glDeleteShader(self.get_vertex_shader_id())
        glDeleteShader(self.get_fragment_shader_id())
        glDeleteProgram(self.get_program_id())

    @abstractmethod
    def bind_attributes(self):
        pass

    def bind_attribute(self, attribute: int, variable_name: str):
        glBindAttribLocation(self.get_program_id(), attribute, variable_name)

    @staticmethod
    def load_shader(file: str, shader_type: int):
        try:
            shader_file = open(file, 'r')                      # read file
            shader_source = ''.join(shader_file.readlines())   # create a continuous string
        except Exception as e:
            print(e)                                        # print exception
            raise SystemExit
        shader_id = glCreateShader(shader_type)             # create the shader
        glShaderSource(shader_id, shader_source)            # load the shader source code
        glCompileShader(shader_id)                          # compile the shader
        if glGetShaderiv(shader_id, GL_COMPILE_STATUS) == GL_FALSE:
            print(glGetShaderInfoLog(shader_id))       # print the info log if it didn't compile correctly
            print("Could not compile shader.")
            raise SystemExit
        return shader_id

    def get_program_id(self):
        return self.__program_id

    def get_vertex_shader_id(self):
        return self.__vertex_shader_id

    def get_fragment_shader_id(self):
        return self.__fragment_shader_id
