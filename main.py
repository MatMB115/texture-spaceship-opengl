import glfw
from model import Spacecraft, Ground
from view import View
from controller import Controller

def main():
    spacecraft = Spacecraft()
    ground = Ground()
    spacecraft_texture_path = 'nave.png'  
    ground_texture_path = 'space.png'
    view = View(spacecraft, ground, spacecraft_texture_path, ground_texture_path)
    controller = Controller(spacecraft, view)

    view.initialize()

    while not view.should_close():
        controller.process_input()
        view.render()
        glfw.poll_events()

    view.terminate()

if __name__ == "__main__":
    main()
