from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():
    '''
    Load data from fixed files and display
    the population for Switserland and Eswatini
    '''
    income: pd.DataFrame = load(
        "../doc/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy: pd.DataFrame = load(
        "../doc/life_expectancy_years.csv")
    if income is None or life_expectancy is None:
        print("Error with loading files")
        exit(1)

    income = income.loc[:, ['country', '1900']]
    life_expectancy = life_expectancy.loc[:, ['country', '1900']]
    data = pd.merge(income, life_expectancy, on="country")
    data.rename(columns={"1900_x": "GDP", "1900_y": "LE"},
                inplace=True)
    data = data.set_index("country")
    print(data.head())
    data["GDP"].replace({'[kK]': '*1e3', '[mM]': '*1e6', '[bB]': '*1e9', },
                        regex=True).map(pd.eval)

    # print(data.head())
    plt.scatter(data["GDP"], data["LE"])
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")
    plt.show()


if __name__ == "__main__":
    main()
