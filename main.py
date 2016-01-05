import pandas as pd
import datetime
import matplotlib.pyplot as plt
import Quandl
import pickle
from matplotlib import style
style.use('fivethirtyeight')

#df = Quandl.get("FMAC/HPI_TX", authtoken='iie_m681_WCTJwD_R9ed')

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]

def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = Quandl.get(query, authtoken='iie_m681_WCTJwD_R9ed')
        print(query)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    pickle_out = open('fiddy_states.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

#grab_initial_state_data()

HPI_data = pd.read_pickle('fiddy_states.pickle')
HPI_data.plot()
plt.legend().remove()
plt.show()