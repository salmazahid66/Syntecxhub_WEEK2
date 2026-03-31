import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales.csv")
df["Date"] = pd.to_datetime(df["Date"])

# -------- LINE CHART --------
plt.figure()
plt.plot(df["Date"], df["Sales"])
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../outputs/line_chart.png")
plt.close()

# -------- BAR CHART --------
category_sales = df.groupby("Category")["Sales"].sum()
plt.figure()
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("../outputs/bar_chart.png")
plt.close()

# -------- PIE CHART --------
plt.figure()
category_sales.plot(kind="pie", autopct='%1.1f%%')
plt.title("Sales Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("../outputs/pie_chart.png")
plt.close()

print("Charts saved in outputs folder!")