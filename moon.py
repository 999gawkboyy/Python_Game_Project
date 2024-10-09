import complexpbr
from panda3d.core import PointLight, Vec3, Vec4

class Moon:
    def __init__(self, base):
        self.base = base

    def show(self, x: int, y: int, z: int, scale:int | None = 1):
        self.space = self.base.loader.load_model("./assets/space/scene.bam")
        self.space.reparent_to(self.base.render)
        self.space.set_pos(x, y, z)
        self.space.set_scale(scale)