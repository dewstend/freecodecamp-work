import math

from util import floor_to_base, generate_whitespace_chart


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


def create_spend_chart(categories):
    title = "Percentage spent by category"

    category_expenditures = []
    longest_category_name = ""

    for i, category in enumerate(categories):
        if len(category.name) > len(longest_category_name):
            longest_category_name = category.name

        category_expenditures.append(0)
        for entry in category.ledger:
            if entry["amount"] < 0:
                category_expenditures[i] += abs(entry["amount"])

    total_expenditure = sum(category_expenditures)

    # Multiples of 10
    category_percentages = []

    for category_expenditure in category_expenditures:
        bar_percentage = floor_to_base(category_expenditure / total_expenditure * 100)
        category_percentages.append(bar_percentage)

    len_categories = len(categories)

    chart_width = 5 + (len_categories * 3)
    chart_height = 12 + len(longest_category_name)

    chart = generate_whitespace_chart(chart_width, chart_height)

    # convert char matrix into string
    def get_chart_text():
        return "\n".join(["".join(row) for row in chart])

    # draw percentage labels
    for i, percentage in enumerate(range(100, -10, -10)):
        percentage_text = f"{percentage}| "
        text_length = len(percentage_text)

        chart[i][5 - text_length : 5] = list(percentage_text)

    # draw horizontal rule
    chart[11] = list(f'    -{"-" * (3 * len_categories)}')

    # draw categories and bars
    for i, category_percentage in enumerate(category_percentages):
        # how many 'o's we'll need to draw (label 0 = 1, label 50 = 6)
        percentage_label_count = int((category_percentage / 10) + 1)

        # draw each 'o' for this bar
        for j in range(percentage_label_count):
            column_index = 3 * i
            chart[10 - j][5 + column_index] = "o"

        # draw each letter for this category name
        for j, char in enumerate(categories[i].name):
            column_index = 3 * i
            chart[12 + j][5 + column_index] = char

    # append title
    chart = [list(title), *chart]

    return get_chart_text()
