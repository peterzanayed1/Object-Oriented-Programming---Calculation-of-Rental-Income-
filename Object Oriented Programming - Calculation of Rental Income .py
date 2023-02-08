class InvestmentBuilding():
    income = []
    expense = []
    downpayment = []

    def _innit_(self,income = [],expense = [],downpayment = []):
        self.income = income
        self.expense = expense
        self.downpayment = downpayment


    def roi(self):
        self.rent = input('What is expected rental income')
        self.laundry = input('What is expected laundry income')
        self.storage = input('What is expected storage income')
        self.misc = input('What is expected misc income')
        self.income.append(int(self.rent))
        self.income.append(int(self.laundry))
        self.income.append(int(self.storage))
        self.income.append(int(self.misc))
        print(f'The total monthly income of this building is {sum(self.income)}')
        self.tax = input('What is expected tax expense')
        self.insurance = input('What is expected insurance expense')
        self.utilities = input('What is expected utilities expense')
        self.hoa = input('What is expected HOA expense')
        self.lawn = input('What is expected lawn/snow expense')
        self.vacancy = input('What is expected vacancy expense')
        self.repairs = input('What is expected repairs expense')
        self.capex = input('What is expected capex expense')
        self.propertymanager = input('What is expected property manager expense')
        self.mortgage = input('What is expected mortgage expense')
        self.expense.append(int(self.tax))
        self.expense.append(int(self.insurance))
        self.expense.append(int(self.utilities))
        self.expense.append(int(self.hoa))
        self.expense.append(int(self.lawn))
        self.expense.append(int(self.vacancy))
        self.expense.append(int(self.repairs))
        self.expense.append(int(self.capex))
        self.expense.append(int(self.propertymanager))
        self.expense.append(int(self.mortgage))
        print(f'The total monthly expenses of this building is {sum(self.expense)}')
        print(f'the total monthly cash flow from this building is {sum(self.income) - sum(self.expense)} ')
        self.downpaymentmade = input('What is the downpayment')
        self.closingcosts = input('What are the closing costs')
        self.rehabbudget = input('What is the rehab budget')
        self.miscother = input('What is the misc/other investment')
        self.downpayment.append(int(self.downpaymentmade))
        self.downpayment.append(int(self.closingcosts))
        self.downpayment.append(int(self.rehabbudget))
        self.downpayment.append(int(self.miscother))
        print(f'your total investment is {sum(self.downpayment)}')
        print(f'your total Roi is {int((sum(self.income) - sum(self.expense)) * 12 / sum(self.downpayment) * 100)}%')

        



building = InvestmentBuilding()

print(building.roi())
