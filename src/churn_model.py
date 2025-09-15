# src/churn_model.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import os

# Make sure output folder exists
os.makedirs("output", exist_ok=True)

# 1. Load dataset
data = pd.read_csv("data/user_behavior.csv")
print("Dataset loaded successfully!")
print(data.head())

# 2. Split features and target
X = data.drop("churn", axis=1)
y = data["churn"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Train Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 4. Predictions & Evaluation
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(f"\n Accuracy: {acc:.2f}")
print("\n Classification Report:\n", classification_report(y_test, y_pred))

# Save classification report to file
with open("output/classification_report.txt", "w") as f:
    f.write(classification_report(y_test, y_pred))

# 5. Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["No Churn", "Churn"],
            yticklabels=["No Churn", "Churn"])
plt.title("Confusion Matrix")
plt.savefig("output/confusion_matrix.png")
plt.close()

# Histogram of a feature (example: session_time)
plt.figure(figsize=(6, 4))
plt.hist(data["session_time"], bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of Session Time")
plt.xlabel("Session Time")
plt.ylabel("Count")
plt.savefig("output/user_behavior_hist.png")
plt.close()

print("\nOutputs saved in /output folder!")
