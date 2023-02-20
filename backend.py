"""
Prototype backend for Calgary Hacks 2023 project

Description:
-Receives emission and forcast data as CSV and creates
visualizations for use in frontend map application.

Author: Seth Campbell

credit:

"""
#libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

"""
creates an emission chart for an inputted state (based on two letter acronym)
e.g. "AL" for Alabama, and would be saved to current directory as "AL_emissions.png"
"""
def create_state_plot(st_acronym):
    # get full state name from imported table
    #st_name = state_table.loc[st_acronym][0]
    print(st_acronym)
    st_name = state_table[state_table["Postal"]==st_acronym].State
    st_name = st_name[st_name.first_valid_index()] #yes, this is janky, but it gets the job done...


    # plotting historical data
    st_data = data_index[data_index["State"]==st_acronym]  # filter data for one state
    ax = plt.axes()
    plt.plot(st_data["Date"], st_data["Historical"], label="Historical")

    #plotting predicted data
    #pred_idx = st_data["Gross Load (MWh)"].last_valid_index() - st_data["Gross Load (MWh)"].first_valid_index() + 1 #index of row where predictions column data starts
    plt.plot(st_data["Date"], st_data["Predicted"], label="Prediction") #replace steam with prediction column name later
    ax.xaxis.set_major_locator(ticker.MaxNLocator(15))  # only show inputted number of x-axis ticks
    ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ','))) #format y-axis to seperate thousands with a ",", from https://stackoverflow.com/questions/25973581/how-to-format-axis-number-format-to-thousands-with-a-comma
    plt.legend(framealpha=0.2) #display legend w/ semi-transparent background

    # formatting    
    plt.title("{} Emissions".format(st_name))
    plt.xlabel('Date')
    plt.ylabel('CO2 mass (short tons)')
    plt.xticks(rotation=30, ha='right')
    plt.savefig("{}_emissions.png".format(st_acronym), transparent=False, bbox_inches="tight", dpi=125)
    plt.clf()

def create_all_plots():
    for i in state_table["Postal"]:
        create_state_plot(i)


#--------------------------------------------------

# load data
#data = pd.read_csv('foo.csv', index_col = "State")
#data = pd.read_csv('foo_2.csv', index_col = "State")
#data_index = pd.read_csv('foo_2.csv') #version of data that is not indexed by state name
data_index = pd.read_csv('james_final_data.csv')
#state_table = pd.read_csv('state names.csv', index_col = "Postal")
state_table = pd.read_csv('state names.csv')

create_state_plot("AL")
