from OpenGL.GL import *
from models.textured_model import TexturedModel


class Renderer:
    """
    This Class is responsible for rendering every object on the screen
    """
    @staticmethod
    def prepare():
        glClearColor(1, 0, 0, 1)        # set backdrop color to red
        glClear(GL_COLOR_BUFFER_BIT)    # clear everything
        glEnable(GL_TEXTURE_2D)

    @staticmethod
    def render(model: TexturedModel):
        raw_model = model.get_raw_model()
        glBindVertexArray(raw_model.get_vao_id())                # bind the desired VAO to be able to use it
        glEnableVertexAttribArray(0)                             # we have put the indices in the 0th address
        glEnableVertexAttribArray(1)                             # we have put the textures in the 1st address
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, model.get_texture().get_id())
        glDrawElements(GL_TRIANGLES, raw_model.get_vertex_count(), GL_UNSIGNED_INT, None)
        glDisableVertexAttribArray(0)                            # disable the attributeList after using it
        glDisableVertexAttribArray(1)                            # disable the attributeList after using it
        glBindVertexArray(0)                                     # unbind the VAO
