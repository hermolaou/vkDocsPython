# -*- coding: utf-8 -*-
import vk_api

# from src.config import ACCESS_TOKEN

class VkService:
    def __init__(self):
        self.vk_session = None
        self.vk = None

    def auth(self, token):
        # vk_session = vk_api.VkApi(token=ACCESS_TOKEN)
        self.vk_session = vk_api.VkApi(token=token)
        # try:
        #     vk_session.auth(token_only=True)
        # except vk_api.AuthError as error_msg:
        #     print(error_msg)
        #     return

        self.vk = self.vk_session.get_api()
        return self.vk

    def get_docs(self, token):
        vk = self.auth(token)
        response = vk.docs.get()  # Используем метод wall.get
        print(vk.docs)

        if response['items']:
            return response['items']

    def search_docs(self, search, own_docs, token):
        vk = self.auth(token)
        docs = []
        docs = vk.docs.search(q=search, search_own=own_docs)
        print(docs)
        if docs != []:
            return docs['items']

        return docs

# asd = VkService()
# docs = asd.search_docs("asd", True, token="vk1.a.939Tzj4dnuf6WtP9Ish2OS4zuy0Sol2Un4Y1EZh4on25DhF0XpBOWRFhn_SLB8jQlmkMcz2-nit67x2to8tZflYd_N_cPE3yDopupFy8XRF4BZE4Y9hQRmKbogn4AGAR0XXv6GyUgQbt2hovy8unhykzYg5jmeOc0O11d5DW9cakXpkMGgL44JrL7bZ3pA5w")

# for doc in docs:
#     print(doc['title'])
