from list_mother import MotherList
from constants import CODE_NORM


class NormList(MotherList):
    def generate_current_password(self) -> None:
        self.current_password = f'{CODE_NORM}{self.code}'
