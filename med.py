import pandas as pd
import matplotlib.pyplot as plt

# Create sample medical store data
data = {
    "Medicine Name": [
        "Paracetamol",
        "Amoxicillin",
        "Cetirizine",
        "Ibuprofen",
        "Azithromycin"
    ],
    "Selling Price": [20, 80, 30, 50, 100],
    "Quantity": [150, 90, 120, 100, 70]
}

df = pd.DataFrame(data)

# Calculate total sales
df["Total Sales"] = df["Selling Price"] * df["Quantity"]

print("Medical Store Dataset:")
print(df)

print("\nTotal Sales:", df["Total Sales"].sum())


# 1. Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(df["Medicine Name"], df["Quantity"])
plt.title("Medicine Quantity - Bar Chart")
plt.xlabel("Medicine Name")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 2. Horizontal Bar Chart
plt.figure(figsize=(8, 5))
plt.barh(df["Medicine Name"], df["Quantity"])
plt.title("Medicine Quantity - Horizontal Bar Chart")
plt.xlabel("Quantity")
plt.ylabel("Medicine Name")
plt.tight_layout()
plt.show()


# 3. Pie Chart
plt.figure(figsize=(7, 7))
plt.pie(
    df["Quantity"],
    labels=df["Medicine Name"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Medicine Quantity - Pie Chart")
plt.axis("equal")
plt.show()


# 4. Line Chart
plt.figure(figsize=(8, 5))
plt.plot(
    df["Medicine Name"],
    df["Total Sales"],
    marker="o"
)
plt.title("Medicine Sales - Line Chart")
plt.xlabel("Medicine Name")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 5. Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(df["Selling Price"], df["Quantity"])
plt.title("Selling Price vs Quantity - Scatter Plot")
plt.xlabel("Selling Price")
plt.ylabel("Quantity")
plt.tight_layout()
plt.show()


# 6. Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Quantity"], bins=5)
plt.title("Medicine Quantity - Histogram")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# 7. Box Plot
plt.figure(figsize=(8, 5))
plt.boxplot(df["Quantity"])
plt.title("Medicine Quantity - Box Plot")
plt.ylabel("Quantity")
plt.show()


# 8. Area Chart
plt.figure(figsize=(8, 5))
plt.fill_between(
    range(len(df)),
    df["Total Sales"],
    alpha=0.5
)
plt.plot(df["Total Sales"], marker="o")
plt.title("Medicine Sales - Area Chart")
plt.xlabel("Medicine Index")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()