import matplotlib.pyplot as plt
import pandas as pd

# Loading the netflix dataset

data = pd.read_csv("netflix_titles.csv")

# Basic information

print(data.info())
print(data.head())
print(data.describe())

# Movies VS TV shows

type_count = data['type'].value_counts()

# Creating a bar chart for Movies vs TV Shows   
plt.bar(
    type_count.index,
    type_count.values,
    width=0.7
)
plt.xlabel("Types: ")
plt.ylabel("Number of Titles: ")
plt.title("Movies Vs TV Shows")

plt.show()

# Rating distribution

rating_count = data['rating'].value_counts().head(10)

# Creating a Pie chart for Rating distribution
plt.pie(
    rating_count.values,
    labels = rating_count.index,
    autopct ="%1.1f%%",
    startangle = 90
)
plt.title("Rating Distribution")
plt.show()

# Release by year
year_count = data['release_year'].value_counts().sort_index()

# Creating a line chart for Release by Year
plt.plot(
    year_count.index,
    year_count.values,
    marker = 'o'
)
plt.xlabel("Release Year")
plt.ylabel("Titles")
plt.title("Release by Year")
plt.show()

# Duration distribution
movies =data[data['type']=="Movie"].copy()
movies["duration_minutes"] = (
    movies["duration"]
    .str.replace(" min", "", regex=False)
    .astype(float)
)

# Creating a histogram for Duration distribution

plt.hist(
    movies["duration_minutes"],
    bins=20,
    edgecolor="black",
    alpha=0.8
)

plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")
plt.title("Netflix Movie Duration Distribution")

plt.show()

# Release Year VS Duration

# Creating a scatter plot for Release Year vs Duration
plt.scatter(
    movies["release_year"],
    movies["duration_minutes"],
    alpha=0.5
)

plt.xlabel("Release Year")
plt.ylabel("Duration (Minutes)")
plt.title("Release Year vs Movie Duration")

plt.grid(True)

plt.show()

