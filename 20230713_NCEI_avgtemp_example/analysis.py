###### Imports
import numpy as np
import matplotlib.pyplot as plt
from tensor_modelling.tensor_class import tens_obj as to

###### Program
def process(name: str = "CRNM0102-CA_Yosemite_Village_12_W.txt"):
    openfile = open(name,"r")
    
    raw_data = []
    
    for line in openfile:
        grab = line.split("\n")[0].split(" ")
        grab_appn = []
        
        for k in grab:
            if len(k) > 0:
                grab_appn.append(k)
                
        raw_data.append(grab_appn)
                
    openfile.close()
    data = np.array(raw_data, dtype = object)
    #print(data)
    data_processed = []
    
    for i in range(len(data)):
        year = int(data[i,1][:4])
        avg_temp = float(data[i,8])
        month = int(data[i,1][4:6])
        
        data_processed.append([month, year, avg_temp])
        
    data_processed = np.array(data_processed, dtype = object)
    
    min_month = min(data_processed[:,0])
    min_year = min(data_processed[:, 1])
    
    data_processed[:,0] -= min_month
    data_processed[:,1] -= min_year
    
    alpha = to(data = data_processed, column_labels = ["month", "year", "temp"])
    
    alpha.conv_ints([0,1])
    alpha.fill_val([0,1],2)
    
    x = list(range(12))
    
    x_2023 = []
    y_2023 = []
    y_avg = []
    
    for i in range(12):
        grab = alpha.tens[i]
        
        valid_data = []
        
        for j in range(len(grab)):
            if grab[j] > -100:
                valid_data.append(grab[j])
                
        y_avg.append(sum(valid_data)/len(valid_data))
        
        yi_2023 = grab[len(grab) - 1]
        if yi_2023 > -100:
            if i < 7:
                x_2023.append(i)
                y_2023.append(yi_2023)
    
    return x, y_avg, x_2023, y_2023, str(min_year)


names = [
    ["CRNM0102-CA_Yosemite_Village_12_W.txt", "CRNM0102-WI_Necedah_5_WNW.txt"],
    ["CRNM0102-WY_Moose_1_NNE.txt", "CRNM0102-AK_Sand_Point_1_ENE.txt"]]

fig, ax = plt.subplots(ncols = 2, nrows = 2)

for i in range(len(names)):
    for j in range(len(names[i])):
        name = names[i][j]
        
        
        
        x, y_avg, x_2023, y_2023, min_year = process(name)
        
        
        name_proc = name.split(".")[0].split("-")[1] + " " + min_year + " to 2023"
        
        ax[i,j].plot(x, y_avg, label = 'average')
        ax[i,j].plot(x_2023, y_2023, label = '2023')
        ax[i,j].set_title(name_proc)
        
        #ax[i,j].set_xlabel("Month")
        ax[i,j].set_ylabel("Temperature")
        
        
        ax[i,j].text(0.5, 0.5, '@Shugsy', transform=ax[i,j].transAxes,
                fontsize=40, color='gray', alpha=0.2,
                ha='center', va='center', rotation=30)

ax[1,1].set_xlabel("Month")
ax[1,0].set_xlabel("Month")

ax[0,0].legend()

plt.suptitle("Data from: https://www.ncei.noaa.gov/pub/data/uscrn/products/monthly01/")