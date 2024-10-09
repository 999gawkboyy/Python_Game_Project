import complexpbr
import light
from blackhole import Blackhole
from space import Space

class Game:
    def __init__(self, base):
        self.base = base  # Use the existing base (ShowBase instance)
        self.clear_screen()
        light.light()
        """
        LVecBase3f(-88.8101, -3.51555, -0.286794)
        LPoint3f(-57.7809, 10.4978, 2.57525)
        """
        # complex PBR 셰이더 적용
        complexpbr.apply_shader(self.base.render)

        # 화면 공간 효과 초기화
        complexpbr.screenspace_init()
        complexpbr.apply_shader(self.base.render, intensity=0.9, env_cam_pos=None, env_res=256)

        # 블룸 효과 설정
        screen_quad = self.base.screen_quad
        screen_quad.set_shader_input("bloom_intensity", 2.0)

        ################################################################

        base.camera.set_pos(-57.7809, 10.4978, 2.57525)
        base.camera.set_hpr(-88.8101, -3.51555, -0.286794)

        blackhole = Blackhole(base=base)
        blackhole.show(0, 0, 0)

        space = Space(base=base)
        space.show(0, 0, 0, 0.5)

    def clear_screen(self):
        """현재 화면에 있는 모든 GUI 요소를 제거"""
        for child in self.base.aspect2d.getChildren():
            child.removeNode()
