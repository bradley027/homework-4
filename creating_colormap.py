# OCNG 689 Python for Geoscientists 
# Kelley Bradley
# HW 4

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def my_cmap(filename):

    '''a function that creates a custom colormap based on a text file downloaded from 
        http://geography.uoregon.edu/datagraphics/color_scales.htm. RGB data will be
        loaded into lists and returns a dictionary of color map data.
        
        new_colormap = my_colormap(____.txt)'''
    
    #creating empty red, green, blue lists 
    r=[]; g=[]; b=[];
    
    #opening txt file with RBG values
    color_nums = open(filename)
    
    #reading RGB data into lists 
    for line in color_nums.readlines()[2:]:
        colors = line.split()
        r.append(float(colors[0]))
        g.append(float(colors[1]))
        b.append(float(colors[2]))
    cmap_len = len(r)
    reds = [((float(n)/(cmap_len-1)),r[n-1],r[n]) for n in range(cmap_len)]
    greens = [((float(n)/(cmap_len-1)),g[n-1],g[n]) for n in range(cmap_len)]
    blues = [((float(n)/(cmap_len-1)),b[n-1],b[n]) for n in range(cmap_len)]
    
    #initializing color dictionary 
    cdict = {'red': reds,
            'green':greens,
            'blue': blues}

    #returns colormap data 
    return matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,256)
    
if __name__ == '__main__': 
    my_cmap = my_cmap('BrBu_10.txt')
    plt.title('Color map plot for BrBu_10.txt', style ='italic' )
    plt.pcolor(np.random.rand(10,10),cmap=my_cmap)
    plt.colorbar()
    plt.show()
    plt.savefig("My_colormap.pdf")