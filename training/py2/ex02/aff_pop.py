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

    # print(data.head())
    data.plot()
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")
    plt.show()


if __name__ == "__main__":

    # df = pd.DataFrame({'value': ['3.28M']})
    # num = pd.to_numeric(df['value'])
    # print(num)

    main()
