# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
print(data.head(10))


# --------------
#Code starts here



#data['Better_Event'] = np.where((data['Total_Summer']==data['Total_Winter'],'Both')
data['Better_Event'] = np.where(data['Total_Summer']==data['Total_Winter'],'Both',np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter'))

better_event = data['Better_Event'].value_counts(ascending=False).idxmax()
print('The better event with respect to all the performing countries :', better_event)


# --------------
#Code starts here

top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = top_countries.drop(top_countries.index[-1])

#print(top_countries.tail())

def top_ten(top_countries,col):

    country_list=[]
    country_list = top_countries.nlargest(10,col)['Country_Name']
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer').tolist()
top_10_winter = top_ten(top_countries,'Total_Winter').tolist()
top_10 = top_ten(top_countries,'Total_Medals').tolist()

common = list(set(top_10_summer).intersection(set(top_10_winter)).intersection(set(top_10)))

print(common)



# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]

winter_df = data[data['Country_Name'].isin(top_10_winter)]

top_df = data[data['Country_Name'].isin(top_10)]

plt.figure(figsize=[12,6])
plt.xlabel("Country Name")
plt.ylabel("Total medal count (Summer)")
plt.title("Total Medals won by Top 10 Countries in Summer Olympics")
plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])


plt.figure(figsize=[12,6])
plt.xlabel("Country Name")
plt.ylabel("Total medal count (Winter)")
plt.title("Total Medals won by Top 10 Countries in Winter Olympics")
plt.bar(summer_df['Country_Name'],summer_df['Total_Winter'])


plt.figure(figsize=[12,6])
plt.xlabel("Country Name")
plt.ylabel("Total medal count (Summer)")
plt.title("Total Medals won by Top 10 Countries in Summer and Winter Olympics")
plt.bar(summer_df['Country_Name'],summer_df['Total_Medals'])





# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio']==summer_max_ratio,                            'Country_Name'].item()
print("Maximum Golden Ratio in Summer Olympics : " , summer_max_ratio)
print("Country with maximum Golden Ratio in Summer Olympics : " , summer_country_gold)



winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio']==winter_max_ratio,                            'Country_Name'].item()
print("Maximum Golden Ratio in Winter Olympics : " , winter_max_ratio)
print("Country with maximum Golden Ratio in Winter Olympics : " , winter_country_gold)



top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.loc[top_df['Golden_Ratio']==top_max_ratio, 'Country_Name'].item() 
print("Maximum Golden Ratio in Summer and Winter Olympics : " , top_max_ratio)
print("Country with maximum Golden Ratio in Summer and Winter Olympics : " , top_country_gold)








# --------------
#Code starts here
data_1 = data.drop(data.index[-1])


data_1['Total_Points'] = data_1['Gold_Total'].multiply(3) + data_1['Silver_Total'].multiply(2) + data_1['Bronze_Total'].multiply(1)

most_points = data_1['Total_Points'].max()
print("Maximum Point : ",most_points)
best_country =data_1.loc[data_1['Total_Points'] == most_points, 'Country_Name'].item()
print("Best country : ",best_country)



# --------------
#Code starts here

best = data[data['Country_Name'] == best_country]
best = best[['Country_Name','Gold_Total','Silver_Total','Bronze_Total']]
best.set_index('Country_Name',inplace=True)
print(best)
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.title("Medals Tally of US in Olympics")
plt.xticks(rotation=45)





