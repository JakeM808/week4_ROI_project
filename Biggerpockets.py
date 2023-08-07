# Income: 
# Rental Income = $2000
# Laundry = 0
# Storage = 0
# Misc = 0

# Total Monthly Income = $2000

# Expenses:

# Tax: $150
# Insurance: $100
# Utilities: $0
# HOA: $0
# Lawn/Snow: $0
# Vacancy: $100
# Repairs: $100
# CapEx: $100
# Property Manage: $200
# Mortgage: $860

# Total Monthly Expenses: $1610

# Cash Flow:
# Income - Expenses = Cash Flow
# 2000 - 1610 = $390

# Cash on Cash ROI:
# Down Payment: $40000
# Closting: $3000
# Rehad Budget: $7000
# Misc:

# TOtal Investment: $50000

# Annual Cash Flow = monthly cash flow * 12
# 390 * 12 = 4680 

# Annual Cash Flow / Total Investment  = 9.36%

# Cash on Cash ROI = 9.36%




print("Enter down payment:")
down_payment = float(input())

print("Enter closing costs:")  
closing_costs = float(input())

print("Enter rehab budget:")
rehab_budget = float(input())

print("Enter misc costs:")
misc_costs = float(input())

print("Enter rental income:")
rental_income = float(input())

print("Enter storage income")
storage_income = float(input())

print("Enter misc income")
misc_income = float(input())

print("Enter taxes:")
tax_expense = float(input())

print("Enter insurance:")
insurance_expense = float(input())

# print("Enter income:")
# total_expense = float(input())

# print("Enter expense:")
# total_income = float(input())


class PropertyInvestment:
    def __init__(self, down_payment, closing_cost, rehab_budget, misc_costs, rental_income, storage_income, misc_income, tax_expense, insurance_expense):
    
        self.down_payment = down_payment
        self.closing_cost = closing_cost
        self.rehab_budget = rehab_budget
        self.misc_costs = misc_costs
        self.rental_income = rental_income
        self.storage_income = storage_income
        self.misc_income = misc_income
        self.tax_expense = tax_expense
        self.insurance_expense = insurance_expense
        

    def total_income(self):
        return self.rental_income + self.storage_income + self.misc_income
    
    def total_expense(self):
        return self.tax_expense + self.insurance_expense
        
    def calc_cash_flow(self):
        return self.total_income() - self.total_expense()

    def total_investment(self):
        return self.down_payment + self.closing_cost + self.rehab_budget + self.misc_costs

    def calculate_roi(self):
        annual_cash_flow = self.calc_cash_flow() * 12
        total_investment = self.total_investment()
        return annual_cash_flow / total_investment * 100
        


property = PropertyInvestment(down_payment, closing_costs, rehab_budget, misc_costs, rental_income, storage_income, misc_income, tax_expense, insurance_expense)
roi = property.calculate_roi()
        
print(f"Cash on Cash ROI: {roi:.2f}%")  

