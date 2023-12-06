import math


def get_title(
    name,
):
    title_stars_total = 30 - len(name)
    title_stars_left_side = math.floor(title_stars_total / 2) * "*"
    title_stars_right_side = (title_stars_total - len(title_stars_left_side)) * "*"

    return title_stars_left_side + str(name) + title_stars_right_side


def get_tab_entry_string(
    description, amount, string_1_size_limit=23, max_total_size=30
):
    string_1_truncated = description[:string_1_size_limit].ljust(string_1_size_limit)
    string_2_truncated = str("{:.2f}".format(amount))

    whitespace = (
        max_total_size - len(string_1_truncated) - len(string_2_truncated)
    ) * " "

    return string_1_truncated + whitespace + string_2_truncated


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def __str__(self):
        title = get_title(self.name)

        tab_entries = [
            get_tab_entry_string(tab_entry["description"], tab_entry["amount"])
            for tab_entry in self.ledger
        ]

        total = f"Total: {self.balance}"
        return "\n".join([title, *tab_entries, total])

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        return amount <= self.balance

    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        self.balance -= amount
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True


# TODO
def create_spend_chart(categories):
    title = "Percentage spent by category"

    expenditures = 0

    # calculate total expenditures by category
    # iterate over each category
    #### filter by withdrawals
    #### add them all up

    # reduce expenditures list to a sum
    total_expenditure = 0

    # map over expenditures and get list of percentages
    #### do: divide each expenditure ...
    category_percentages = 0

    return title
