from kivy.config import Config

# Mobile keyboard configuration - PERFECT SETTINGS
Config.set('kivy', 'keyboard_mode', 'systemandmulti')
Config.set('kivy', 'keyboard_layout', 'qwerty')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '700')
Config.set('graphics', 'resizable', False)
Config.set('kivy', 'exit_on_escape', '0')
Config.set('input', 'mouse', 'mouse,disable_multitouch')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, RoundedRectangle, Line
from kivy.core.clipboard import Clipboard
from kivy.uix.popup import Popup
from kivy.metrics import dp
import random
import webbrowser
import os
import sys

# Window settings
Window.clearcolor = get_color_from_hex('#0A0A1A')
Window.size = (400, 700)
Window.borderless = True
Window.softinput_mode = 'pan'
Window.keyboard_anim_args = {'d': 0.2, 't': 'in_out_quad'}

# Block all closing methods
from kivy.core.window import WindowBase
original_on_close = WindowBase.on_close
def block_close(*args):
    return True
WindowBase.on_close = block_close

# Block exit attempts
old_exit = sys.exit
def block_exit(*args, **kwargs):
    pass
sys.exit = block_exit

old_os_exit = os._exit
def block_os_exit(*args, **kwargs):
    pass
os._exit = block_os_exit

class ContactPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = " "
        self.size_hint = (0.85, 0.6)
        self.background = ''
        self.separator_height = 0
        self.auto_dismiss = True
        
        content = BoxLayout(orientation='vertical', spacing=15, padding=[25, 30, 25, 25])
        
        with content.canvas.before:
            Color(0.12, 0.08, 0.20, 0.98)
            self.rect = RoundedRectangle(pos=content.pos, size=content.size, radius=[30])
            Color(0.8, 0.4, 1, 0.2)
            Line(rounded_rectangle=(content.x, content.y, content.width, content.height, 30), width=2)
        
        content.bind(pos=self.update_rect, size=self.update_rect)
        
        title_label = Label(
            text="DEVELOPER",
            font_size='24sp',
            bold=True,
            color=get_color_from_hex('#C792EA'),
            size_hint=(1, 0.2)
        )
        content.add_widget(title_label)
        
        name_label = Label(
            text="SAKIB AHMED SADI",
            font_size='26sp',
            bold=True,
            color=get_color_from_hex('#4AE54A'),
            size_hint=(1, 0.2)
        )
        content.add_widget(name_label)
        
        username_label = Label(
            text="@sakibahmedsadi",
            font_size='20sp',
            color=get_color_from_hex('#AAAAAA'),
            size_hint=(1, 0.15)
        )
        content.add_widget(username_label)
        
        button_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 0.3))
        
        telegram_btn = Button(
            text="OPEN TELEGRAM",
            size_hint=(1, None),
            height='50dp',
            background_normal='',
            background_color=get_color_from_hex('#0088cc'),
            color=(1,1,1,1),
            bold=True,
            font_size='18sp'
        )
        telegram_btn.bind(on_release=lambda x: webbrowser.open('https://t.me/sakibahmedsadi'))
        button_layout.add_widget(telegram_btn)
        
        copy_btn = Button(
            text="COPY USERNAME",
            size_hint=(1, None),
            height='50dp',
            background_normal='',
            background_color=get_color_from_hex('#6A0DAD'),
            color=(1,1,1,1),
            bold=True,
            font_size='18sp'
        )
        copy_btn.bind(on_release=lambda x: self.copy_username())
        button_layout.add_widget(copy_btn)
        
        content.add_widget(button_layout)
        
        close_btn = Button(
            text="CLOSE",
            size_hint=(1, 0.15),
            background_normal='',
            background_color=get_color_from_hex('#2A2A3A'),
            color=get_color_from_hex('#FFFFFF'),
            bold=True,
            font_size='16sp'
        )
        close_btn.bind(on_release=self.dismiss)
        content.add_widget(close_btn)
        
        self.content = content
        self.username_copied = False
    
    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    def copy_username(self):
        Clipboard.copy('@sakibahmedsadi')
        self.username_copied = True
        for child in self.content.children:
            if isinstance(child, Label) and child.text == "@sakibahmedsadi":
                child.text = "USERNAME COPIED"
                child.color = get_color_from_hex('#4AE54A')
                Clock.schedule_once(lambda dt: self.reset_username(), 2)
                break
    
    def reset_username(self):
        for child in self.content.children:
            if isinstance(child, Label) and child.text == "USERNAME COPIED":
                child.text = "@sakibahmedsadi"
                child.color = get_color_from_hex('#AAAAAA')
                break

class CyberExpertApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.can_close = False
        self.attempts = 0
        self.close_attempts = 0
        self.lock_active = True
        self.keyboard_visible = False
        
    def build(self):
        Window.bind(on_request_close=self.on_request_close)
        
        main = BoxLayout(orientation='vertical', padding=[25, 35, 25, 25], spacing=12)
        
        with main.canvas.before:
            Color(0.02, 0.02, 0.05, 1)
            self.bg_rect = Rectangle(pos=main.pos, size=main.size)
            
            Color(0.3, 0.1, 0.5, 0.1)
            for i in range(8):
                Line(circle=(random.randint(0, 400), random.randint(0, 700), 3), width=0.5)
        
        main.bind(pos=self.update_bg, size=self.update_bg)
        
        top_bar = BoxLayout(size_hint=(1, 0.08), spacing=10)
        
        self.cyber_label = Label(
            text="CYBER EXPERT",
            font_size='28sp',
            bold=True,
            color=get_color_from_hex('#C792EA'),
            size_hint=(0.7, 1),
            halign='left'
        )
        self.cyber_label.bind(size=self.cyber_label.setter('text_size'))
        top_bar.add_widget(self.cyber_label)
        
        self.lock_status = Label(
            text="LOCK",
            font_size='18sp',
            bold=True,
            color=get_color_from_hex('#FF6B6B'),
            size_hint=(0.3, 1),
            halign='right'
        )
        self.lock_status.bind(size=self.lock_status.setter('text_size'))
        top_bar.add_widget(self.lock_status)
        
        main.add_widget(top_bar)
        
        main.add_widget(Widget(size_hint=(1, 0.02)))
        
        self.lock_label = Label(
            text="[ LOCKED ]",
            font_size='28sp',
            bold=True,
            color=get_color_from_hex('#FF6B6B'),
            size_hint=(1, 0.1)
        )
        main.add_widget(self.lock_label)
        
        main.add_widget(Widget(size_hint=(1, 0.03)))
        
        name_container = BoxLayout(orientation='vertical', size_hint=(1, 0.15), spacing=5)
        
        self.name_display = Label(
            text="SAKIB AHMED SADI",
            font_size='24sp',
            bold=True,
            color=get_color_from_hex('#4AE54A'),
            size_hint=(1, 0.5)
        )
        name_container.add_widget(self.name_display)
        
        self.telegram_display = Label(
            text="@sakibahmedsadi",
            font_size='18sp',
            color=get_color_from_hex('#89DDB8'),
            size_hint=(1, 0.5)
        )
        self.telegram_display.bind(on_touch_down=self.show_contact)
        name_container.add_widget(self.telegram_display)
        
        main.add_widget(name_container)
        
        main.add_widget(Widget(size_hint=(1, 0.05)))
        
        instruction_label = Label(
            text="ENTER PASSWORD TO EXIT APPLICATION",
            font_size='14sp',
            color=get_color_from_hex('#AAAAAA'),
            size_hint=(1, 0.06)
        )
        main.add_widget(instruction_label)
        
        self.password_input = TextInput(
            hint_text="PASSWORD",
            password=True,
            multiline=False,
            size_hint=(1, 0.1),
            font_size='24sp',
            halign='center',
            background_color=get_color_from_hex('#151525'),
            foreground_color=get_color_from_hex('#FFFFFF'),
            cursor_color=get_color_from_hex('#C792EA'),
            hint_text_color=get_color_from_hex('#45455A'),
            padding=(15, 15),
            input_filter=None,
            write_tab=False,
            on_focus=self.on_keyboard_focus
        )
        main.add_widget(self.password_input)
        
        main.add_widget(Widget(size_hint=(1, 0.02)))
        
        self.action_button = Button(
            text="UNLOCK & EXIT",
            size_hint=(1, 0.1),
            background_normal='',
            background_color=get_color_from_hex('#FF6B6B'),
            color=get_color_from_hex('#FFFFFF'),
            bold=True,
            font_size='22sp'
        )
        self.action_button.bind(on_release=self.verify_password)
        main.add_widget(self.action_button)
        
        main.add_widget(Widget(size_hint=(1, 0.02)))
        
        self.status_display = Label(
            text="SYSTEM SECURE",
            font_size='14sp',
            color=get_color_from_hex('#5A5A7A'),
            size_hint=(1, 0.05)
        )
        main.add_widget(self.status_display)
        
        footer_layout = BoxLayout(size_hint=(1, 0.06), spacing=5)
        
        self.close_counter = Label(
            text="CLOSE: 0",
            font_size='12sp',
            color=get_color_from_hex('#3A3A4A'),
            size_hint=(0.5, 1),
            halign='left'
        )
        self.close_counter.bind(size=self.close_counter.setter('text_size'))
        footer_layout.add_widget(self.close_counter)
        
        self.keyboard_hint = Label(
            text="KEYBOARD: TAP TO TYPE",
            font_size='10sp',
            color=get_color_from_hex('#4AE54A'),
            size_hint=(0.5, 1),
            halign='right'
        )
        self.keyboard_hint.bind(size=self.keyboard_hint.setter('text_size'))
        footer_layout.add_widget(self.keyboard_hint)
        
        main.add_widget(footer_layout)
        
        Clock.schedule_interval(self.animate_elements, 2)
        Clock.schedule_interval(self.pulse_lock, 1.2)
        Clock.schedule_interval(self.check_lock_status, 0.5)
        
        return main
    
    def on_keyboard_focus(self, instance, value):
        if value:
            self.keyboard_visible = True
            self.keyboard_hint.text = "KEYBOARD: OPEN"
            self.keyboard_hint.color = get_color_from_hex('#4AE54A')
        else:
            self.keyboard_visible = False
            self.keyboard_hint.text = "KEYBOARD: TAP TO TYPE"
            self.keyboard_hint.color = get_color_from_hex('#AAAAAA')
    
    def show_contact(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.password_input.focus = False
            ContactPopup().open()
    
    def on_request_close(self, *args):
        self.close_attempts += 1
        self.close_counter.text = f"CLOSE: {self.close_attempts}"
        
        if self.can_close:
            return False
        else:
            self.status_display.text = "ENTER PASSWORD FIRST"
            self.status_display.color = get_color_from_hex('#FF6B6B')
            self.shake_component(self.action_button)
            self.shake_component(self.lock_label)
            self.shake_component(self.password_input)
            
            Animation(background_color=get_color_from_hex('#FF0000'), duration=0.1).start(self.action_button)
            Clock.schedule_once(lambda dt: self.reset_button_color(), 0.2)
            
            Clock.schedule_once(lambda dt: self.reset_display(), 2)
            return True
    
    def reset_button_color(self):
        Animation(background_color=get_color_from_hex('#FF6B6B'), duration=0.1).start(self.action_button)
    
    def check_lock_status(self, dt):
        if not self.can_close and self.lock_active:
            Window.bind(on_request_close=self.on_request_close)
    
    def update_bg(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size
    
    def animate_elements(self, dt):
        colors = ['#C792EA', '#9D7AD9', '#B392E0', '#C792EA']
        self.cyber_label.color = get_color_from_hex(random.choice(colors))
    
    def pulse_lock(self, dt):
        if not self.can_close:
            colors = ['#FF6B6B', '#FF8585', '#FFA0A0', '#FF6B6B']
            color = get_color_from_hex(random.choice(colors))
            Animation(color=color, duration=0.3).start(self.lock_label)
    
    def verify_password(self, instance):
        if self.password_input.text == "sakib123":
            self.can_close = True
            self.lock_active = False
            self.status_display.text = "ACCESS GRANTED"
            self.status_display.color = get_color_from_hex('#4AE54A')
            self.action_button.background_color = get_color_from_hex('#4AE54A')
            self.action_button.text = "EXITING"
            self.lock_label.text = "[ UNLOCKED ]"
            self.lock_label.color = get_color_from_hex('#4AE54A')
            self.lock_status.text = "UNLOCK"
            self.lock_status.color = get_color_from_hex('#4AE54A')
            
            self.password_input.focus = False
            
            anim = Animation(font_size='30sp', duration=0.2) + Animation(font_size='28sp', duration=0.2)
            anim.start(self.lock_label)
            
            Clock.schedule_once(lambda dt: self.stop(), 1.5)
        else:
            self.attempts += 1
            self.password_input.text = ""
            self.password_input.hint_text = f"INVALID ({self.attempts})"
            self.shake_component(self.password_input)
            self.shake_component(self.action_button)
            self.shake_component(self.lock_label)
            self.status_display.text = "ACCESS DENIED"
            self.status_display.color = get_color_from_hex('#FF3B3B')
            self.action_button.background_color = get_color_from_hex('#FF3B3B')
            
            self.password_input.focus = True
            
            Clock.schedule_once(self.reset_interface, 2)
    
    def reset_interface(self, dt=None):
        self.status_display.text = "SYSTEM SECURE"
        self.status_display.color = get_color_from_hex('#5A5A7A')
        self.action_button.background_color = get_color_from_hex('#FF6B6B')
        self.action_button.text = "UNLOCK & EXIT"
        self.password_input.hint_text = "PASSWORD"
        self.lock_label.text = "[ LOCKED ]"
        self.lock_label.color = get_color_from_hex('#FF6B6B')
    
    def reset_display(self, dt=None):
        if not self.can_close:
            self.status_display.text = "SYSTEM SECURE"
            self.status_display.color = get_color_from_hex('#5A5A7A')
    
    def shake_component(self, widget):
        orig_x = widget.pos_hint.get('center_x', 0.5)
        anim = Animation(pos_hint={'center_x': 0.47}, duration=0.02) + \
               Animation(pos_hint={'center_x': 0.53}, duration=0.02) + \
               Animation(pos_hint={'center_x': 0.48}, duration=0.02) + \
               Animation(pos_hint={'center_x': 0.52}, duration=0.02) + \
               Animation(pos_hint={'center_x': 0.49}, duration=0.02) + \
               Animation(pos_hint={'center_x': 0.51}, duration=0.02) + \
               Animation(pos_hint={'center_x': orig_x}, duration=0.02)
        anim.start(widget)

if __name__ == '__main__':
    CyberExpertApp().run()
