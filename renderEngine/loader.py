from OpenGL.GL import *
from OpenGL.GLUT import *
from PIL import Image
import numpy
import sys
from .raw_model import RawModel


class Loader:
    """
    This class creates and keeps track of all VAOs and VBOs and is responsible for binding them
    """
    __vaos = []
    __vbos = []
    __textures = []

    def load_to_vao(self, positions: list[float], texture_coords: list[float], indices: list[int]):
        vao_id = self.create_vao()               # creates VAO
        self.bind_indices_buffer(indices)        # every vertex is given an index for the order
        self.store_data_in_attribute_list(0, 3, positions)       # binds the positions into the 0th place in the VAO
        self.store_data_in_attribute_list(1, 2, texture_coords)  # binds the texture coords into 1st place in the VAO
        self.unbind_vao()                                 # unbinds the vao
        return RawModel(vao_id, len(indices))             # returns raw model object

    @classmethod
    def load_texture(cls, file_name: str):
        try:
            img = Image.open(f"{sys.path[0]}/res/{file_name}.png")
            img = img.transpose(Image.FLIP_TOP_BOTTOM)              # flip image upside down
        except Exception as e:
            print(e)
            raise SystemExit
        try:
            ix, iy, image = img.size[0], img.size[1], img.tobytes("raw", "RGBA", 0, -1)
        except SystemError:
            ix, iy, image = img.size[0], img.size[1], img.tobytes("raw", "RGBX", 0, -1)
        texture_id = glGenTextures(1)             # generate a texture ID
        cls.__textures.append(texture_id)
        glBindTexture(GL_TEXTURE_2D, texture_id)  # make it current
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        # copy the texture into the current texture texture_id
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        return texture_id

    @classmethod
    def clean_up(cls):
        for vao in cls.__vaos:
            glDeleteVertexArrays(1, [vao])
        for vbo in cls.__vbos:
            glDeleteBuffers(1, [vbo])
        for texture in cls.__textures:
            glDeleteTextures(1, [texture])

    @classmethod
    def create_vao(cls):
        vao_id = glGenVertexArrays(1)   # creates 1 vertex array
        cls.__vaos.append(vao_id)       # appends it to the VAO list in the class
        glBindVertexArray(vao_id)       # binds the VAO to use it
        return vao_id

    @classmethod
    def store_data_in_attribute_list(cls, attribute_number: int, coordinate_size: int, data: list[float]):
        data = numpy.array(data, dtype='float32')   # convert the data into a float32 array
        vbo_id = glGenBuffers(1)                    # create 1 VBO buffer
        cls.__vbos.append(vbo_id)                   # appends it to the VBO list in the class
        glBindBuffer(GL_ARRAY_BUFFER, vbo_id)       # binds the buffer to use it
        glBufferData(GL_ARRAY_BUFFER, data, GL_STATIC_DRAW)  # specifies the buffer, data and usage
        glVertexAttribPointer(attribute_number, coordinate_size, GL_FLOAT, False, 0, None)  # put the VBO into a VAO
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    @staticmethod
    def unbind_vao():
        glBindVertexArray(0)

    @classmethod
    def bind_indices_buffer(cls, indices: list[int]):
        indices = numpy.array(indices, dtype=numpy.uint32)  # convert the data into an unsigned integer array
        vbo_id = glGenBuffers(1)
        cls.__vbos.append(vbo_id)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vbo_id)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices, GL_STATIC_DRAW)
