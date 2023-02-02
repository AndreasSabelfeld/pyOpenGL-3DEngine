from OpenGL.GL import *
from OpenGL.GLUT import *
from .loader import Loader


class DisplayManager:

    __window_id = 0

    def __init__(self, x: int = 1920, y: int = 1080):
        self.__width = x
        self.__height = y
        self.next_window_id()                                   # give this window a unique window id

    def create_display(self, window_name):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)                           # initialize colors
        glutInitWindowSize(self.get_width(), self.get_height())  # set windows size
        glutInitWindowPosition(0, 0)                             # set window position
        glutCreateWindow(f"{window_name}")                       # create window (with a name) and set window attribute
        glutSetWindow(self.get_window_id())
        glutDisplayFunc(self.update_display)
        glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_GLUTMAINLOOP_RETURNS)  # prevent program from stopping

    @staticmethod
    def update_display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Remove everything from screen (i.e. displays all white)
        glLoadIdentity()                                    # Reset all graphic/shape's position
        glutSwapBuffers()                                   # Important for double buffering

    def destroy_window(self):
        Loader.clean_up()
        glutDestroyWindow(self.get_window_id())

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    @classmethod
    def next_window_id(cls):
        cls.__window_id += 1

    def get_window_id(self):
        return self.__window_id
