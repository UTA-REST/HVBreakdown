

# High Voltage Data Processing Program
#By: Logan Norman

import numpy as np


def processdat(x, y, n, m):
    yerr = []
    ya = []
    xa = []
    xerr = []

    if (m =='GP'):
        offset=1 #Gauge Pressure
        gerr=.5
    if (m =='AP'):
        offset=0 #Absolute Pressure 
        gerr=.01
    #Error and average for 2 cm
    if (n == '20mm'):
        for i in range(len(x)):
            ya.append(np.mean(y[i], axis=0))
            xa.append((x[i]+offset)*2*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.5**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*2*np.sqrt((gerr/x[i])**2+(.1/2)**2)*760.1)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
    
    #Error and average for 1 mm
    if (n == '1mm'):
        for i in range(len(x)):
            ya.append(np.mean(y[i], axis=0))
            xa.append((x[i]+offset)*.1*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.1**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*.1*np.sqrt((gerr/x[i])**2+(.01/.1)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
    
    #Error and average for 1 cm
    if (n == '10mm'):
        for i in range(len(x)):
            ya.append(np.mean(y[i], axis=0))
            xa.append((x[i]+offset)*1*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.25**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*1*np.sqrt((gerr/x[i])**2+(.01/1)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
    
    #Error and average for 5 mm
    if (n == '5mm'):
        for i in range(len(x)):
            ya.append(np.mean(y[i], axis=0))
            xa.append((x[i]+offset)*.5*760)
            yerr.append(np.sqrt(((np.std(y[i], axis=0)))**2+.1**2+(ya[i]*.11565)**2))
            xerr.append(x[i]*.5*np.sqrt((gerr/x[i])**2+(.01/.5)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
        
    #Error and average for .1 mm
    if (n == '0.1mm'):
        for i in range(len(x)):
            ya.append(np.mean(y[i], axis=0))
            xa.append((x[i]+offset)*.01*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.1**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*.01*np.sqrt((gerr/x[i])**2+(.005/.01)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
        
        
    return ya, yerr, xa, xerr, trend

def processdatE(x, y, n, m):
    yerr = []
    ya = []
    xa = []
    xerr = []
    
    if (m == 'GP'):
        offset=1 #Gauge Pressure
        gerr=.5
    if (m == 'AP'):
        offset=0 #Absolute Pressure
        gerr=.01
    
    #Error and average for 2 cm
    if (n == '20mm'):
        for i in range(len(x)):
            ya.append(np.mean(y[i], axis=0))
            xa.append((x[i]+offset)*2*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.5**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*2*np.sqrt((gerr/x[i])**2+(.1/2)**2)*760.1)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
    
    #Error and average for 1 mm
    if (n == '1mm'):
        for i in range(len(x)):
            ya.append(np.mean(y[i]/.1, axis=0))
            xa.append((x[i]+offset)*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.1**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*.1*np.sqrt((gerr/x[i])**2+(.01/.1)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
    
    #Error and average for 1 cm
    if (n == '10mm'):
        for i in range(len(x)):
            ya.append(np.mean(y[i]/1, axis=0))
            xa.append((x[i]+offset)*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.25**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*1*np.sqrt((gerr/x[i])**2+(.01/1)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
    
    #Error and average for 5 mm
    if (n == '5mm'):
        for i in range(len(x)):
            ya.append(np.mean(y[i]/.5, axis=0))
            xa.append((x[i]+offset)*760)
            yerr.append(np.sqrt(((np.std(y[i], axis=0)))**2+.1**2+(ya[i]*.11565)**2))
            xerr.append(x[i]*.5*np.sqrt((gerr/x[i])**2+(.01/.5)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
        
    #Error and average for .1 mm
    if (n == '0.1mm'):
        for i in range(len(x)):
            ya.append(np.mean(y[i]/.01, axis=0))
            xa.append((x[i]+offset)*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.1**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*.01*np.sqrt((gerr/x[i])**2+(.01/.005)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000

    return ya, yerr, xa, xerr, trend
