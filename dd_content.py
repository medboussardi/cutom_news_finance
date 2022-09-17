import csv

def get_random_quote():
    try:
        with open('quotes.csv','r') as csvfile:
            quotes = [{'Author':line[0],'quotes':line[1]} for line in csv.reader(csvfile,delimiter='|')]
    except IOError:
        quotes = {'Author':'Robert Arnott','quotes':"In investing what is comfortable is rarely profitable."}        
    return quotes 

def get_weather_forecast():
    pass

def get_twitter_trends():
    pass

def get_wikipedia_article():
    pass

if __name__ == '__main__':
    pass # test code