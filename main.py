# Description: This web app is a stock market dashboard to show data and charts of stocks of various companies and
# also the predicted prices.

# Import the libraries
import streamlit as st
import pandas as pd
from PIL import Image

st.write("""
# Stock Market Web Application
**Visually** shows the stock data for various companies!
""")
image = Image.open("Stock.jpeg")
st.image(image, use_column_width=True)

# Create a sidebar header
st.sidebar.header('User Input')


# Create a function to get the users input
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2016-03-23")
    end_date = st.sidebar.text_input("End Input", "2021-03-16")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "TATAMOTORS")
    return start_date, end_date, stock_symbol


# Function to get the company name
def get_company_name(symbol):
    if symbol == 'ASIANPAINT':
        return 'Asian Paints'
    elif symbol == 'BAJFINANCE':
        return 'Bajaj Finance'
    elif symbol == 'BRITANNIA':
        return 'Britannia'
    elif symbol == 'INDIGO':
        return 'Indigo'
    elif symbol == 'KOTAKBANK':
        return 'Kotak Bank'
    elif symbol == 'LT':
        return 'L&T'
    elif symbol == 'INFY':
        return 'Infosys'
    elif symbol == 'BHARTIARTL':
        return 'Airtel'
    elif symbol == 'HDFCBANK':
        return 'HDFC Bank'
    elif symbol == 'RELIANCE':
        return 'Reliance'
    elif symbol == 'TATAMOTORS':
        return 'Tata Motors'
    elif symbol == 'TITAN':
        return 'Titan'
    else:
        print(symbol)
        'None'


# Function to get proper company data and the the proper timeframe
def get_data(symbol, start, end):
    if symbol.upper() == 'ASIANPAINT':
        df = pd.read_csv('https://raw.githubusercontent.com/Aum020/Stock-Market-Analysis/master/Datasets/ASIANPAINT.csv?token=AOAVBUDYEXORLEVWLJ3MZUTAO36RA')
    elif symbol.upper() == 'BAJFINANCE':
        df = pd.read_csv('https://raw.githubusercontent.com/Aum020/Stock-Market-Analysis/master/Datasets/bajajfinance.csv?token=AOAVBUBODMF7GM6LIMAVJD3AO36T6')
    elif symbol.upper() == 'BRITANNIA':
        df = pd.read_csv('https://raw.githubusercontent.com/Aum020/Stock-Market-Analysis/master/Datasets/BRITANNIA.csv?token=AOAVBUESYCOKVVU4464L5ETAO36VS')
    elif symbol.upper() == 'INDIGO':
        df = pd.read_csv('https://raw.githubusercontent.com/Aum020/Stock-Market-Analysis/master/Datasets/INDIGO.csv?token=AOAVBUEQH4WINIA4TE66QYTAO36YK')
    elif symbol.upper() == 'KOTAKBANK':
        df = pd.read_csv('https://raw.githubusercontent.com/Aum020/Stock-Market-Analysis/master/Datasets/KOTAKBANK.csv?token=AOAVBUEZZNRSFHFX36T2RTLAO362O')
    elif symbol.upper() == 'LT':
        df = pd.read_csv('https://raw.githubusercontent.com/Aum020/Stock-Market-Analysis/master/Datasets/LT.csv?token=AOAVBUBT5KOJZGZE4HXPTZTAO3634')
    elif symbol.upper() == 'INFY':
        df = pd.read_csv('https://raw.githubusercontent.com/Aum020/Stock-Market-Analysis/master/Datasets/INFY.NS.csv?token=AOAVBUGERDG23TAKJTSRUTLAO3666')
    elif symbol.upper() == 'BHARTIARTL':
        df = pd.read_csv('https://raw.githubusercontent.com/Aum020/Stock-Market-Analysis/master/Datasets/BHARTIARTL.NS.csv?token=AOAVBUHOT54UB4WDVRQOCZ3AO37J4')
    elif symbol.upper() == 'HDFCBANK':
        df = pd.read_csv('https://raw.githubusercontent.com/Aum020/Stock-Market-Analysis/master/Datasets/HDFCBANK.NS%20(1).csv?token=AOAVBUARO6P77KO3ERGMQ6DAO37OE')
    elif symbol.upper() == 'RELIANCE':
        df = pd.read_csv('https://raw.githubusercontent.com/Aum020/Stock-Market-Analysis/master/Datasets/ril(1).csv?token=AOAVBUEUAFZF73CJWMJTOUDAO37SI')
    elif symbol.upper() == 'TATAMOTORS':
        df = pd.read_csv('https://raw.githubusercontent.com/Aum020/Stock-Market-Analysis/master/Datasets/TATAMOTORS.csv?token=AOAVBUHXT3V7ZACOQ6QNNSLAO37T4')
    elif symbol.upper() == 'TITAN':
        df = pd.read_csv('https://raw.githubusercontent.com/Aum020/Stock-Market-Analysis/master/Datasets/TITAN.csv?token=AOAVBUGIF5ARIBD7RVMMU53AO37VM')
    else:
        df = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    print(start, end)
    #Set the start date and end index both to 0
    start_row = 0
    end_row = 0

    #Start the date from top of the data set and go down to see if the user date is less than or equal to the date in the given data
    for i in range(0, len(df)):
        if start>=pd.to_datetime(df['Date'][i]):
            start_row = i
            break
    #Start the data set from top of the data set and go down to see if the user date is
    for j in range(0,len(df)):
        if end<=pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df) - 1 - j
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))
    return df.iloc[start_row:end_row+1,:]
# Get the user input
start, end, symbol = get_input()
# Get the data
df = get_data(symbol,start,end)
#Get the company name
print(symbol)
company_name = get_company_name(symbol.upper())
print("Company name is ",company_name)
#Display the close price
st.header(company_name+' Close\n')
st.line_chart(df['Close'])
#Display the volume
st.header(company_name+ " Volume\n")
st.line_chart(df['Volume'])

#Get stats on the data
st.header('Data statistics')
st.write(df.describe())
