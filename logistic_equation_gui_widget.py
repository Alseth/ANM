import numpy as np
import matplotlib.pylab as plt

# Logistic equation
def logistic_map(x,r):
    return x*r*(1.0-x)

# Calculate points for Verhaulst diagram
def get_VH_points(r, x=0.5, n=100):
    # Points will be stored in tuple
    
    # Initialization and first point 
    VH_points  = [(x,0)]
    for i in range(n):
        y1 = logistic_map(x,r)
        VH_points.append((x,y1))
        VH_points.append((y1,y1))
        y2 = logistic_map(y1,r)
        VH_points.append((y1,y2))
        x = y1
    return zip(*VH_points)

# Calculate y-points from from logistic equation for x in range(0,1)
def get_function_points(r, n =1000):
    x_vals = np.linspace(0,1,n)
    y_vals = [logistic_map(x,r) for x in x_vals]
    return x_vals, y_vals


# Plotting VerhaulsteÙv diagram 
def plot_VH(r, function_n = 1000, VH_n = 100, VH_x = 0.5):
    func_x_vals, func_y_vals = get_function_points(r=r, n=function_n)
    VH_x_vals, VH_y_vals = get_VH_points(r=r, x = VH_x, n = VH_n)
    
    fig, ax = plt.subplots(figsize = (6,6))
    diagonal_line = ax.plot((0,1), (0,1), color='gray', linewidth=1.35)
    function_line = ax.scatter(func_x_vals,func_y_vals, color= 'r', edgecolor='None', s=1.5)
    VH_line = ax.plot(VH_x_vals,VH_y_vals, color='b', linewidth=1)
    
    ax.set_ylim((0,1))
    ax.set_xlim((0,1))
    
    plt.show()

from Tkinter import *
root = Tk()
r_entry = Entry(root, width=4)
r_entry.pack(side='left')
runit_label = Label(root, text='feedback r')
runit_label.pack(side='left')

def compute():
    # main code
    r = float(r_entry.get())
    plot_VH(r)
    
compute = Button(root, text=' compute ', command=compute)
compute.pack(side='left', padx=4)

root.mainloop()
