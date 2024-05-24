from norm_list import NormList

class PriorityList(NormList):
    def generate_current_password(self) -> None:
        self.current_password = f'PR{self.code}'
    
    def update_list(self) -> None:
        self.reset_list()
        self.generate_current_password()
        self.norm_list.append(self.current_password)

    def statistics(self, day: str, agency:int, flag: str) -> dict:
        if flag != 'detail':
            statistic = f''
        else:
            statistic ={}
            statistic['day'] = day
            statistic['agency'] = agency
            statistic['served_clients'] = self.clients_served
            statistic['quantity_served_clients'] = len(self.clients_served)

        return statistic