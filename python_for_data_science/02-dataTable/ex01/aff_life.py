from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():
    '''
    Load data from fixed file and displa
    the population growth chart for Switserland
    '''
    data: pd.DataFrame = load("../doc/life_expectancy_years.csv")
    if data is None:
        print("Error with loading file")
        exit(1)
    if ('country' not in data.columns or
            'Switzerland' not in data['country'].unique()):
        print("Error: Data does not have a country or Switzerland field")
        exit(1)

    data = data.set_index("country").T
    print(data.head())
    data["Switzerland"].plot()
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.title("Switzerland Life expectancy Projections")
    plt.show()


if __name__ == "__main__":
    main()
