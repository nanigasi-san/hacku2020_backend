class StockData:
    pass

class Standings:
    def __init__(self, contest_name: str):
        pass

class Contest:
    def __init__(self, contest_name: str, period: tuple, stock_data: StockData):
        self.period = period
        self.stock_data = stock_data
        self.standings = Standings(contest_name)
