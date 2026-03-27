import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("titanic.csv")


print(data.head())


print("Shape:", data.shape)
print(data.info())


print(data.describe())


print(data.isnull().sum())


print("Duplicates:", data.duplicated().sum())


data = data.drop_duplicates()


plt.hist(data["Age"])
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()


sns.countplot(x="Survived", data=data)
plt.title("Survival Count")
plt.show()


sns.countplot(x="Sex", data=data)
plt.title("Gender Distribution")
plt.show()


sns.boxplot(x=data["Fare"])
plt.title("Fare Distribution")
plt.show()


plt.figure(figsize=(8,5))
sns.heatmap(data.corr(), annot=True)
plt.show()


data["Age"] = data["Age"].fillna(data["Age"].mean())


data["Sex"] = data["Sex"].map({"male":0, "female":1})


data = data.drop(["Name","Ticket","Cabin"], axis=1)


print(data.isnull().sum())

print("Data preprocessing completed")