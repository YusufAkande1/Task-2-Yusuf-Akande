# Exploratory Data Analysis (EDA) Project

## Project Overview
This project focuses on performing Exploratory Data Analysis (EDA) on a cleaned sales dataset using Python.

The goal of the analysis was to explore the dataset, identify patterns, detect trends, and generate business insights that can support data-driven decision-making.

EDA plays a critical role in understanding data before building dashboards, reports, or machine learning models.

---

## Objectives

The objectives of this project were to:

- Understand the structure of the dataset
- Analyze sales performance
- Identify top-selling products
- Explore customer purchasing behavior
- Examine payment methods and order status
- Visualize trends and patterns
- Generate business insights from the data

---

## Tools & Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Excel
- PyCharm

---

## Dataset Description

The dataset contains sales transaction information including:

- Order ID
- Date
- Customer ID
- Product
- Quantity
- Unit Price
- Payment Method
- Order Status
- Coupon Code
- Referral Source
- Total Price

---

## Exploratory Data Analysis Process

### 1. Loading the Dataset

The cleaned dataset was imported using Pandas.

#### Example:

```python
import pandas as pd

df = pd.read_excel(
    "Cleaned_Dataset.xlsx",
    engine="openpyxl"
)
```
### 2. Understanding the Dataset

Basic dataset exploration was performed to understand:

- Number of rows and columns
- Data types
- Missing values

#### Example:
```
print(df.info())

#Dataset dimensions:

print(df.shape)
```
### 3. Statistical Summary

Descriptive statistics were generated for numerical columns.

#### Example:
```
print(df.describe())
```
This provided insights into:

- Mean
- Minimum values
- Maximum values
- Standard deviation

### 4. Product Analysis

Top-selling products were identified using value counts.

#### Example:
```
top_products = df["Product"].value_counts()

print(top_products)
```
### 5. Revenue Analysis

Revenue-related analysis was performed to understand:

- Total revenue
- Average revenue
- Highest sales value

#### Example:
```
print(df["TotalPrice"].sum())
```
### 6. Payment Method Analysis

Customer payment preferences were analyzed.

#### Example:
```
print(df["PaymentMethod"].value_counts())
```
### 7. Monthly Sales Trend Analysis

Monthly sales trends were explored to identify seasonal patterns.

#### Example:
```
df["Month"] = df["Date"].dt.month_name()

monthly_sales = df.groupby("Month")["TotalPrice"].sum()
```
### 8. Data Visualization

Visualizations were created using Matplotlib and Seaborn.

###### Top Selling Products Chart
```
top_products.head(10).plot(kind="bar")

plt.title("Top Selling Products")

plt.show()
```
###### Payment Method Distribution
```
df["PaymentMethod"].value_counts().plot(kind="bar")

plt.title("Payment Method Distribution")

plt.show()
```
###### Correlation Heatmap
```
import seaborn as sns

correlation = df.corr(numeric_only=True)

sns.heatmap(correlation, annot=True)

plt.title("Correlation Matrix")

plt.show()
```
### Key Insights

The analysis revealed several important insights:

- Certain products generated significantly higher sales
- Customer payment preferences were identified
- Monthly revenue trends showed variations in sales performance
- Some order statuses occurred more frequently than others
- Data visualization improved understanding of patterns and relationships

### Skills Demonstrated
- Exploratory Data Analysis (EDA)
- Data Visualization
- Python Programming
- Pandas
- Matplotlib
- Seaborn
- Business Insight Generation
- Data Interpretation

### Key Learning Outcomes

Through this project, I gained practical experience in:

- Exploring and understanding datasets
- Identifying trends and patterns
- Creating visualizations using Python
- Interpreting business insights from data
- Preparing data for dashboards and reporting

### Future Improvements

Potential future enhancements include:

- Building an interactive Power BI dashboard
- Advanced statistical analysis
- Predictive analytics and forecasting
- Customer segmentation analysis


## Author

Yusuf Akande

Aspiring Data Analyst passionate about Python, SQL, Power BI, and transforming data into actionable insights.
