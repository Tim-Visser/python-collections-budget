from . import Expense

class BudgetList:
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def append(self, item):
        if item + self.sum_expenses < self.budget:
            self.expenses.append(item)
            self.sum_expenses += item
        else:
            self.overages.append(item)
            self.sum_overages += item

    def __len__(self):
        return len(self.expenses) + len(self.overages)


def __main__():
    myBudgetlist = BudgetList(1200)

    expenses = Expense.Expenses()
    expenses.read_expenses("data/spending_data.csv")

    for expense in expenses.list:
        myBudgetlist.append(expense.amount)

    print("The count of all expenses: " + str(len(myBudgetlist)))


if __name__ == '__main__':
    __main__()
