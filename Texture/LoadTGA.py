# encoding: utf-8


from OpenGL.GL import *
from OpenGL.GLU import *
import glfw
import time
from CTargaImage import CTargaImage

m_tga = CTargaImage()   
m_tga_un = CTargaImage()

def MouseHandler(button, state):
    if(button == glfw.MOUSE_BUTTON_RIGHT):
        exit(0)


def KeyboardHandler(key, state):
    if(state == glfw.GLFW_PRESS):
        if(key == 'S'):
            pass

def WindowCLose():
    exit(0)


def Reshape(width, height):
    if(height == 0):
        height = 1
    
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width - 1.0, 0.0, height - 1.0, -1.0, 1.0);
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
def Render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()
    
    global m_tga, m_tga_un
    glRasterPos2i(250, 400)
    glDrawPixels(m_tga.m_width, m_tga.m_height, GL_RGB, GL_UNSIGNED_BYTE, m_tga.m_imageData)
    
    glRasterPos2i(250, 100)
    glDrawPixels(m_tga_un.m_width, m_tga_un.m_height, GL_RGB, GL_UNSIGNED_BYTE, m_tga_un.m_imageData)

def init():
    width = 1024
    height = 768
    glfw.Init()
    glfw.OpenWindow(width, height, 8, 8, 8, 0, 24, 0, glfw.WINDOW)
    glfw.SetWindowTitle("glfw line")
    glfw.SetWindowSizeCallback(Reshape)
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL);
    
    glfw.SetMouseButtonCallback(MouseHandler)
    glfw.SetKeyCallback(KeyboardHandler)
    glfw.SetWindowCloseCallback(WindowCLose)
    
    global m_tga
    m_tga.load("rock.tga")
    m_tga_un.load("opengl_logo_un.tga")

init()
while(True):
    Render()
    glfw.SwapBuffers()
    if( glfw.GetKey(glfw.KEY_ESC) == glfw.GLFW_PRESS ):
        break
    time.sleep(0.01)

glfw.Terminate()

