from . import vk_api
import json
import urwid
import asyncio


class vk_cli:
    def __init__(self, args, config):
        self.config = self.parse_config(config)
        self.vk = vk_api.API(self.config["auth"][0])
        self.__run__()
        self.runtime_data = {"conversations": {"users":[],"groups":[],"chats":[]}, "new_messages": [], "chat_messages":[]}
    
    def __run__(self):
        from . import vk_ui
        self.ui = vk_ui.UI(self.vk, self.config)
        self.lb = urwid.LineBox(self.ui, "VK-cli by JUNQ")


        aloop = asyncio.get_event_loop()
        ev_loop = urwid.AsyncioEventLoop(loop=aloop)
        loop = urwid.MainLoop(self.lb,
                            unhandled_input=self.unhandled, event_loop=ev_loop)
        aloop.create_task(self.async_loop())
        loop.run()
    
    def unhandled(self, key):
        if key in ("Q","q","й","Й"):
            raise urwid.ExitMainLoop()
        elif key in ("1","!"):
            self.ui.convs_list()
        elif key in ("2","@"):
            self.ui.chat_list()
    
    async def async_loop(self):
        ...


        
    
    def parse_config(self, config_path):
        with open (config_path, "r+") as file:
            config  = json.load(file)
        
        return config