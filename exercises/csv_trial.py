import csv
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def draw_graph(data):

    dates = [d[1] for d in data]
    cases = [float(d[2])/10 for d in data]
    rates = [d[4] for d in data]

    fig, ax = plt.subplots()
    ax.plot(dates, cases, label="cases x 10")
    ax.plot(dates, rates, label="rates")

    # Major ticks every 6 months.
    fmt_half_year = mdates.MonthLocator(interval=6)
    ax.xaxis.set_major_locator(fmt_half_year)

    # Minor ticks every month.
    fmt_month = mdates.MonthLocator()
    ax.xaxis.set_minor_locator(fmt_month)

    # Text in the x axis will be displayed in 'YYYY-mm' format.
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # Round to nearest years.
    datemin = dates[-1]
    datemax = dates[0]
    ax.set_xlim(datemin, datemax)

    # Format the coords message box, i.e. the numbers displayed as the cursor moves
    # across the axes within the interactive GUI.
    ax.format_xdata = mdates.DateFormatter('%Y-%m')
    ax.format_ydata = lambda x: f'${x:.2f}'  # Format the price.
    ax.grid(True)

    # Rotates and right aligns the x labels, and moves the bottom of the
    # axes up to make room for them.
    fig.autofmt_xdate()
    plt.legend()
    plt.show()


def main():
    with open("data.csv", newline="") as file:
        reader = csv.reader(file)

        header = next(reader)
        data = []
        for row in reader:
            date = datetime.strptime(row[0], "%d/%m/%Y")
            cases = int(row[4])
            deaths = int(row[5])
            country = row[6]
            rate_per_mil = float(row[11]) if row[11] else None
            data.append((country, date, cases, deaths, rate_per_mil))

    print(header)
    print(len(data), "rows")
    print(data[:3])

    ro_data = [row for row in data if row[0] == "Romania"]

    for row in ro_data[:10]:
        print(row)

    draw_graph(ro_data)


if __name__ == '__main__':
    main()
