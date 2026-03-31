import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales.csv")

# -------- CORRELATION HEATMAP --------
corr = df.corr(numeric_only=True)
plt.figure(figsize=(6,5))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("../outputs/heatmap.png")
plt.close()

# -------- PAIRPLOT --------
sns.pairplot(df)
plt.savefig("../outputs/pairplot.png")
plt.close()

print("Heatmap and pairplot saved in outputs folder!")