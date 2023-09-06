import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter =',')
      header = next(reader)
      list_dict = []
      for row in reader:
        iterable = zip(header, row)
        country_dict = {key:value for key, value in iterable}
        list_dict.append(country_dict)
    return list_dict
if __name__ == '__main__':
    read_csv('app/data.csv')