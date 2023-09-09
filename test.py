from vk_cli import vk_api

token = "vk1.a.5q8Ie5tD2NUkRt0bwQ9lQk-gcXLpKUg_MWYsnqrwqp6br-OYA07JdUp7Hq8cZ6nSi2AQnLwoo2CJxbHB2X1updgpuX8dtUaefmpUG3zdMJp4GGjchgWe30B63AUalIqYFnR06whiC7Ktv4N1VY7lob6b40y1pO6m_bKTHAYkrLLmAm_2utNUTDSRZJonW1WRYlKDPubEWxYdZxN9bDu9DQ"

vk = vk_api.API(token)
a = vk.lrequest("messages.getConversations", count=10)

convs = a["items"]
uids = []
chids = []
gids = []
chats = []
for i in convs:
    if i["conversation"]["peer"]["type"] == "user":
        uids.append(i["conversation"]["peer"]["id"])
    if i["conversation"]["peer"]["type"] == "group":
        gids.append(i["conversation"]["peer"]["local_id"])
    if i["conversation"]["peer"]["type"] == "chat":
        chids.append(i["conversation"]["peer"]["id"])
        chats.append(i["conversation"]["chat_settings"]["title"])

users = list(map(lambda user: f"{user['first_name']} {user['last_name']}",vk.lrequest("users.get", user_ids=uids)))
groups = list(map(lambda group: group["name"],vk.lrequest("groups.getById", group_ids=gids)))

# title = vk.lrequest("users.get", user_ids = id)
print(uids, chids, gids)
print(users, chats, groups)

# print(vk.lrequest("messages.getConversationsById", peer_ids = id))