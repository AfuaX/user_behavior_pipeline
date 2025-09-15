# src/generate_data.py
from sklearn.datasets import make_classification
import pandas as pd
import os

# Generate synthetic classification dataset
X, y = make_classification(
    n_samples=500,
    n_features=5,
    n_informative=3,
    n_redundant=1,
    random_state=42
)

# Define columns for user behavior
columns = [
    "login_count",
    "session_time",
    "purchases",
    "support_tickets",
    "days_since_last_login"
]

# Create DataFrame
data = pd.DataFrame(X, columns=columns)
data["churn"] = y  # target column

# Ensure 'data' folder exists relative to project root
project_root = os.path.join(os.path.dirname(__file__), "..")
data_folder = os.path.join(project_root, "data")
os.makedirs(data_folder, exist_ok=True)

# Save dataset in the correct folder
output_path = os.path.join(data_folder, "user_behavior.csv")
data.to_csv(output_path, index=False)

print(f"✅ Synthetic dataset saved at {output_path}")
