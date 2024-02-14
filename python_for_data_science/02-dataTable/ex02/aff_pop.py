from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():
    '''
    Load data from fixed file and display
    the population for Switserland and Eswatini
    '''
    data: pd.DataFrame = load("../doc/population_total.csv")
    if data is None:
        print("Error with loading file")
        exit(1)
    if ('country' not in data.columns or
            'Switzerland' not in data['country'].unique() or
            'Eswatini' not in data['country'].unique()):
        print("Error: Data does not have country/s field")
        exit(1)

    data = data.set_index("country").T
    data = data.loc['1800':'2050', ["Switzerland", "Eswatini"]].replace(
        {'[kK]': '*1e3', '[mM]': '*1e6', '[bB]': '*1e9', },
        regex=True).map(pd.eval)

    def yaxis_formatter(y, pos) -> str:
        '''Formats the population data to be human readable'''
        units = ["", "K", "M", "B"]
        power = 0
        while abs(y) >= 1000 and power < 3:
            y /= 1000
            power += 1
        return f"{y:.0f}{units[power]}"

    data.plot()

    plt.gca().yaxis.set_major_formatter(yaxis_formatter)

    plt.locator_params(axis="y", nbins="5")
    ticks = plt.gca().yaxis.get_major_ticks()
    ticks[1].set_visible(False)
    ticks[-2].set_visible(False)

    plt.legend(loc="lower right", title="")

    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")
    plt.show()


if __name__ == "__main__":

    main()
