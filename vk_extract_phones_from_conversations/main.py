import os

from vk_extract_phones_from_conversations.business import conversations
from vk_extract_phones_from_conversations.business.report import create_csv_report
from vk_extract_phones_from_conversations.utils.requests_cache_decorator import CACHE_DIR


def main():
    init()
    members = conversations.collect_members_from_conversations()
    conversations.fill_phone_numbers(members)
    create_csv_report(members)


def init():
    if not os.getenv("VK_API_TOKEN"):
        raise Exception("No VK_API_TOKEN environment variable set.")
    if not os.path.exists(CACHE_DIR):
        os.mkdir(CACHE_DIR)


if __name__ == "__main__":
    main()
