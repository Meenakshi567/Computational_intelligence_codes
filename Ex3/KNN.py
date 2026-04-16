import csv
import math
from collections import Counter

# -------- DISTANCE CALCULATION FUNCTIONS --------
def euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def manhattan_distance(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

# -------- DYNAMIC MIN-MAX NORMALIZATION --------
def normalize(data, test_point):
    num_features = len(test_point)
    num_records = len(data)
    normalized_data = [[] for _ in range(num_records)]
    normalized_test = []

    for i in range(num_features):
        col_values = [row[i] for row in data]
        min_val, max_val = min(col_values), max(col_values)
        # Normalization Formula: (Value - Min) / (Max - Min)
        range_val = (max_val - min_val) if max_val != min_val else 1.0

        for j in range(num_records):
            val = (data[j][i] - min_val) / range_val
            normalized_data[j].append(round(val, 4))

        t_val = (test_point[i] - min_val) / range_val
        normalized_test.append(round(t_val, 4))
    return normalized_data, normalized_test

# -------- LOAD DATASET --------
def load_dataset(filename):
    data, labels = [], []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if not row: continue
                # Converting features to float for math operations
                data.append(list(map(float, row[:-1])))
                labels.append(row[-1])
                if len(data) == 100: break
        return data, labels
    except Exception as e:
        print(f"Error: {e}")
        return None, None

# -------- MAIN PROGRAM --------
print("--- KNN Classifier (Normalization & Multi-Voting) ---")
filename = input("Enter dataset CSV file name: ")
raw_data, raw_labels = load_dataset(filename)
print("This dataset represents Smartphone Specifications:Feature 1: CPU Speed (GHz)\nFeature 2: RAM (GB)\nFeature 3: Battery (mAh / 1000)\n Label (4th): Category (Budget, Mid-Range, Flagship)")
if raw_data:
    num_features = len(raw_data[0])
    test_pt = []
    print(f"\nDetected {num_features} features. Enter test point values:")
    for i in range(num_features):
        test_pt.append(float(input(f" Feature {i+1}: ")))

    # 1. Normalize
    norm_train, norm_test = normalize(raw_data, test_pt)

    # 2. PRINT NORMALIZED TABLE
    print("\n" + "="*20 + " TABLE 1: NORMALIZED RECORDS " + "="*20)
    feat_headers = " | ".join([f"Feat {i+1:<5}" for i in range(num_features)])
    print(f"{'ID':<4} | {feat_headers} | {'Label'}")
    print("-" * (15 + (num_features * 10)))
    for i in range(len(norm_train)):
        row_vals = " | ".join([f"{v:<8}" for v in norm_train[i]])
        print(f"{i+1:<4} | {row_vals} | {raw_labels[i]}")

    # 3. Choose Distance Metric
    print("\nSelect Distance Metric for Calculation:")
    print("1. Euclidean Distance")
    print("2. Manhattan Distance")
    dist_choice = input("Enter choice (1 or 2): ")

    # 4. Calculate Distances
    results = []
    for i in range(len(norm_train)):
        dist = manhattan_distance(norm_train[i], norm_test) if dist_choice == '2' else euclidean_distance(norm_train[i], norm_test)
        results.append({
            'id': i+1,
            'dist': round(dist, 4),
            'label': raw_labels[i],
            'features': norm_train[i] # Stored for the final record print
        })

    # Sort results by distance to determine Ranks
    results.sort(key=lambda x: x['dist'])

    # 5. Print Ranked Table
    metric_name = "Manhattan" if dist_choice == '2' else "Euclidean"
    print(f"\n--- TABLE 2: RANKED DISTANCES ({metric_name}) ---")
    print(f"{'Rank':<6} | {'ID':<5} | {'Distance':<10} | {'Label'}")
    print("-" * 45)
    for rank, item in enumerate(results, 1):
        print(f"{rank:<6} | {item['id']:<5} | {item['dist']:<10} | {item['label']}")

    # 6. Get K & Print K Records
    k = int(input("\nEnter value of K: "))
    k_nearest = results[:k]

    print(f"\n--- TOP {k} NEAREST NEIGHBOR RECORDS ---")
    print(f"{'Rank':<5} | {'ID':<4} | {'Features':<25} | {'Dist':<10} | {'Label'}")
    for rank, item in enumerate(k_nearest, 1):
        # Corrected Indentation for record printing
        feat_str = " | ".join([f"{v:<6}" for v in item['features']])
        print(f"{rank:<5} | {item['id']:<4} | {feat_str:<25} | {item['dist']:<10} | {item['label']}")

    # 7. Calculate Both Voting Methods (Corrected Indentation)
    # Unweighted Logic: Simple majority
    votes = [n['label'] for n in k_nearest]
    unweighted_counts = Counter(votes)

    # Weighted Logic: 1/distance
    class_weights = {}
    for n in k_nearest:
        # Distance weight calculation using 1/d formula
        weight = 1 / n['dist'] if n['dist'] != 0 else 10000.0
        class_weights[n['label']] = class_weights.get(n['label'], 0) + weight

    # Final Comparison Print
    print("\n" + "#"*50)
    print(f" FINAL RESULTS (K={k})")
    print("#"*50)
    print(f"UNWEIGHTED WINNER: ** {unweighted_counts.most_common(1)[0][0]} ** {dict(unweighted_counts)}")
    print(f"WEIGHTED WINNER:   ** {max(class_weights, key=class_weights.get)} ** " + str({key: round(val, 2) for key, val in class_weights.items()}))
    print("#"*50)