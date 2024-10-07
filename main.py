from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import *

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.create_screen_1()

    def create_screen_1(self):
        """첫 번째 화면 생성"""
        self.clear_screen()

        self.label1 = DirectLabel(text="This is Screen 1",
                                  scale=0.1,
                                  pos=(0, 0, 0.8))

        self.button1 = DirectButton(text=("Go to Screen 2"),
                                    scale=0.1,
                                    pos=(0, 0, 0.4),
                                    command=self.create_screen_2)

        self.button2 = DirectButton(text=("Go to Screen 3"),
                                    scale=0.1,
                                    pos=(0, 0, 0.2),
                                    command=self.create_screen_3)

    def create_screen_2(self):
        """두 번째 화면 생성"""
        self.clear_screen()

        self.label2 = DirectLabel(text="This is Screen 2",
                                  scale=0.1,
                                  pos=(0, 0, 0.8))

        self.button1 = DirectButton(text=("Go to Screen 1"),
                                    scale=0.1,
                                    pos=(0, 0, 0.4),
                                    command=self.create_screen_1)

        self.button2 = DirectButton(text=("Go to Screen 3"),
                                    scale=0.1,
                                    pos=(0, 0, 0.2),
                                    command=self.create_screen_3)

    def create_screen_3(self):
        """세 번째 화면 생성"""
        self.clear_screen()

        self.label3 = DirectLabel(text="This is Screen 3",
                                  scale=0.1,
                                  pos=(0, 0, 0.8))

        self.button1 = DirectButton(text=("Go to Screen 1"),
                                    scale=0.1,
                                    pos=(0, 0, 0.4),
                                    command=self.create_screen_1)

        self.button2 = DirectButton(text=("Go to Screen 2"),
                                    scale=0.1,
                                    pos=(0, 0, 0.2),
                                    command=self.create_screen_2)

    def clear_screen(self):
        """현재 화면에 있는 모든 GUI 요소를 제거"""
        for child in self.aspect2d.getChildren():
            child.removeNode()

app = MyApp()
app.run()
