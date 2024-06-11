import numpy as np

# Como o sólido foi desenhado a mão, deixar os vértices indicados em ordem de desenho
class Spacecraft:
    def __init__(self):
        self.vertices = np.array([
            [0.0, 0.0, 1.0],  # Vértice 0
            [-1.0, -1.0, -1.0],  # Vértice 1
            [1.0, -1.0, -1.0],  # Vértice 2
            [0.0, 3.0, -1.0],  # Vértice 3
            [-2.0, -1.0, -1.0],  # Vértice 4
            [2.0, -1.0, -1.0],  # Vértice 5
        ], dtype=np.float32)

        self.indices = np.array([
            0, 1, 2,
            0, 1, 3,
            0, 2, 3,
            1, 2, 3,
            1, 4, 3,
            2, 5, 3
        ], dtype=np.uint32)

        self.edges = np.array([
            [0, 1], [1, 2], [2, 0],
            [0, 3], [1, 3], [2, 3],
            [1, 4], [4, 3],
            [2, 5], [5, 3]
        ], dtype=np.uint32)

        self.tex_coords = np.array([
            [0.5, 1.0],  # Vértice 0
            [0.0, 0.0],  # Vértice 1
            [1.0, 0.0],  # Vértice 2
            [0.5, 0.5],  # Vértice 3 (ponto superior)
            [0.0, 0.0],  # Vértice 4 (asa esquerda)
            [1.0, 0.0],  # Vértice 5 (asa direita)
        ], dtype=np.float32)

        self.position = np.array([0.0, 0.0, 0.0], dtype=np.float32)
        self.scale = np.array([1.0, 1.0, 1.0], dtype=np.float32)
        self.rotation = np.array([-90.0, 0.0, 0.0], dtype=np.float32)

    def translate(self, dx, dy, dz):
        self.position += np.array([dx, dy, dz], dtype=np.float32)

    def rotate(self, angle, axis):
        self.rotation += np.array(angle) * np.array(axis)

    def scale(self, sx, sy, sz):
        self.scale *= np.array([sx, sy, sz], dtype=np.float32)

class Ground:
    def __init__(self):
        self.vertices = np.array([
            [-40.0, -8.0, -40.0],
            [40.0, -8.0, -40.0],
            [40.0, -8.0, 40.0],
            [-40.0, -8.0, 40.0]
        ], dtype=np.float32)
        
        self.indices = np.array([
            0, 1, 2,
            2, 3, 0
        ], dtype=np.uint32)

        self.tex_coords = np.array([
            [0.0, 0.0],
        ])
