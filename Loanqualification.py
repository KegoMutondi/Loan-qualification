# Function to determine loan eligibility
def check_loan_eligibility(age, income):
    if age >= 21 and income >= 21000:
        return "Congratulations, you qualify for a loan."
    else:
        return "Unfortunately, we are unable to offer you a loan at this time."

# Prompt the user for age and income
age = int(input("Enter your age: "))
income = float(input("Enter your annual income (in Sh): "))

# Check loan eligibility
result = check_loan_eligibility(age, income)

# Print the result
print(result)
