# Bayes Theorem Calculator

# Input from user
P_A = float(input("Enter P(A): "))
P_B = float(input("Enter P(B): "))
P_B_given_A = float(input("Enter P(B|A): "))

# Check to avoid division by zero
if P_B == 0:
    print("P(B) cannot be zero!")
else:
    # Apply Bayes theorem
    P_A_given_B = (P_B_given_A * P_A) / P_B

    # Output
    print(f"\nP(A|B) = {P_A_given_B:.4f}")