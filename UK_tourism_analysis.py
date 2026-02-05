import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("uttara_kannada_tourism_data.csv.xlsx")


print("Dataset Loaded Successfully")
print(df.head())
#average visitors per month
plt.figure()
plt.bar(df["Place"], df["Avg_Visitors_Per_Month"])
plt.title("Average Monthly Visitors by Tourist Place")
plt.xlabel("Tourist Place")
plt.ylabel("Average Visitors per Month")
plt.xticks(rotation=90)
plt.show()

#tourist distribution by category
category_data = df.groupby("Category")["Avg_Visitors_Per_Month"].sum()

plt.figure()
plt.pie(category_data.values, labels=category_data.index, autopct="%1.1f%%")
plt.title("Tourist Distribution by Category")
plt.show()

#tourist places ordered by distance
sorted_df = df.sort_values("Distance_From_Gokarna_KM")

plt.figure()
plt.barh(sorted_df["Place"], sorted_df["Distance_From_Gokarna_KM"])
plt.xlabel("Distance from Gokarna (KM)")
plt.title("Tourist Places Ordered by Distance")
plt.show()




#crowd level
crowd_counts = df["Crowd_Level"].value_counts()

plt.figure()
plt.pie(
    crowd_counts.values,
    labels=crowd_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={"width": 0.4}
)
plt.title("Distribution of Tourist Places by Crowd Level")
plt.show()

#season wise
season_data = df.groupby("Best_Season")["Avg_Visitors_Per_Month"].sum()

plt.figure()
plt.plot(season_data.index, season_data.values, marker='o')
plt.title("Season-wise Tourist Trend")
plt.xlabel("Season")
plt.ylabel("Total Visitors")
plt.show()

#eco sensitivity
eco_crowd = df.groupby("Eco_Sensitivity")["Avg_Visitors_Per_Month"].sum()

plt.figure()
plt.bar(eco_crowd.index, eco_crowd.values)
plt.title("Tourist Pressure by Eco Sensitivity Level")
plt.xlabel("Eco Sensitivity")
plt.ylabel("Total Visitors")
plt.show()

plt.figure()
plt.scatter(df["Entry_Fee"], df["Popularity_Score"])
plt.title("Entry Fee vs Popularity Score")
plt.xlabel("Entry Fee (₹)")
plt.ylabel("Popularity Score")
plt.show()


#popularity
category_popularity = df.groupby("Category")["Popularity_Score"].mean()

plt.figure()
plt.bar(category_popularity.index, category_popularity.values)
plt.xticks(rotation=45)
plt.xlabel("Category")
plt.ylabel("Average Popularity Score")
plt.title("Average Popularity by Tourism Category")
plt.show()






