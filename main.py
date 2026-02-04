import pandas as pd

# Step 1: Read the Excel files
df_basic = pd.read_excel("employee_basic.xlsx")
df_salary = pd.read_excel("employee_salary.xlsx")

# Step 2: Remove duplicate rows (if any)
df_basic = df_basic.drop_duplicates()
df_salary = df_salary.drop_duplicates()

# Step 3: Merge the two files using Emp_ID
merged_df = pd.merge(df_basic, df_salary, on="Emp_ID", how="inner")

# Step 4: Handle missing values 
merged_df = merged_df.fillna("Not Available")

# Step 5: Save merged output into a new Excel file
merged_df.to_excel("combined_employee.xlsx", index=False)

print("combined_employee.xlsx created successfully!")