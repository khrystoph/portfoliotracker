# Introduction

  The purpose of this tool is a few things:
  1. give me more python experience
  2. provide an easy way to track all my stocks in a centralized location (outside of my various stock portfolios)
  3. eventually hook in with Amazon Echo as an app that can present stock value, portfolio value, and individual stock
    price for an individual check.

# Basic Use

  To use this application, you need a few packages installed via pip:
  1. google finance
  ```
  sudo pip install googlefinance
  ```
  2. json python module
  ```
  sudo pip install json
  ```
  3. You MAY need to install the csv module (but I don't think you do)
  ```
  sudo pip install csv
  ```
  You will additionally need a csv file in the following directory:
  ```
  ~/github/portfoliotracker/stocks.txt
  ```

  There is expectation that the stocks file is located there. If you want to change this behavior, you can modify this
  line in the finance.py file:
  ```
  confFile = os.path.expanduser('~/github/portfoliotracker/stocks.txt')
  ```

  Eventually, this behavior may change if I create an init function that sets up your file for you.
  Stocks follow the following format in this file:
  ticker,quantity

  The purpose for this is that you just set the ticker and the number of that stock you own and it will parse the file
  and calculate the total value of your existing stocks.

# Warnings
  This software comes without any support or warranty. I am providing the code that I have created free of charge and
  with open distribution on purpose. First and foremost, this project is for myself. So, I work on my own timeline and
  make decisions about what it will do where the code will go based on how I envision the software down the road. You
  are free to make suggestions or let me know if you have any problems with the code, but there is no guarantee I will
  respond in a timely manner. As this is intended for PERSONAL use, please do not hook this in with production software
  that could make decisions or hook in with trading applications. If you do so, and something goes wrong, it is your own
  responsibility and I will not be liable for your use of the code.