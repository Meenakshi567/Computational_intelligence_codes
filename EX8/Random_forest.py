import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# 1. User input
trees = int(input("Enter number of decision trees: "))

# 2. Load dataset
data = load_breast_cancer()
X = data.data
y = data.target

# 3. Print dataset description
print("\nDataset Description:\n")
print(data.DESCR)

# 4. Splits
splits = [(0.7,0.3), (0.6,0.4), (0.75,0.25)]

results = []

for train, test in splits:

    print("\n--------------------------------------------")
    print(f"Split: {int(train*100)}-{int(test*100)}")

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test, random_state=42)

    print("Train samples:", len(X_train))
    print("Test samples :", len(X_test))

    # 5. Model (Gini used here)
    model = RandomForestClassifier(n_estimators=trees, criterion='gini', random_state=42)
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Confusion Matrix
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

    print("\nConfusion Matrix:")
    print(f"          Predicted 0   Predicted 1")
    print(f"Actual 0     TN= {tn}    FP= {fp}")
    print(f"Actual 1     FN= {fn}    TP= {tp}")

    # Metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("\nAccuracy :", round(acc,4))
    print("Precision:", round(prec,4))
    print("Recall   :", round(rec,4))
    print("F1 Score :", round(f1,4))

    results.append([f"{int(train*100)}-{int(test*100)}", tp, tn, fp, fn, acc, prec, rec, f1])


# 6. Final Table
print("\nFinal Consolidated Results:")
print("Split   TP   TN   FP   FN   Accuracy  Precision  Recall   F1-Score")

for r in results:
    print(f"{r[0]}  {r[1]:3}  {r[2]:3}  {r[3]:3}  {r[4]:3}   {r[5]:.4f}   {r[6]:.4f}   {r[7]:.4f}   {r[8]:.4f}")