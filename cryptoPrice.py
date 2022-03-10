# Description: This program gets the price of crypto currencies in real time
#              Based on the webpage: 
# https://betterprogramming.pub/get-the-price-of-cryptocurrencies-in-real-time-using-python-cdaf07516479

# Importing the libraries
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import requests
import time

#Create a function to get the price of a cryptocurrency
def get_crypto_price(coin):
    #Get the URL
    #url = "https://www.google.com/search?q=" + coin + "+price"
    url = "https://www.cointracker.io/price"

    #Make a request to the website
    HTML = requests.get(url).content

    #Parse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser') 

    #Find the current price 
    #text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    text = soup.find("table", attrs={'class':'table mx-auto'})#.find("td", attrs={'data-price-container-symbol':coin}).text
    print(text)

    #Return the text 
    return 1


#Create a main function to consistently show the price of the cryptocurrency
def main():
    #Set the last price to negative one
    last_price = {}

    #Create an infinite loop to continuously show the price
    while True:
        #Choose the cryptocurrency that you want to get the price of (e.g. bitcoin, litecoin)
        #crypto = ['bitcoin', 'litecoin', 'ether']
        crypto = ['BTC']

        for c in crypto:
            #Get the price of the crypto currency
            price = get_crypto_price(c)

            if c not in last_price.keys():
                last_price[c] = -1

            #Check if the price changed
            if price != last_price[c]:
                print(c + ' price: ', price) #Print the price
                last_price[c] = price #Update the last price

        time.sleep(3) #Suspend execution for 3 seconds.

main()