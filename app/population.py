import read_csv
import charts
import utils


def plot_country_population(data):
    country_name = input('country  => ')

    country_data_raw = utils.population_by_country(data, country_name)[0]
    print(country_data_raw)

    country_data = {key[:4]: value for key, value in country_data_raw.items() if len(key) > 3 and key[:4].isnumeric()}

    country_data = dict(sorted(country_data.items()))

    charts.generate_bar_chart(country_name,country_data.keys(),list(map(lambda x: int(x),country_data.values())))

def plot_wolrd_population_rate(data):
    world_rate = {dict['Country/Territory']: dict['World Population Percentage'] for dict in data if dict['Continent'] == 'South America'}
    charts.generate_pie_chart(labels= world_rate.keys(), values=world_rate.values())

if __name__ == '__main__':
    data = read_csv.read_csv('app/data.csv')
    plot_wolrd_population_rate(data)
    plot_country_population(data)