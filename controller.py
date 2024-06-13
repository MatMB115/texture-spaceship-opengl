import glfw
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def process_input(self):
        # Nave
        if glfw.get_key(self.view.window, glfw.KEY_W) == glfw.PRESS:
            self.model.translate(0, 0.1, 0)
        if glfw.get_key(self.view.window, glfw.KEY_S) == glfw.PRESS:
            self.model.translate(0, -0.1, 0)
        if glfw.get_key(self.view.window, glfw.KEY_A) == glfw.PRESS:
            self.model.translate(-0.1, 0, 0)
        if glfw.get_key(self.view.window, glfw.KEY_D) == glfw.PRESS:
            self.model.translate(0.1, 0, 0)
        if glfw.get_key(self.view.window, glfw.KEY_UP) == glfw.PRESS:
            self.model.rotate(-2, [1, 0, 0])
        if glfw.get_key(self.view.window, glfw.KEY_DOWN) == glfw.PRESS:
            self.model.rotate(2, [1, 0, 0])
        if glfw.get_key(self.view.window, glfw.KEY_LEFT) == glfw.PRESS:
            self.model.rotate(-2, [0, 1, 0])
        if glfw.get_key(self.view.window, glfw.KEY_RIGHT) == glfw.PRESS:
            self.model.rotate(2, [0, 1, 0])
        if glfw.get_key(self.view.window, glfw.KEY_Q) == glfw.PRESS:
            self.model.rotate(-2, [0, 0, 1])
        if glfw.get_key(self.view.window, glfw.KEY_E) == glfw.PRESS:
            self.model.rotate(2, [0, 0, 1])
        # Camêra
        if glfw.get_key(self.view.window, glfw.KEY_I) == glfw.PRESS:
            self.view.camera_position[1] += 0.1  
        if glfw.get_key(self.view.window, glfw.KEY_K) == glfw.PRESS:
            self.view.camera_position[1] -= 0.1  
        if glfw.get_key(self.view.window, glfw.KEY_J) == glfw.PRESS:
            self.view.camera_position[0] -= 0.1  
        if glfw.get_key(self.view.window, glfw.KEY_L) == glfw.PRESS:
            self.view.camera_position[0] += 0.1 
        if glfw.get_key(self.view.window, glfw.KEY_U) == glfw.PRESS:
            self.view.camera_position[2] -= 0.1  
        if glfw.get_key(self.view.window, glfw.KEY_O) == glfw.PRESS:
            self.view.camera_position[2] += 0.1  
        if glfw.get_key(self.view.window, glfw.KEY_EQUAL) == glfw.PRESS:  
            self.model.scale[0] += 0.1  
            self.model.scale[1] += 0.1  
            self.model.scale[2] += 0.1  
        if glfw.get_key(self.view.window, glfw.KEY_MINUS) == glfw.PRESS:  
            self.model.scale[0] = max(0.1, self.model.scale[0] - 0.1)  
            self.model.scale[1] = max(0.1, self.model.scale[1] - 0.1)  
            self.model.scale[2] = max(0.1, self.model.scale[2] - 0.1)
        # Asa
        if glfw.get_key(self.view.window, glfw.KEY_N) == glfw.PRESS:
            if self.model.vertices[4][0] <= -2 and self.model.vertices[5][0] >= 2:
                self.model.vertices[4][0] += 0.1
                self.model.vertices[5][0] -= 0.1
            else:
                self.model.vertices[4][0] -= 0.1
                self.model.vertices[5][0] += 0.1
        if glfw.get_key(self.view.window, glfw.KEY_M) == glfw.PRESS:
            self.model.vertices[4][0] -= 0.1
            self.model.vertices[5][0] += 0.1
        if glfw.get_key(self.view.window, glfw.KEY_V) == glfw.PRESS:
            self.model.vertices[4][0] -= 0.001
            self.model.vertices[5][0] += 0.001
            self.model.vertices[4][2] -= 0.01
            self.model.vertices[5][2] -= 0.01
        if glfw.get_key(self.view.window, glfw.KEY_B) == glfw.PRESS:
            self.model.vertices[4][0] += 0.001
            self.model.vertices[5][0] -= 0.001
            self.model.vertices[4][2] += 0.01
            self.model.vertices[5][2] += 0.01

