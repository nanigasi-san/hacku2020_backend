from typing import NamedTuple
from datetime import datetime


class Period(NamedTuple):
    start: datetime
    finish: datetime


class StockData:
    def __init__(self):
        self.data_path = ""


class Standings:
    def __init__(self, contest_name: str):
        pass


class Contest:
    def __init__(self, contest_name: str, period: Period, stock_data: StockData):
        self.contest_name = contest_name
        self.period = period
        self.stock_data = stock_data
        self.standings = Standings(contest_name)
