import MetaTrader5 as mt5
import datetime as DT
import pytz  # import pytz module for working with time zone
import pandas as pd


# Function to start Meta Trader 5 (MT5)
def start_mt5(username, password, server, path):
    # Ensure that all variables are the correct type
    uname = int(username)  # Username must be an int
    pword = str(password)  # Password must be a string
    trading_server = str(server)  # Server must be a string
    filepath = str(path)  # Filepath must be a string

    # Attempt to start MT5
    if mt5.initialize(login=uname, password=pword, server=trading_server, path=filepath):
        print("Trading Bot Starting")
        # Login to MT5
        if mt5.login(login=uname, password=pword, server=trading_server):
            print("Trading Bot Logged in and Ready to Go!")
            # display data on the MetaTrader 5 package
            print("MetaTrader5 package author: ", mt5.__author__)
            print("MetaTrader5 package version: ", mt5.__version__)
            return True
        else:
            print("Login Fail")
            quit()
            return PermissionError
    else:
        print("MT5 Initialization Failed, error code =", mt5.last_error())
        quit()
        return ConnectionAbortedError


def tick_extraction():
    # run pandas
    pd.set_option('display.max_columns', 500)  # number of columns to be displayed
    pd.set_option('display.width', 1500)  # max table width to display
    # set time zone to UTC
    timezone = pytz.timezone("Etc/UTC")
    # create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
    utc_from = DT.datetime(2020, 5, 17, tzinfo=timezone)
    utc_to = DT.datetime(2023, 5, 17, tzinfo=timezone)
    # request USDJPY ticks within 17.05.2020 - 17.05.2023
    try:
        ticks = mt5.copy_ticks_range("USDJPY", utc_from, utc_to, mt5.COPY_TICKS_ALL)
        print("Ticks variable:", ticks)
        print("Ticks variable type:", type(ticks))
        if ticks is not None:
            print("Ticks received:", len(ticks))
        else:
            print("No ticks recieved")
    except Exception as e:
        print("An error occured:", str(e))

    # shut down connection to the MetaTrader 5 terminal
    mt5.shutdown()

    # display data on each tick on a new line
    print("Display obtained ticks 'as is'")
    count = 0
    for tick in ticks:
        count += 1
        print(tick)
        if count >= 10:
            break

    # create DataFrame out of the obtained data
    ticks_frame = pd.DataFrame(ticks)
    # convert time in seconds into the datetime format
    ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')

    # display data
    print("\nDisplay dataframe with ticks")
    print(ticks_frame.head(10))
