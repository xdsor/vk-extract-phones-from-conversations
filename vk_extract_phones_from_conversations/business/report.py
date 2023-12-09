import csv
from typing import Set

from vk_extract_phones_from_conversations.domain.models import GroupMember


def create_csv_report(conversations: Set[GroupMember]):
    with open("report.csv", "w") as f:
        writer = csv.writer(f)
        headers = ["Имя", "Фамилия", "Телефон", "Пол"]
        writer.writerow(headers)
        for conversation in conversations:
            data = [conversation.first_name, conversation.last_name, conversation.phone_number, conversation.sex]
            writer.writerow(data)
