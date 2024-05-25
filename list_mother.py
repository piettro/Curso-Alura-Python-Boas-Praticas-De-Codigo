from typing import List

from constants import LEN_MAX_DEFAULT, LEN_MIN_DEFAULT

class MotherList():
    code: int = 0
    current_password: str = ''
    clients_served: List[str] = []
    norm_list: List[str] = []

    def reset_list(self) -> None:
        if self.code >= LEN_MAX_DEFAULT:
            self.code = LEN_MIN_DEFAULT
        else:
            self.code += 1

    def insert_client(self) -> None:
        self.norm_list.append(self.current_password)

    def update_list(self) -> None:
        self.reset_list()
        self.generate_current_password()
        self.insert_client()

    def call_client(self, desk: int) -> str:
        current_client = self.norm_list.pop(0)
        self.clients_served.append(current_client)

        return f'Current Client: {current_client}, go to desk:{desk}'

    def generate_current_password(self) -> None:
        ...
