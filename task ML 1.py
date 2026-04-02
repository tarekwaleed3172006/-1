import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
penguins = sns.load_dataset("penguins")

print("Tips Dataset")
print(tips.head())

sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Tips vs Total Bill")
plt.show()

print("Iris Dataset")
print(iris.head())

sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=iris)
plt.title("Iris Species")
plt.show()

print("Titanic Dataset")
print(titanic.head())

sns.countplot(x="survived", data=titanic)
plt.title("Survival Count")
plt.show()

print("Penguins Dataset")
print(penguins.head())

sns.scatterplot(x="bill_length_mm", y="flipper_length_mm", hue="species", data=penguins)
plt.title("Penguins")
plt.show()