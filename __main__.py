from OpenGL.GLUT import *
from renderEngine.display_manager import DisplayManager
from renderEngine.renderer import Renderer
from renderEngine.loader import Loader
from shaders.static_shader import StaticShader
from textures.model_texture import ModelTexture
from models.textured_model import TexturedModel
from entities.entity import Entity


def main():
    vertices = [
        -0.5, 0.5, 0,   # V0
        -0.5, -0.5, 0,  # V1
        0.5, -0.5, 0,   # V2
        0.5, 0.5, 0,    # V3
    ]

    indices = [
        0, 1, 3,        # Top left triangle (V0, V1, V3)
        3, 1, 2         # Bottom right triangle (V3, V1, V2)
    ]

    texture_coords = [
        0, 0,   # V0
        0, 1,   # V1
        1, 1,   # V2
        1, 0    # V3
    ]

    display = DisplayManager(1280, 720)
    display.create_display("test")  # creates display

    loader = Loader()
    model = loader.load_to_vao(vertices, texture_coords, indices)
    texture = ModelTexture(loader.load_texture("grass"))
    static_model = TexturedModel(model, texture)

    entity = Entity(static_model, [-1, 0, 0], 0, 0, 0, 1)

    renderer = Renderer()

    shader = StaticShader()

    while glutGetWindow() != 0:
        # game logic
        entity.increase_position(0.0002, 0, 0)
        entity.increase_rotation(0, 0.1, 0)
        display.update_display()
        shader.start()            # start the shader
        renderer.render(entity, shader)    # render everything
        shader.stop()             # stop the shader once finished rendering
        glutSwapBuffers()         # needs to be called AFTER finished drawing
        glutMainLoopEvent()       # used to run openGL manually in a loop instead of glutMainLoop()


if __name__ == '__main__':
    main()
