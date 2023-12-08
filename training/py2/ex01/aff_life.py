from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():
    '''
    Load data from fixed file and displa
    the population growth chart for Switserland
    '''
    data: pd.DataFrame = load("../doc/life_expectancy_years.csv")
    assert data is not None, "Error with datafile.csv"

    data = data.set_index("country").T
    print(data.head())
    data["Switzerland"].plot()
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.title("Switzerland Life expectancy Projections")
    plt.show()


if __name__ == "__main__":
    main()
