from vk_extract_phones_from_conversations.business.phone_number_parser import format_phone


class GroupMember:

    def __init__(self, member_id, first_name, last_name, sex):
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self._phone_number = None
        self.sex = "Жен" if sex == 1 else "Муж"

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        formatted = format_phone(value)
        self._phone_number = formatted if len(formatted) == 11 else None

    def __str__(self):
        return (f'GroupMember('
                f'member_id={self.member_id}, '
                f'first_name={self.first_name}, '
                f'last_name={self.last_name}, '
                f'phone_number={self.phone_number})')

    def __repr__(self):
        return (f'GroupMember('
                f'member_id={self.member_id}, '
                f'first_name={self.first_name}, '
                f'last_name={self.last_name}, '
                f'phone_number={self.phone_number})')

    def __eq__(self, other):
        if isinstance(other, GroupMember):
            return self.member_id == other.member_id
        return False

    def __hash__(self):
        return hash(self.member_id)
