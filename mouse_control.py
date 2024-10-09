from panda3d.core import WindowProperties, Mat4

class MouseControl():
    def __init__(self, base):
        self.base = base

    def enable_mouse(self):
        mat = Mat4(self.base.camera.getMat())
        mat.invertInPlace()
        self.base.mouseInterfaceNode.setMat(mat)
        props = WindowProperties()
        props.setCursorHidden(False)
        self.base.win.requestProperties(props)
        self.base.enableMouse()
        
    def disable_mouse(self):
        props = WindowProperties()
        props.setCursorHidden(True)
        self.base.win.requestProperties(props)
        self.base.win.movePointer(0, self.base.win.getProperties().getXSize() // 2, self.base.win.getProperties().getYSize() // 2)
        self.base.disableMouse()
