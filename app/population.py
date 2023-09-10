import charts
import pandas as pd


def plot_country_population(data):
    #country_name = input('country  => ')
    country_name = 'Colombia'
    country_df = data[data['Country/Territory'] == country_name]
    years = list(filter(lambda x:x[:4].isnumeric(),country_df.columns))
    country_data = country_df[years]
    print(type(country_data))

    charts.generate_bar_chart(country_name,years, country_data.iloc[0,].values)

def plot_wolrd_population_rate(data):
    world_rate = data[data['Continent'] == 'South America']
    charts.generate_pie_chart(labels= world_rate['Country/Territory'].values, 
                              values=world_rate['World Population Percentage'].values)

def run():
    data = pd.read_csv('data.csv')
    plot_country_population(data)
    #plot_wolrd_population_rate(data)
