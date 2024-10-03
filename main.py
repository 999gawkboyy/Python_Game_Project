from direct.showbase.ShowBase import ShowBase
import complexpbr

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()

        # 모델 로드
        self.model = self.loader.load_model("./assets/scene.bam")
        self.model.reparent_to(self.render)
        self.camera.set_pos(0, -10, 2)  # 카메라를 모델 뒤쪽으로 이동
        self.camera.look_at(self.model)
        self.model.set_pos(0, 5, 0) 
        # 복잡한 PBR 셰이더 적용
        complexpbr.apply_shader(self.render)

        # 화면 공간 효과 초기화
        complexpbr.screenspace_init()

        complexpbr.apply_shader(self.render, intensity=0.9, env_cam_pos=None, env_res=256)


        # 블룸 효과 설정
        screen_quad = base.screen_quad
        screen_quad.set_shader_input("bloom_intensity", 2.0)

        self.task_mgr.add(self.rotate_model)

    def rotate_model(self, task):
        # 매 프레임마다 모델을 회전
        self.model.set_h(self.model.get_h() + 1)  # 1도씩 회전
        return task.cont  # 계속해서 작업을 수행

app = MyApp()
app.run()
