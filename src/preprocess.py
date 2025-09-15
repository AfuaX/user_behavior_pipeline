import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print("Loaded data:")
    print(df.head())
    return df

if __name__ == "__main__":
    load_data("../data/user_views.csv")
