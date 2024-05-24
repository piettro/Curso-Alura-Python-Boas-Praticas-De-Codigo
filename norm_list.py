
class NormList():
    code: int = 0
    current_password: str = ''
    clients_served = []
    norm_list = []

    def reset_list(self) -> None:
        if self.code >= 100:
            self.code = 0
        else:
            self.code += 1

    def generate_current_password(self) -> None:
        self.current_password = f'NM{self.code}'

    def update_list(self) -> None:
        self.reset_list()
        self.generate_current_password()
        self.norm_list.append(self.current_password)

    def call_client(self, desk:int) -> str:
        current_client = self.norm_list.pop(0)
        self.clients_served.append(current_client)

        return f'Current Client: {current_client}, go to desk:{desk}'