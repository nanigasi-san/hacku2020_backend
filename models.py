class User:
    def __init__(self, id: int, password: str):
        self.id = id
        self.__password = password


class StockData:
    pass

class Standings:
    def __init__(self, contest_name: str):
        pass

class Contest:
    def __init__(self, contest_name: str, period: tuple, stock_data: StockData):
        self.period = period
        self.__stock_data = stock_data
        self.standings = Standings(contest_name)
