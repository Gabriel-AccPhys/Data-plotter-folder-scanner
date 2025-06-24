# importing modules
from math import nan
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import datetime
import os # added this to handle the csv files
import glob # added this to handle the csv files

#-----------------------------------------Plotter function------------------------------ 
def plotter(file_name,x_1,y_1,x_2,y_2):
    #Define the size of the plot
    plt.rcParams["figure.figsize"] = [20.5, 17]
    plt.rcParams.update({'font.size': 20})

    fig, ax1 = plt.subplots() 

    color = 'tab:red'
    ax1.set_xlabel('Time [MM/DD HH]')
    ax1.set_ylabel('Voltage [kV]', color=color)
    ax1.plot(x_1, y_1, "ob") # plots miliseconds on x-axis and milivotls on y-axis
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim(0, 300)
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    #color = 'tab:blue'
    ax2.set_ylabel('IP current [mA]', color=color)  # we already handled the x-label with ax1
    ax2.plot(x_2,y_2,"og") #plots decarad
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(0, 0.0001)
    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    #Plot title is created with file name
    plt.title('file name: ' + file_name) 

    #plt.ylim(0, 7) # controls y-axis limit
    #plt.grid(True) # controls Grid
    
    # Save the plot to file with the file_name variable as file name lol 
    plt.savefig(file_name + '.png') #save plot to png file
    
    # Show the plot
    plt.show() 

#----------------------------------------- Using glob to get all csv files ----------------------------------- credit to geeksforgeeks
# Read the file name
print ("Give me the folder path (files in it must be CSV format) ")
path=input()

#path = os.getcwd() This line was now asigned by reading the input
csv_files = glob.glob(os.path.join(path, "*.csv"))

# loop over the list of csv files
for f in csv_files:
      
    # read the csv file
    df = pd.read_csv(f, header = 0, names = ['time', 'Unix time', 'IGLGL01HVPSkVolts_ave', 'IGLGL01Preset_Volt', 'IGLGL01HVIREAD', 'IGLGL01UpRamp_Rate', 'VIPGT04cur', 'IFYGT00PICOdataRead', 'IDRGTS1RAD04'], parse_dates = ['time']) #Oscilloscope files have no header 
      
    #print the location and filename
    #print('Location:', f)
    #print('File Name:', f.split("\\")[-1])
      
    # print the content
    #print('Content:')
    #display(df)
    #print()
    
    # Call the plotter sub function 
    plotter(f, df['time'], df['IGLGL01HVPSkVolts_ave'], df['time'], df['VIPGT04cur'])

print('Done! ¯\_(ツ)_/¯')
#-----------------------------------------Data displays for troubleshooting------------------------------
# displays data for troubleshoot
#print('voltage data', voltage)
#print('decarad data', decarad)