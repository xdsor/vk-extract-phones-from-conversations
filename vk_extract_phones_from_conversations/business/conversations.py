from typing import Set

from vk_extract_phones_from_conversations.api import vk_api
from vk_extract_phones_from_conversations.business.phone_number_parser import try_to_parse_phone_number
from vk_extract_phones_from_conversations.domain.models import GroupMember


def collect_members_from_conversations() -> Set[GroupMember]:
    conversations_response = vk_api.get_conversations()["response"]
    unreached_conversations = conversations_response["count"] - len(conversations_response["profiles"])
    group_members = {GroupMember(x["id"], x["first_name"], x["last_name"], x["sex"]) for x in conversations_response["profiles"]}
    current_page = 1
    while unreached_conversations > 0:
        conversations_response = vk_api.get_conversations(current_page)["response"]
        unreached_conversations -= len(conversations_response["profiles"])
        group_members.update(
            {GroupMember(x["id"], x["first_name"], x["last_name"], x["sex"]) for x in conversations_response["profiles"]})
        current_page += 1
    return group_members


def fill_phone_numbers(group_members: Set[GroupMember]):
    for group_member in group_members:
        history_response = vk_api.get_history(group_member.member_id)["response"]
        unreached_messages = history_response["count"] - len(history_response["items"])
        messages = []
        for message in history_response["items"]:
            if message["from_id"] != group_member.member_id:
                continue
            messages.append(message["text"])
        current_page = 1
        while unreached_messages > 0:
            history_response = vk_api.get_history(group_member.member_id, current_page)["response"]
            unreached_messages -= len(history_response["items"])
            for message in history_response["items"]:
                if message["from_id"] != group_member.member_id:
                    continue
                messages.append(message["text"])
            current_page += 1

        for message in messages:
            phone_number = try_to_parse_phone_number(message)
            if phone_number is not None:
                group_member.phone_number = phone_number
                break
