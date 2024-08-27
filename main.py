from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # 윈도우 제목 설정
        props = WindowProperties()
        props.setTitle("First-Person View")
        props.setCursorHidden(True)
        self.win.requestProperties(props)

        # 마우스 포인터 숨기기
        self.disableMouse()

        # 기본적인 환경 설정
        self.setup_environment()

        # 플레이어 설정 (카메라)
        self.setup_player()

        # 키 입력 상태를 저장할 딕셔너리
        self.key_map = {
            "forward": False,
            "backward": False,
            "left": False,
            "right": False
        }

        # 키 입력 설정
        self.accept("w", self.update_key_map, ["forward", True])
        self.accept("w-up", self.update_key_map, ["forward", False])
        self.accept("s", self.update_key_map, ["backward", True])
        self.accept("s-up", self.update_key_map, ["backward", False])
        self.accept("a", self.update_key_map, ["left", True])
        self.accept("a-up", self.update_key_map, ["left", False])
        self.accept("d", self.update_key_map, ["right", True])
        self.accept("d-up", self.update_key_map, ["right", False])

        # 마우스 움직임 설정 및 플레이어 이동 task 추가
        self.taskMgr.add(self.update_camera, "update_camera")
        self.taskMgr.add(self.move_player, "move_player")

    def setup_environment(self):
        # 예시 환경 생성 (평면)
        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)

    def setup_player(self):
        # 카메라 초기 위치 설정
        self.camera.setPos(0, 0, 2)
        self.camera.lookAt(0, 1, 2)

    def update_key_map(self, key, value):
        self.key_map[key] = value

    def move_player(self, task):
        # 플레이어의 움직임을 키 상태에 따라 업데이트
        speed = 0.5
        if self.key_map["forward"]:
            self.camera.setPos(self.camera.getPos() + self.camera.getQuat().getForward() * speed)
        if self.key_map["backward"]:
            self.camera.setPos(self.camera.getPos() - self.camera.getQuat().getForward() * speed)
        if self.key_map["left"]:
            self.camera.setPos(self.camera.getPos() - self.camera.getQuat().getRight() * speed)
        if self.key_map["right"]:
            self.camera.setPos(self.camera.getPos() + self.camera.getQuat().getRight() * speed)

        return task.cont

    def update_camera(self, task):
        # 마우스 움직임에 따른 카메라 회전
        md = self.win.getPointer(0)
        x = md.getX()
        y = md.getY()

        if self.win.movePointer(0, self.win.getXSize() // 2, self.win.getYSize() // 2):
            self.camera.setH(self.camera.getH() - (x - self.win.getXSize() // 2) * 0.1)
            self.camera.setP(self.camera.getP() - (y - self.win.getYSize() // 2) * 0.1)

        return task.cont

app = MyApp()
app.run()
