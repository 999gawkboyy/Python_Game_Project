import complexpbr
import light
from blackhole import Blackhole
from panda3d.core import WindowProperties, Vec3
from space import Space
from mouse_control import MouseControl

class Game:
    def __init__(self, base):
        self.base = base  # Use the existing base (ShowBase instance)
        self.clear_screen()
        light.light()
        mc = MouseControl(base=base)

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

        # 카메라 이동 속도 및 마우스 감도 설정
        base.camera_speed = 10
        self.mouse_sensitivity = 0.2

        mc.disable_mouse()

        # 키보드 입력을 추적하기 위한 키 상태 초기화
        self.key_map = {"w": False, "a": False, "s": False, "d": False}

        # 키보드 입력을 등록
        base.accept("w", self.update_key_map, ["w", True])
        base.accept("a", self.update_key_map, ["a", True])
        base.accept("s", self.update_key_map, ["s", True])
        base.accept("d", self.update_key_map, ["d", True])
        base.accept("escape", mc.enable_mouse)
        base.accept("w-up", self.update_key_map, ["w", False])
        base.accept("a-up", self.update_key_map, ["a", False])
        base.accept("s-up", self.update_key_map, ["s", False])
        base.accept("d-up", self.update_key_map, ["d", False])

        # 태스크 추가
        base.taskMgr.add(self.update_camera, "update_camera")

    def update_key_map(self, key, value):
        """키 입력을 처리하여 상태를 업데이트"""
        self.key_map[key] = value

    def update_camera(self, task):
        """카메라 위치 및 시점을 업데이트"""
        dt = globalClock.getDt()  # 프레임 간 경과 시간

        # 마우스 시점 조작
        md = self.base.win.getPointer(0)
        mouse_x = md.getX()
        mouse_y = md.getY()

        # 마우스 센터로부터의 거리 계산
        center_x = self.base.win.getProperties().getXSize() // 2
        center_y = self.base.win.getProperties().getYSize() // 2
        delta_x = (mouse_x - center_x) * self.mouse_sensitivity
        delta_y = (mouse_y - center_y) * self.mouse_sensitivity

        # 카메라 회전 업데이트 (heading과 pitch 조정)
        self.base.camera.setH(self.base.camera.getH() - delta_x)
        self.base.camera.setP(self.base.camera.getP() - delta_y)

        # 마우스를 화면 중앙으로 재설정
        self.base.win.movePointer(0, center_x, center_y)

        # WASD로 카메라 이동
        move_vector = Vec3(0, 0, 0)
        if self.key_map["w"]:
            move_vector += self.base.camera.getQuat().getForward() * self.base.camera_speed * dt
        if self.key_map["s"]:
            move_vector -= self.base.camera.getQuat().getForward() * self.base.camera_speed * dt
        if self.key_map["a"]:
            move_vector -= self.base.camera.getQuat().getRight() * self.base.camera_speed * dt
        if self.key_map["d"]:
            move_vector += self.base.camera.getQuat().getRight() * self.base.camera_speed * dt

        self.base.camera.setPos(self.base.camera.getPos() + move_vector)

        return task.cont

    def clear_screen(self):
        """현재 화면에 있는 모든 GUI 요소를 제거"""
        for child in self.base.aspect2d.getChildren():
            child.removeNode()
