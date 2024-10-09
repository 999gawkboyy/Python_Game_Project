from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import DirectLabel, DirectButton
from panda3d.core import WindowProperties
from game import Game


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.main_page()
        props = WindowProperties() 
        props.setSize(1920, 1080) 

        self.win.requestProperties(props) 
    def main_page(self):
        """첫 번째 화면 생성"""
        self.clear_screen()

        self.label1 = DirectLabel(text="Main Page",
                                  scale=0.1,
                                  pos=(0, 0, 0.8))

        self.button1 = DirectButton(text=("Start Game"),
                                    scale=0.1,
                                    pos=(0, 0, 0.4),
                                    command=self.create_game_instance)

    def create_game_instance(self):
        """게임 인스턴스를 생성하여 두 번째 화면으로 이동"""
        self.clear_screen() 
        self.game = Game(base=self)  

    def clear_screen(self):
        """현재 화면에 있는 모든 GUI 요소를 제거"""
        for child in self.aspect2d.getChildren():
            child.removeNode()


app = MyApp()
app.run()
