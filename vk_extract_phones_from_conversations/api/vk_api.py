import os

from vk_extract_phones_from_conversations.utils import requests_cache_decorator as r

API_URL = "https://api.vk.com/method/"
STANDARD_OFFSET = 200
VK_API_TOKEN = os.environ.get("VK_API_TOKEN")


def get_conversations(page: int = 0):
    response = r.get(API_URL + f"messages.getConversations?extended=1&v=5.199&count={STANDARD_OFFSET}"
                               f"&offset={page * STANDARD_OFFSET}&access_token={VK_API_TOKEN}")
    return response


def get_history(conversation_id: int, page: int = 0):
    response = r.get(API_URL + f"messages.getHistory?v=5.199&peer_id={conversation_id}&count={STANDARD_OFFSET}"
                               f"&offset={page * STANDARD_OFFSET}&access_token={VK_API_TOKEN}")
    return response
