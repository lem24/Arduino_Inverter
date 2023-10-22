from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.uix import gridlayout

KV = '''
MDScreen: 
    MDLabel:
        id: bo_x
        text: "Arduino Uno"
        pos_hint: {"center_x": 0.95, "center_y": 0.95}
        # theme_text_color: "Custom"
        font_style: "H6"
        text_color: 0, 0, 1, 1  

# -----------------------------Digital label text-----------------------------
    Label:
        id: D2
        text: "Digital Out 2"
        pos_hint: {"center_x": 0.1, "center_y": 0.1}
        theme_text_color: "Custom"
    Label:
        id: D3
        text: "Digital Out 3"
        pos_hint: {"center_x": 0.1, "center_y": 0.2}
        theme_text_color: "Custom"
    Label:
        id: D4
        text: "Digital Out 4"
        pos_hint: {"center_x": 0.1, "center_y": 0.3}
        theme_text_color: "Custom"
    Label:
        id: D5
        text: "Digital Out 5"
        pos_hint: {"center_x": 0.1, "center_y": 0.4}
        theme_text_color: "Custom"
    Label:
        id: D6
        text: "Digital Out 6"
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        theme_text_color: "Custom"
    Label:
        id: D7
        text: "Digital Out 7"
        pos_hint: {"center_x": 0.1, "center_y": 0.6}
        theme_text_color: "Custom"
    Label:
        id: D8
        text: "Digital Out 8"
        pos_hint: {"center_x": 0.1, "center_y": 0.7}
        theme_text_color: "Custom" 
    Label:
        id: D9
        text: "Digital Out 9"
        pos_hint: {"center_x": 0.1, "center_y": 0.8}
        theme_text_color: "Custom" 

# --------------------------Red indecator--------------------------- 
    MDIconButton:
        id: icon_led2
        icon: "D:\python-kivymd\img\down_led-removebg-preview.png"
        pos_hint: {"center_x": .2, "center_y": .1}
    MDIconButton:
        id: icon_led3
        icon: "D:\python-kivymd\img\down_led-removebg-preview.png"
        pos_hint: {"center_x": .2, "center_y": .2}
    MDIconButton:
        id: icon_led4
        icon: "D:\python-kivymd\img\down_led-removebg-preview.png"
        pos_hint: {"center_x": .2, "center_y": .3}
    MDIconButton:
        id: icon_led5
        icon: "D:\python-kivymd\img\down_led-removebg-preview.png"
        pos_hint: {"center_x": .2, "center_y": .4}
    MDIconButton:
        id: icon_led6
        icon: "D:\python-kivymd\img\down_led-removebg-preview.png"
        pos_hint: {"center_x": .2, "center_y": .5}
    MDIconButton:
        id: icon_led7
        icon: "D:/python-kivymd/img/down_led-removebg-preview.png"
        pos_hint: {"center_x": .2, "center_y": .6}
    MDIconButton:
        id: icon_led8
        icon: "D:/python-kivymd/img/down_led-removebg-preview.png"
        pos_hint: {"center_x": .2, "center_y": .7}
    MDIconButton:
        id: icon_led9
        icon: "D:/python-kivymd/img/down_led-removebg-preview.png"
        pos_hint: {"center_x": .2, "center_y": .8}

# ------------------------- On-Off button------------------------------- 
    MDRoundFlatButton:
        id: flatbutton2
        text: "On-Off"
        text_color: "white"
        pos_hint: {"center_x": .9, "center_y": .1}
        on_press: app.change_red2()
    MDRoundFlatButton:
        id: flatbutton3
        text: "On-Off"
        text_color: "white"
        pos_hint: {"center_x": .9, "center_y": .2}
        on_press: app.change_red3()
    MDRoundFlatButton:
        id: flatbutton4
        text: "On-Off"
        text_color: "white"
        pos_hint: {"center_x": .9, "center_y": .3}
        on_press: app.change_red4()
    MDRoundFlatButton:
        id: flatbutton5
        text: "On-Off"
        text_color: "white"
        pos_hint: {"center_x": .9, "center_y": .4}
        on_press: app.change_red5()
    MDRoundFlatButton:
        id: flatbutton6
        text: "On-Off"
        text_color: "white"
        pos_hint: {"center_x": .9, "center_y": .5}
        on_press: app.change_red6()
    MDRoundFlatButton:
        id: flatbutton7
        text: "On-Off"
        text_color: "white"
        pos_hint: {"center_x": .9, "center_y": .6}
        on_press: app.change_red7()
    MDRoundFlatButton:
        # id: flatbutton8
        text: "On-Off"
        text_color: "white"
        pos_hint: {"center_x": .9, "center_y": .7}
        on_press: app.change_red8()
    MDRoundFlatButton:
        # id: flatbutton9
        text: "On-Off"
        text_color: "white"
        pos_hint: {"center_x": .9, "center_y": .8}
        on_press: app.change_red9()

# ----------------------------- other ------------------------------------ 
    Image:
        source: "D:/python-kivymd/img/arduino_uno.png" 

'''


class Example(MDApp):
    def change_red2(self):
        status_on = "D:/python-kivymd/img/up_red_led-removebg-preview.png"
        status_off = "D:/python-kivymd/img/down_led-removebg-preview.png"
        if (self.root.ids.icon_led2.icon == status_off):
            self.root.ids.icon_led2.icon = status_on
        else:
            self.root.ids.icon_led2.icon = status_off
    def change_red3(self):
        status_on = "D:/python-kivymd/img/up_red_led-removebg-preview.png"
        status_off = "D:/python-kivymd/img/down_led-removebg-preview.png"
        if (self.root.ids.icon_led3.icon == status_off):
            self.root.ids.icon_led3.icon = status_on
        else:
            self.root.ids.icon_led3.icon = status_off
    def change_red4(self):
        status_on = "D:/python-kivymd/img/up_red_led-removebg-preview.png"
        status_off = "D:/python-kivymd/img/down_led-removebg-preview.png"
        if (self.root.ids.icon_led4.icon == status_off):
            self.root.ids.icon_led4.icon = status_on
        else:
            self.root.ids.icon_led4.icon = status_off
    def change_red5(self):
        status_on = "D:/python-kivymd/img/up_red_led-removebg-preview.png"
        status_off = "D:/python-kivymd/img/down_led-removebg-preview.png"
        if (self.root.ids.icon_led5.icon == status_off):
            self.root.ids.icon_led5.icon = status_on
        else:
            self.root.ids.icon_led5.icon = status_off
    def change_red6(self):
        status_on = "D:/python-kivymd/img/up_red_led-removebg-preview.png"
        status_off = "D:/python-kivymd/img/down_led-removebg-preview.png"
        if (self.root.ids.icon_led6.icon == status_off):
            self.root.ids.icon_led6.icon = status_on
        else:
            self.root.ids.icon_led6.icon = status_off

    def change_red7(self):
        status_on = "D:/python-kivymd/img/up_red_led-removebg-preview.png"
        status_off = "D:/python-kivymd/img/down_led-removebg-preview.png"
        if (self.root.ids.icon_led7.icon == status_off):
            self.root.ids.icon_led7.icon = status_on
        else:
            self.root.ids.icon_led7.icon = status_off

    def change_red8(self):
        status_on = "D:/python-kivymd/img/up_red_led-removebg-preview.png"
        status_off = "D:/python-kivymd/img/down_led-removebg-preview.png"
        if (self.root.ids.icon_led8.icon == status_off):
            self.root.ids.icon_led8.icon = status_on
        else:
            self.root.ids.icon_led8.icon = status_off

    def change_red9(self):
        status_on = "D:/python-kivymd/img/up_red_led-removebg-preview.png"
        status_off = "D:/python-kivymd/img/down_led-removebg-preview.png"
        if (self.root.ids.icon_led9.icon == status_off):
            self.root.ids.icon_led9.icon = status_on
        else:
            self.root.ids.icon_led9.icon = status_off

    # main widgid
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)


Example().run()