class Stock:
    def __init__(self,name,shares,prices) -> None:
        self.name = name 
        self.shares = shares
        self.prices = prices
    def cost(self) -> float:
        return self.shares * self.prices

from dataclasses import dataclass
import typing
from collections import namedtuple
# @dataclass
class newStock():
    Name:str
    Shares:int
    Prices:float

    def Cost(self) -> float:
        return self.Shares*self.Prices
    
newStock1 = namedtuple("newStock",["Name","Shares","Prices"])

def dcost(self)->float:
    return self.Shares * self.Prices

newStock1.Cost =dcost

# s = Stock("AMD",100,18.88)
# cost = s.cost()
# print(f"stockName:{s.name},stockShares:{s.shares},stockPrices:{s.prices},allCost:{cost}")
S = newStock1("Nvdia",300,78.87)

# S.Name = "AMD"
Name,Shares,Prices = S

print("%10s,%10d,%10.2f"% S)

print(f"stockName:{S.Name},stockShares:{S.Shares},stockPrices:{S.Prices},allCost:{S.Cost()}")