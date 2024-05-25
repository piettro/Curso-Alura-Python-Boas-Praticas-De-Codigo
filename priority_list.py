from list_mother import MotherList
from constants import CODE_PRIORITARY

class PriorityList(MotherList):
    def generate_current_password(self) -> None:
        self.current_password = f'{CODE_PRIORITARY}{self.code}'

    def statistics(self, day: int, agency: int, flag: str) -> dict:
        statistic: dict = {}

        if flag == 'detail':
            statistic['day'] = day
            statistic['agency'] = agency
            statistic['served_clients'] = self.clients_served
            statistic['quantity_served_clients'] = len(self.clients_served)

        return statistic
