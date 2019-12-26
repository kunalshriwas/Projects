# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data = data.rename(columns={'Total': 'Total_Medals'})
data.head(10)


# --------------
#Code starts here\
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')

data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])

better_event=data['Better_Event'].value_counts().index.values[0]
#better_Event = 'Summer'
#Better_Event.iloc[]
print(better_event)
#print(Better_Event[0,0])
#sub_df.iloc[0]['A']


# --------------
#Code starts here
top_countries=pd.DataFrame(data,columns=['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'])
top_countries=top_countries[:-1]
def top_ten(data,col):
    country_list=[]
    country_list= list((data.nlargest(10,col)['Country_Name']))
    return country_list
top_10_summer=top_ten(top_countries,'Total_Summer')
print(top_10_summer)
top_10_winter=top_ten(top_countries,'Total_Winter')
print(top_10_winter)
top_10=top_ten(top_countries,'Total_Medals')
common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))



# --------------
#Code starts here
summer_df  = data[data['Country_Name'].isin(top_10_summer)]
#print(summer_df)

winter_df  = data[data['Country_Name'].isin(top_10_winter)]


top_df  = data[data['Country_Name'].isin(top_10)]

summer_df.plot(x='Country_Name', y='Total_Summer', kind='bar') 
plt.show()

winter_df.plot(x='Country_Name', y='Total_Winter', kind='bar') 
plt.show()

top_df.plot(x='Country_Name', y='Total_Medals', kind='bar') 
plt.show()


# --------------
#Code starts here
#summer_df['Golden_Ratio'] = summer_df['Total_Summer']//summer_df['Gold_Summer']
#summer_max_ratio = summer_df['Golden_Ratio'].max()
#print(summer_max_ratio)

summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer'] 
summer_max_ratio=max(summer_df['Golden_Ratio']) 
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_max_ratio)
print(summer_country_gold)


winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter'] 
winter_max_ratio=max(winter_df['Golden_Ratio']) 
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_max_ratio)
print(winter_country_gold)


top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals'] 
top_max_ratio=max(top_df['Golden_Ratio']) 
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_max_ratio)
print(top_country_gold)



# --------------
#Code starts here
data_1=data[:-1]
data_1['Total_Points'] = (data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+(data_1['Bronze_Total']*1)
most_points = max(data_1['Total_Points']) 
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(most_points)
print(best_country)


# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
#best.head()
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked = True)
plt.xlabel('United states')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


