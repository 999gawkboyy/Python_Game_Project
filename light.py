from panda3d.core import PointLight, Spotlight, AmbientLight, PerspectiveLens
from panda3d.core import LPoint3f, Point3, Vec3, Vec4, LVecBase3f, VBase4, LPoint2f

def light() -> None:
    amb_light = AmbientLight('amblight')
    amb_light.set_color(Vec4(Vec3(1),1))
    amb_light_node = base.render.attach_new_node(amb_light)
    base.render.set_light(amb_light_node)

    slight_1 = Spotlight('slight_1')
    slight_1.set_color(Vec4(Vec3(5),1))
    slight_1.set_shadow_caster(True, 4096, 4096)
    lens = PerspectiveLens()
    slight_1.set_lens(lens)
    slight_1.get_lens().set_fov(120)
    slight_1_node = base.render.attach_new_node(slight_1)
    slight_1_node.set_pos(50, 50, 90)
    slight_1_node.look_at(0,0,0.5)
    base.render.set_light(slight_1_node)

    slight_2 = Spotlight('slight_2')
    slight_2.set_color(Vec4(Vec3(5),1))
    slight_2.set_attenuation((0.5,0,0.0005))
    lens = PerspectiveLens()
    slight_2.set_lens(lens)
    slight_2.get_lens().set_fov(90)
    slight_2_node = base.render.attach_new_node(slight_2)
    slight_2_node.set_pos(-82, -79, 50)
    slight_2_node.look_at(0,0,0.5)
    base.render.set_light(slight_2_node)