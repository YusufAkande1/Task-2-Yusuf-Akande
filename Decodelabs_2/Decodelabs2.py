import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# LOAD DATASET
df = pd.read_excel("Data_Analytics.xlsx")

# VIEW DATASET INFORMATION
print(df.info())

# GENERATE STATISTICAL SUMMARY
print(df.describe())

# CHECK UNIQUE VALES
print(df["PaymentMethod"].unique())

print(df["OrderStatus"].value_counts())

# ANALYZE SALES
# Total Revenue
print(df["TotalPrice"].sum())

# Average Revenue
print(df["TotalPrice"].mean())

# Highest Sale
print(df["TotalPrice"].max())

# Top Selling Products
top_products = df["Product"].value_counts()

print(top_products)

# Top Selling Products Bar Chart
top_products = df["Product"].value_counts().head(10)

top_products.plot(kind="bar")

plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)
plt.savefig("Decodelabs_Visualizations/Top Selling Products.png",
            dpi=300,
            bbox_inches="tight"
)
plt.show()

# Order Status Distribution
df["OrderStatus"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Order Status Distribution")

plt.ylabel("")
plt.savefig("Decodelabs_Visualizations/Order Status Distribution",
            dpi=300,
            bbox_inches="tight"
)
plt.show()

# Payment Method Analysis
df["PaymentMethod"].value_counts().plot(
    kind="bar"
)

plt.title("Payment Methods Used")

plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.savefig("Decodelabs_Visualizations/Payment Method",
            dpi=300,
            bbox_inches="tight"
)
plt.show()

# MONTHLY SALES TREND
df["Month"] = df["Date"].dt.month_name()

# Monthly Revenue
monthly_sales = df.groupby("Month")["TotalPrice"].sum()

print(monthly_sales)
# Plot Monthly Revenue
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.savefig("Decodelabs_Visualizations/Monthly Sales Trend",
            dpi=300,
            bbox_inches="tight"
)
plt.show()
# CORRELATION ANALYSIS
correlation = df.corr(numeric_only=True)

print(correlation)

plt.show()

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Correlation Matrix")
plt.savefig("Decodelabs_Visualizations/Correlation Matrix",
            dpi=300,
            bbox_inches="tight"
            )
plt.show()

# Detect Outliers

plt.boxplot(df["TotalPrice"])

plt.title("TotalPrice Outliers")

plt.savefig("Decodelabs_Visualizations/TotalPrice Outliers",
            dpi=300,
            bbox_inches="tight"
)
plt.show()

# SAVE EXPLORATORY DATA ANALYSIS RESULT
top_products.to_excel(
    "Top_Products.xlsx"
)