class CouponBond:
    def __init__(self,principal,interest_rate,maturity,market_interest_rate):
        self.principal = principal
        self.interest_rate = interest_rate/100
        self.maturity = maturity
        self.market_interest_rate = market_interest_rate/100

    def present_value(self,x,n):
        return x/(1+self.market_interest_rate)**n

    def calculate_price(self):
        price = 0
        for t in range(1,self.maturity+1):
            price = price + self.present_value(self.interest_rate*self.principal,t)

        price = price + self.present_value(self.principal,self.maturity)

        return price

if __name__ == "__main__":
    bond = CouponBond(1000, 10, 3, 4)
    print(bond.calculate_price())