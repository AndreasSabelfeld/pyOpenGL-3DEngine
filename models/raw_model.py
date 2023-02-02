
class RawModel:
    """
    This class creates a raw model object, which saves the ID of the vao and the vertex count
    """
    def __init__(self, vao_id: int, vertex_count: int):
        self.__vao_id = vao_id
        self.__vertex_count = vertex_count

    def get_vao_id(self):
        return self.__vao_id

    def get_vertex_count(self):
        return self.__vertex_count
