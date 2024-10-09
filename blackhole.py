import complexpbr

class Blackhole:
    def __init__(self, base):
        self.base = base

    def show(self, x: int, y: int, z: int, scale:int | None = 1):
        self.blackhole = self.base.loader.load_model("./assets/blackhole/scene.bam")
        self.blackhole.reparent_to(self.base.render)
        self.blackhole.set_pos(x, y, z)
        self.blackhole.set_scale(scale)
        self.base.task_mgr.add(self.rotate_blackhole)

    def rotate_blackhole(self, task):
        # 매 프레임마다 모델을 회전
        self.blackhole.set_h(self.blackhole.get_h() + 1)  # 1도씩 회전
        return task.cont  # 계속해서 작업을 수행