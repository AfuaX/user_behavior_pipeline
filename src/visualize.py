import pandas as pd
import matplotlib.pyplot as plt

def plot_data(path):
    df = pd.read_csv(path)
    churned = df[df['churn'] == 1]['views']
    active = df[df['churn'] == 0]['views']
    plt.hist([churned, active], bins=10, label=['Churned','Active'])
    plt.legend()
    plt.xlabel("Views")
    plt.ylabel("Count")
    plt.title("User Behavior Distribution")
    plt.show()

if __name__ == "__main__":
    plot_data("../data/user_views.csv")
