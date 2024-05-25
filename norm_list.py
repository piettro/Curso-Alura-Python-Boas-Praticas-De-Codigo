from list_mother import MotherList


class NormList(MotherList):
    def generate_current_password(self) -> None:
        self.current_password = f'NM{self.code}'
