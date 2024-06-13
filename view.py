import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import glutInit, glutBitmapCharacter, GLUT_BITMAP_HELVETICA_18
from PIL import Image
import time

class View:
    def __init__(self, spacecraft, ground, spacecraft_texture_path, ground_texture_path):
        self.spacecraft = spacecraft
        self.ground = ground
        self.spacecraft_texture_path = spacecraft_texture_path
        self.ground_texture_path = ground_texture_path
        self.camera_position = [0.0, 2.0, 25.0]
        self.camera_target = [0.0, 0.0, 0.0]
        self.camera_up = [0.0, 1.0, 0.0]
        self.spacecraft_texture_id = None
        self.ground_texture_id = None
        self.ground_texture_offset = 0.0

    def load_texture(self, texture_path):
        image = Image.open(texture_path)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = image.convert("RGBA").tobytes()
        width, height = image.size

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        return texture_id

    def initialize(self):
        if not glfw.init():
            return
        self.window = glfw.create_window(1280, 720, "OpenGL Spacecraft", None, None)
        if not self.window:
            glfw.terminate()
            return
        glfw.make_context_current(self.window)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1280 / 720, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)

        glClearColor(0, 0.0, 0, 0.6)

        self.spacecraft_texture_id = self.load_texture(self.spacecraft_texture_path)
        self.ground_texture_id = self.load_texture(self.ground_texture_path)

        glutInit()

    def update_ground_texture_offset(self, delta_time):
        self.ground_texture_offset += delta_time * 0.01 # velocidade animação do chão

    def render_spacecraft(self):
        glBindTexture(GL_TEXTURE_2D, self.spacecraft_texture_id)
        glPushMatrix()
        glTranslatef(*self.spacecraft.position)
        glRotatef(self.spacecraft.rotation[0], 1.0, 0.0, 0.0)
        glRotatef(self.spacecraft.rotation[1], 0.0, 1.0, 0.0)
        glRotatef(self.spacecraft.rotation[2], 0.0, 0.0, 1.0)
        glScalef(*self.spacecraft.scale)

        glBegin(GL_TRIANGLES)
        for i in range(0, len(self.spacecraft.indices), 3):
            for j in range(3):
                glTexCoord2f(*self.spacecraft.tex_coords[self.spacecraft.indices[i + j]])
                vertex = self.spacecraft.vertices[self.spacecraft.indices[i + j]]
                glVertex3f(*vertex)
        glEnd()

        glLineWidth(4.0)
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_LINES)
        for edge in self.spacecraft.edges:
            for vertex in edge:
                glVertex3f(*self.spacecraft.vertices[vertex])
        glEnd()
        glColor3f(1.0, 1.0, 1.0)
        glPopMatrix()

    def render_ground(self):
        glBindTexture(GL_TEXTURE_2D, self.ground_texture_id)
        glPushMatrix()
        glBegin(GL_QUADS)
        for i, vertex in enumerate(self.ground.vertices):
            glTexCoord2f((i % 2) + self.ground_texture_offset, (i // 2) + self.ground_texture_offset)
            glVertex3f(*vertex)
        glEnd()
        glPopMatrix()

    def render_text(self, text, x, y):
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, 1280, 0, 720)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        glRasterPos2f(x, y)
        for char in text:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()

    def render_commands(self):
        commands = [
            "W, A, S, D: Move nave nos eixos (X,Y)",
            "Arrow Keys: Rotaciona a nave nos eixos (X,Y)",
            "Q, E: Rotaciona nave no eixo Z",
            "I, K: Move câmera cima/baixo",
            "J, L: Move câmera esquerda/direita",
            "U, O: Move câmera frente/trás",
            "=, -: Aumenta/diminui escala da nave",
            "N, M: Aumenta/diminui asa da nave",
            "V, B: Desce/sobe asa da nave",
        ]
        y = 700  
        for command in commands:
            self.render_text(command, 10, y)
            y -= 20 

    def render(self):
        current_time = time.time()
        if not hasattr(self, 'last_time'):
            self.last_time = current_time
        delta_time = current_time - self.last_time
        self.last_time = current_time

        self.update_ground_texture_offset(delta_time)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(
            self.camera_position[0], self.camera_position[1], self.camera_position[2],
            self.camera_target[0], self.camera_target[1], self.camera_target[2],
            self.camera_up[0], self.camera_up[1], self.camera_up[2]
        )

        self.render_ground()
        self.render_spacecraft()
        self.render_commands()

        glfw.swap_buffers(self.window)

    def should_close(self):
        return glfw.window_should_close(self.window)

    def terminate(self):
        glfw.terminate()
