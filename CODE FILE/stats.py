import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales.csv")

# -------- HISTOGRAM --------
plt.figure()
sns.histplot(df["Sales"], kde=True)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("../outputs/histogram.png")
plt.close()

# -------- BOX PLOT --------
plt.figure()
sns.boxplot(x=df["Sales"])
plt.title("Boxplot of Sales")
plt.tight_layout()
plt.savefig("../outputs/boxplot.png")
plt.close()

# -------- REGION BOX PLOT --------
plt.figure()
sns.boxplot(x="Region", y="Sales", data=df)
plt.title("Sales by Region")
plt.tight_layout()
plt.savefig("../outputs/region_boxplot.png")
plt.close()

print("Statistical plots saved in outputs folder!")