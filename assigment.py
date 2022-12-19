#import important libraries
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import style
import numpy as np 
import seaborn as sns 



# using pandas to read worldbank data  
data = pd.read_csv('worldbank_dataset.csv')



# countries nitrous oxide data over specfic years
# we need to extract data from our original data frame
nitrous_oxide_data = data[['country','year','nitrous_oxide']]

# drop the null values present in the dataset
nitrous_oxide_data = nitrous_oxide_data.dropna()


# data related to 1990 
no_data_1990 = nitrous_oxide_data[nitrous_oxide_data['year'] == 1990] 

# data related to 1995
no_data_1995 = nitrous_oxide_data[nitrous_oxide_data['year'] == 1995] 

# data related to 2000
no_data_2000 = nitrous_oxide_data[nitrous_oxide_data['year'] == 2000] 

# data related to 2005 
no_data_2005 = nitrous_oxide_data[nitrous_oxide_data['year'] == 2005] 

# data related to 2010 
no_data_2010 = nitrous_oxide_data[nitrous_oxide_data['year'] == 2010]

# data related to 2015 
no_data_2015 = nitrous_oxide_data[nitrous_oxide_data['year'] == 2015]

# data related to 2020 
no_data_2020 = nitrous_oxide_data[nitrous_oxide_data['year'] == 2020] 


def plot_bar_plot():
    ''' 
    This function will plot a bar chart for different countries
    over the years for nitrous oxide emission data
    
    return plt.show() 
    
    To display the bar plot
    
    '''
    style.use('ggplot')

    # set fig size
    plt.figure(figsize=(15,10))

    # set width of bars
    barWidth = 0.1

    # plot bar charts
    plt.bar(np.arange(no_data_1990.shape[0]),
        no_data_1990['nitrous_oxide'],
        color='indigo', width=barWidth, label='1990')

    plt.bar(np.arange(no_data_1995.shape[0])+0.2,
        no_data_1995['nitrous_oxide'],
        color='violet',width=barWidth, label='1995')

    plt.bar(np.arange(no_data_2000.shape[0])+0.3,
        no_data_2000['nitrous_oxide'],
        color='pink',width=barWidth, label='2000')

    plt.bar(np.arange(no_data_2005.shape[0])+0.4,
        no_data_2005['nitrous_oxide'],
        color='olive',width=barWidth, label='2005')

    plt.bar(np.arange(no_data_2010.shape[0])+0.5,
        no_data_2010['nitrous_oxide'],
        color='dodgerblue',width=barWidth, label='2010')

    plt.bar(np.arange(no_data_2015.shape[0])+0.6,
        no_data_2015['nitrous_oxide'],
        color='crimson',width=barWidth, label='2015')




    # show the legends on the plot
    plt.legend()

    # set the x-axis label
    plt.xlabel('Country',fontsize=15)

    # add title to the plot 
    plt.title("Nitrous Oxide Emissions",fontsize=15)

    # add countries names to the 11 groups on the x-axis
    plt.xticks(np.arange(no_data_2010.shape[0])+0.2,
               ('Brazil', 'China', 'Germany', 'France', 'Japan', 'Sri Lanka',
           'Mexico', 'Netherlands', 'Pakistan', 'Russian',
           'Turkiye', 'United States'),
               fontsize=10,rotation = 45)

    # show the plot
    return plt.show()



# we want to see countries Population over the years
# we need to filter our original data frame to get specific fields
pop_data = data[['country','year','population_growth']]

# drop the null values present in the dataset
pop_data = pop_data.dropna()


bz_pop = pop_data[pop_data['country'] == 'Brazil']
chn_pop = pop_data[pop_data['country']== 'China']
ger_pop =  pop_data[pop_data['country'] == 'Germany'] 
fr_pop = pop_data[pop_data['country'] == 'France'] 
jap_pop = pop_data[pop_data['country'] == 'Japan'] 
mex_pop = pop_data[pop_data['country'] == 'Mexico'] 
neth_pop = pop_data[pop_data['country'] == 'Netherlands'] 
rsa_pop = pop_data[pop_data['country'] == 'Russian Federation'] 
turk_pop = pop_data[pop_data['country'] == 'Turkiye'] 
sri_pop = pop_data[pop_data['country'] == 'Sri Lanka'] 
us_pop = pop_data[pop_data['country'] == 'United States'] 
pk_pop = pop_data[pop_data['country']== 'Pakistan'] 


def plot_line_plot():
    '''
        This function will plot line plot for growth rate annually in population
        for different countries over specfic decades
    
    '''
    # set fig size
    plt.figure(figsize=(10,10))

    # set the line plot value on x-axis and y-axis by year and population growth respectively
    plt.plot(bz_pop.year, bz_pop.population_growth, '--',label='Brazil')
    plt.plot(chn_pop.year, chn_pop.population_growth,'--',label='China')
    plt.plot(ger_pop.year, ger_pop.population_growth,'--',label='Germany')
    plt.plot(fr_pop.year, fr_pop.population_growth,'--',label='France')
    plt.plot(jap_pop.year, jap_pop.population_growth,'--',label='Japan')
    plt.plot(mex_pop.year, mex_pop.population_growth,'--',label='Mexico')
    plt.plot(neth_pop.year, neth_pop.population_growth,'--',label='Netherlands')
    plt.plot(rsa_pop.year, rsa_pop.population_growth,'--',label='Russia')
    plt.plot(turk_pop.year, turk_pop.population_growth,'--',label='Turkiya')
    plt.plot(sri_pop.year, sri_pop.population_growth,'--',label='Sri Lanka')
    plt.plot(us_pop.year, us_pop.population_growth,'--',label='US')
    plt.plot(pk_pop.year, pk_pop.population_growth,'-',label='Pakistan')

    #Set the X-axis label and make it bold
    plt.xlabel('Year',fontweight='bold')

    #Set the Y-axis labe
    plt.ylabel('Growth rate',fontweight='bold')

    # set the title
    plt.title("Population Growth")

    # show the legends on the plot and place it on suitable position
    plt.legend(bbox_to_anchor=(0.99,0.6),shadow=True)

    #show the line plot
    plt.show()

# making dataframe of US data
pk_df = data[data['country'] == 'Pakistan']
pk_df.head(5)


def remove_null_values(feature):
    '''
    This function takes dataframe feature as a input
    remove missing values in it and return valid values 
    '''
    return np.array(feature.dropna())



# Making dataframe of all the feature in the avaiable in 
# US dataframe passing it to remove null values function 
# for dropping the null values 
greenhouse = remove_null_values(pk_df[['greenhouse_gas_emissions']])

argicultural_land = remove_null_values(pk_df[['agricultural_land']])

nitrous_oxide = remove_null_values(pk_df[['nitrous_oxide']])

irrigated_land = remove_null_values(pk_df[['irrigated_land']])

forest_area = remove_null_values(pk_df[['forest_area']])

population = remove_null_values(pk_df[['population_growth']])

urban_pop = remove_null_values(pk_df[['urban_population']])

gdp = remove_null_values(pk_df[['GDP']])

# find the lenght of each feature size
# this will help us in creating dataframe 
# to avoid axis bound error in data frame creation
print('greenhouse Length = '+str(len((greenhouse)))) 
print('argicultural_land Length = '+str(len(argicultural_land))) 
print('nitrous_oxide  Length = '+str(len(nitrous_oxide))) 
print('irrigated_land Length = '+str(len(irrigated_land)))
print('forest_area Length = '+str(len(forest_area)))
print('population Length = '+str(len(population)))
print('urban_pop Length = '+str(len(urban_pop)))
print('gdp Length = '+str(len(gdp)))


# after removing the null values we will create datafram for China data
pk_data = pd.DataFrame({'GreenHouse': [greenhouse[x][0] for x in range(30)],
                                 'Argicultural Land': [argicultural_land[x][0] for x in range(30)],
                                 'Forest Area': [forest_area[x][0] for x in range(30)],
                                 'Nitrous Oxide': [nitrous_oxide[x][0] for x in range(30)],
                                 'Population': [population[x][0] for x in range(30)],
                                 'Urban': [urban_pop[x][0] for x in range(30)],
                                 'GDP': [gdp[x][0] for x in range(30)],
                                })



def plot_correlation_matrix():
    '''
        This function display correlation matrix of Pakistan 
        which will show different relationship between different 
        features.
        
    '''
    # create correlation matrix
    corr_matrix = pk_data.corr()
    plt.figure(figsize=(8,5))
    # using seaborn library to create heatmap 
    sns.heatmap(corr_matrix, annot=True,cmap="YlGnBu")
    plt.title("Correlation Heatmap of Pakistan")
    plt.show()


plot_correlation_matrix()

