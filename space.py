import complexpbr
from panda3d.core import PointLight, Vec3, Vec4

class Space:
    def __init__(self, base):
        self.base = base

    def show(self, x: int, y: int, z: int, scale:int | None = 1):
        env_light_1 = PointLight('env_light_1')
        env_light_1.set_color(Vec4(Vec3(6),1))
        env_light_1 = self.base.render.attach_new_node(env_light_1)
        env_light_1.set_pos(0, 0, 0)

        self.space = self.base.loader.load_model("./assets/space/space.bam")
        self.space.reparent_to(self.base.render)
        self.space.set_pos(x, y, z)
        self.space.set_scale(scale)
        self.space.set_light(env_light_1)