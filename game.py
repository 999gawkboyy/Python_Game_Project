from direct.showbase.ShowBase import ShowBase
import complexpbr
from panda3d.core import DirectionalLight, AmbientLight, LVector3
from direct.filter.CommonFilters import CommonFilters
from panda3d.core import PointLight, Vec3, Vec4
import light

class Game(ShowBase):
    def __init__(self):
        super().__init__()

        light.light()

        self.blackhole = self.loader.load_model("./assets/blackhole/scene.bam")
        self.blackhole.reparent_to(base.render)
        self.blackhole.set_pos(0, 0, 0) 

        self.camera.set_pos(0, -10, 0)  # 카메라를 모델 뒤쪽으로 이동
        
        env_light_1 = PointLight('env_light_1')
        env_light_1.set_color(Vec4(Vec3(6),1))
        env_light_1 = base.render.attach_new_node(env_light_1)
        env_light_1.set_pos(0,0,0)

        self.space = self.loader.load_model("./assets/space/space.bam")
        self.space.reparent_to(base.render)
        self.space.set_pos(0, 0, 0)
        self.space.set_scale(0.5)
        self.space.set_light(env_light_1)

        # complex PBR 셰이더 적용
        complexpbr.apply_shader(self.render)

        # 화면 공간 효과 초기화
        complexpbr.screenspace_init()
        complexpbr.apply_shader(self.render, intensity=0.9, env_cam_pos=None, env_res=256)
       

        # 블룸 효과 설정
        screen_quad = base.screen_quad
        screen_quad.set_shader_input("bloom_intensity", 2.0)

        self.task_mgr.add(self.rotate_blackhole)

    def rotate_blackhole(self, task):
        # 매 프레임마다 모델을 회전
        self.blackhole.set_h(self.blackhole.get_h() + 1)  # 1도씩 회전
        return task.cont  # 계속해서 작업을 수행

app = Game()
app.run()
