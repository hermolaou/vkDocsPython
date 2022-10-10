# -*- coding: utf-8 -*-
import vk_api

# from src.config import ACCESS_TOKEN


def _auth(token: str):
    # vk_session = vk_api.VkApi(token=ACCESS_TOKEN)
    vk_session = vk_api.VkApi(token=token)
    # try:
    #     vk_session.auth(token_only=True)
    # except vk_api.AuthError as error_msg:
    #     print(error_msg)
    #     return

    vk = vk_session.get_api()

    return vk


def get_docs(token: str):
    vk = _auth(token)
    response = vk.docs.get()  # Используем метод wall.get

    if response['items']:
        return response['items']
        # print(response['items'][0])


def main():
    """ Пример получения последнего сообщения со стены """
    pass


if __name__ == '__main__':
    main()
