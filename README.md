# :earth_americas: E-commerce Data Analysis for Amazon

# Project Scope 

The project scope is to gather insights about the users of Amazon, and find things like customer shopping behaviors, segment customers based on their buying patterns, and identify relationships between products. 

The tasks that need to be done for the analysis:

1. Data preprocessing: taking the raw data extracted from a paage, and either drop the NA coloumns, or handel the data
2. feture engenering: creating fetures like fequrencey, monarart value, as well as taking exsiting coloums and converiing the data type, for example taking thr price values and converting them to floats.
3. EDA: create visualizationa and analyse the data to gather insights
4. Rule mining: genartte ascoations to find patterens
5. Clustering: use k-means clusters to find patterens
6. Gather insights: analyse the information and gather insights 
# Data preprocessing 

Methods used:

1. dropNA: dropped all the values
2. Outlier Handeling

# Visualizations:

## Price Distribution Analysis
![Price Distribution by Main Category](./price_distribution.png)

The scatter plot above shows the relationship between actual prices and discount prices across different product categories on Amazon. Key observations:
- Electronics products show the widest price range and highest prices
- Most products cluster in the lower price ranges (0-20,000)
- There's a strong linear relationship between actual and discount prices
- Different product categories show distinct pricing patterns

# Key insights

1. People usualy buy eletronics, coumputers along twith their accessories, and kicthen appliences from amamzon
2. The avrage price of most amazon orders is between $500 to $1000
3. There is a fine limit for discounts, which is around 70%, then the quality of the prouduct w
4. Based on Clustering, i found out that mst people buy one thing per purchas, and usualy do not buy in bulk unless it is cheap.
5. Basedon rule ascoation rule mining with the apriori algrothim, i found that usualy the prices for coumputers and acsories are in tme medium range, and has an avrage rating. This means that they are not too expensive, and not too good. The home and kicthen has a high price, but a medium rating, so the items there are over priced items. The electronics items have a high pirce, but a high rating, so it says that the items are good quality and are proplery priced. 

# Steramlit deployment link 

https://gdp-dashboard-3r3a45ggkft.streamlit.app


# Refrecens

[www.youtube.com/watch?v=afPJeQuVeuY&t](https://www.youtube.com/watch?v=afPJeQuVeuY&t)
