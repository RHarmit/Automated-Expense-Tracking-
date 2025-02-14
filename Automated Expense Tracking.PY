import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Expense Data
data = {
    "Date": pd.date_range(start='2023-01-01', periods=10, freq='D'),
    "Description": ["Uber Ride", "Walmart Purchase", "Restaurant Bill", "Gas Station", "Netflix Subscription", "Flight Ticket", "Grocery Store", "Electricity Bill", "Amazon Order", "Gym Membership"],
    "Amount": np.random.randint(10, 200, size=10)
}

df = pd.DataFrame(data)

# Expense Categories
categories = {
    "Transport": ["Uber", "Flight", "Gas"],
    "Groceries": ["Walmart", "Grocery"],
    "Entertainment": ["Netflix", "Amazon", "Restaurant"],
    "Utilities": ["Electricity"],
    "Fitness": ["Gym"]
}

def categorize_expenses(description):
    for category, keywords in categories.items():
        if any(keyword in description for keyword in keywords):
            return category
    return "Other"

df["Category"] = df["Description"].apply(categorize_expenses)

def generate_summary_report(df):
    summary = df.groupby("Category")["Amount"].sum().reset_index()
    print("\nExpense Summary Report:")
    print(summary)
    df.to_csv("expense_report.csv", index=False)
    print("\nReport saved as 'expense_report.csv'")
    
    # Visualizing Expenses by Category
    plt.figure(figsize=(8,5))
    sns.barplot(x='Amount', y='Category', data=summary, palette='viridis')
    plt.xlabel('Total Amount ($)')
    plt.ylabel('Category')
    plt.title('Expense Distribution by Category')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()

    # Monthly Spending Trend
    plt.figure(figsize=(8,5))
    df.groupby("Date")["Amount"].sum().plot(marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Total Daily Expenses ($)')
    plt.title('Daily Expense Trend')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

# Run Categorization & Report
generate_summary_report(df)
