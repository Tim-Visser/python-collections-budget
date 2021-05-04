from . import Expense
import matplotlib.pyplot as plt


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

    def __iter__(self):
        self.iter_e = iter(self.expenses)
        self.iter_o = iter(self.overages)
        return self

    def __next__(self):
        try:
            return next(self.iter_e)
        except StopIteration as stop:
            return next(self.iter_o)


def main():
    myBudgetlist = BudgetList(1200)

    expenses = Expense.Expenses()
    expenses.read_expenses("data/spending_data.csv")

    for expense in expenses.list:
        myBudgetlist.append(expense.amount)

    print("The count of all expenses: " + str(len(myBudgetlist)))

    for entry in myBudgetlist:
        print(entry)

    fig, ax = plt.subplots()
    labels = ["Expenses", "Overages", "Budget"]
    values = [myBudgetlist.sum_expenses, myBudgetlist.sum_overages, myBudgetlist.budget]
    ax.set_title("Total expenses vs total budget")
    ax.bar(labels, values, color=["green", "red", "blue"])

    plt.show()

if __name__ == '__main__':
    main()
