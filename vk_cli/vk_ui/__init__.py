import urwid
import asyncio


class Conversation(urwid.LineBox):
    def __init__(self, title, last_message, c_type, c_id, ui):
        self.type = c_type
        self.id = c_id
        ow = urwid.Button(label=urwid.Text(title), on_press=self.on_press, user_data=(self.id,self.type))
        super().__init__(original_widget=ow,title=title)
    
    def on_press(self, c_id, c_type):
        print(c_id,c_type)

class UI(urwid.Filler):
    def __init__(self,config,vk):
        body = urwid.Text(u"")
        super().__init__(body)
        self.config = config
        self.vk = vk

        self.convs_list()


    def convs_list(self):
        self.original_widget = urwid.BoxAdapter(urwid.ListBox([urwid.Text(U"Dimsda Dsdasdfa"),urwid.Text(U"Masdsa Fsdasdfa") ]), 5)
        
    def chat_list(self):
        self.original_widget = urwid.BoxAdapter(urwid.ListBox([urwid.Text(U"Dimsda Dsdasdfa",align="left"),urwid.Text(U"Masdsa Fsdasdfa",align="right") ]),5)