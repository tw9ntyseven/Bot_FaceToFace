# -*- coding: utf-8 -*-
import vk_api
import time
import asyncio

from facematch import is_one_person

token = "1dbcda3e92d5fc461cf43916382318e64202ac8e3fa85317139c4f01a9497a3bc0fff2d2621c673c3baa3"

vk = vk_api.VkApi(token=token)

vk._auth_token()

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages['items'][0]['last_message']['from_id']
            attachments = messages['items'][0]['last_message'].get('attachments', None)
            if attachments and len(attachments) == 2:
                img1 = attachments[0]['photo']['sizes'][2]['url']
                # print(img1)
                img2 = attachments[1]['photo']['sizes'][2]['url']
                print(img1)
                result = is_one_person(img1,img2)
                print(result)
                vk.method("messages.send", {"random_id": 0, "peer_id": id, "message": result})
            else:
                vk.method("messages.send", {"random_id": 0, "peer_id": id, "message": "Отправьте 2 фотографии одним сообщением!"})
    except Exception as E:
        time.sleep(20)