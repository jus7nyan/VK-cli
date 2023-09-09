import aiohttp
import json
import requests


class API:
    def __init__(self, token):
        self.api_url = "https://api.vk.com/method/"
        self.api_version = "5.131"
        self.token = token

    def req_gen(self, method, args):
        r = f"{self.api_url}{method}?v={self.api_version}&access_token={self.token}"
        for i in args.keys():
            if type(args[i]) != list:
                r += f"&{i}={args[i]}"
            else:
                r += f"&{i}={str(args[i])[1:-1]}"
        return r

    async def arequest(self, method, **args):
        async with aiohttp.ClientSession() as session:
            r = self.req_gen(method, args)

            async with session.get(r) as resp:

                return json.loads(await resp.text())["response"]
                try:
                    return json.loads(await resp.text())["response"]
                except:
                    return json.loads(await resp.text())
    
    def lrequest(self, method, **args):
        r = self.req_gen(method, args)

        a = requests.get(r)
        try:
            return a.json()["response"]
        except:
            return a.json()
