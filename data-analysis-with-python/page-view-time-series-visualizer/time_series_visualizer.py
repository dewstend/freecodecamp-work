import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

months = pd.Series(
    [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
)

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("./fcc-forum-pageviews.csv", parse_dates=["date"])

df = df.set_index("date")

# Clean data
df = df[
    (df["value"] < df["value"].quantile(0.975))
    & (df["value"] > df["value"].quantile(0.025))
]


def draw_line_plot():
    # Draw line plot
    df_line = df.copy()
    fig = df_line.plot(
        title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
        xlabel="Date",
        ylabel="Page Views",
        figsize=[16, 10],
    ).figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar = (
        df_bar.groupby([df_bar.index.year, df_bar.index.month_name()]).mean().unstack()
    )

    df_bar = df_bar.droplevel(0, axis=1)
    df_bar = df_bar[months]
    df_bar.columns.name = "Months"

    # Draw bar plot
    fig = df_bar.plot(
        kind="bar", figsize=[16, 5], xlabel="Years", ylabel="Average Page Views"
    ).figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box["month"] = pd.DatetimeIndex(df_box["date"]).month_name().str[:3]  # hackish

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(16, 9))

    sns.boxplot(df_box, x="year", y="value", ax=axes[0]).set(
        title="Year-wise Box Plot (Trend)", xlabel="Year", ylabel="Page Views"
    )

    sns.boxplot(
        df_box, x="month", y="value", ax=axes[1], order=months.str.slice(0, 3)
    ).set(
        title="Month-wise Box Plot (Seasonality)", xlabel="Month", ylabel="Page Views"
    )

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
