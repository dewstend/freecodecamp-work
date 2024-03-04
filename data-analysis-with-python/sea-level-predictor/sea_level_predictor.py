import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    _, (ax) = plt.subplots()
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], marker=".")

    # Create first line of best fit
    m, b, *_ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    extended_years = np.arange(df["Year"].min(), 2051, 1)

    ax.plot(extended_years, m * extended_years + b, "-y", label="Trend")

    # Create second line of best fit
    recent_df = df[df["Year"] >= 2000]

    m, b, *_ = linregress(recent_df["Year"], recent_df["CSIRO Adjusted Sea Level"])

    years = np.arange(2000, 2051, 1)

    ax.plot(years, m * years + b, "-r", label="Trend since 2000s")
    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
