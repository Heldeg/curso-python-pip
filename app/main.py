import utils, read_csv
import population



def run():
    keys, values = utils.get_population()
    print(keys,values)
    country = input('type country: ')
    result = utils.population_by_country(data,country)
    print(result)

if __name__ == '__main__':
    data = read_csv.read_csv('app/data.csv')
    population.plot_wolrd_population_rate(data)
    population.plot_country_population(data)