

# High Voltage Data Processing Program
#By: Logan Norman

import numpy as np


def processdat(x, y, n, m):
    yerr = []
    ya = []
    xa = []
    xerr = []
    
    #Error and average for 2 cm
    if (n == '20mm' and m == 'GP'):
        for i in range(len(x)):
            ya.append(np.mean(y[i], axis=0))
            xa.append((x[i]+1)*2*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.5**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*2*np.sqrt((.5/x[i])**2+(.1/2)**2)*760.1)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
    
    #Error and average for 1 mm
    if (n == '1mm' and m == 'GP'):
        for i in range(len(x)):
            ya.append(np.mean(y[i], axis=0))
            xa.append((x[i]+1)*.1*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.1**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*.1*np.sqrt((.5/x[i])**2+(.01/.1)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
    
    #Error and average for 1 cm
    if (n == '10mm' and m == 'GP'):
        for i in range(len(x)):
            ya.append(np.mean(y[i], axis=0))
            xa.append((x[i]+1)*1*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.25**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*1*np.sqrt((.5/x[i])**2+(.01/1)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
    
    #Error and average for 5 mm
    if (n == '5mm' and m == 'GP'):
        for i in range(len(x)):
            ya.append(np.mean(y[i], axis=0))
            xa.append((x[i]+1)*.5*760)
            yerr.append(np.sqrt(((np.std(y[i], axis=0)))**2+.1**2+(ya[i]*.11565)**2))
            xerr.append(x[i]*.5*np.sqrt((.5/x[i])**2+(.01/.5)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
        
    #Error and average for 1 mm, Absolute
    if (n == '1mm' and m == 'AP'):
        for i in range(len(x)):
            ya.append(np.mean(y[i], axis=0))
            xa.append(x[i]*.1*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.1**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*.1*np.sqrt((.01/x[i])**2+(.001/.1)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
        
    #Error and average for .1 mm, gauge
    if (n == '0.1mm' and m == 'GP'):
        for i in range(len(x)):
            ya.append(np.mean(y[i], axis=0))
            xa.append((x[i]+1)*.01*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.1**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*.01*np.sqrt((.5/x[i])**2+(.005/.01)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
        
    #Error and average for .1 mm, Absolute
    if (n == '0.1mm' and m == 'AP'):
        for i in range(len(x)):
            ya.append(np.mean(y[i], axis=0))
            xa.append(x[i]*.01*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.02**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*.01*np.sqrt((.01/x[i])**2+(.001/.01)**2)*760)
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
    
    #Error and average for 2 cm
    if (n == '20mm' and m == 'GP'):
        for i in range(len(x)):
            ya.append(np.mean(y[i], axis=0))
            xa.append((x[i]+1)*2*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.5**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*2*np.sqrt((.5/x[i])**2+(.1/2)**2)*760.1)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
    
    #Error and average for 1 mm
    if (n == '1mm' and m == 'GP'):
        for i in range(len(x)):
            ya.append(np.mean(y[i]/.1, axis=0))
            xa.append((x[i]+1)*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.1**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*.1*np.sqrt((.5/x[i])**2+(.01/.1)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
    
    #Error and average for 1 cm
    if (n == '10mm' and m == 'GP'):
        for i in range(len(x)):
            ya.append(np.mean(y[i]/1, axis=0))
            xa.append((x[i]+1)*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.25**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*1*np.sqrt((.5/x[i])**2+(.01/1)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
    
    #Error and average for 5 mm
    if (n == '5mm' and m == 'GP'):
        for i in range(len(x)):
            ya.append(np.mean(y[i]/.5, axis=0))
            xa.append((x[i]+1)*760)
            yerr.append(np.sqrt(((np.std(y[i], axis=0)))**2+.1**2+(ya[i]*.11565)**2))
            xerr.append(x[i]*.5*np.sqrt((.5/x[i])**2+(.01/.5)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
        
    #Error and average for 1 mm, Absolute
    if (n == '1mm' and m == 'AP'):
        for i in range(len(x)):
            ya.append(np.mean(y[i]/.1, axis=0))
            xa.append(x[i]*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.1**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*.1*np.sqrt((.01/x[i])**2+(.01/.1)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
        
    #Error and average for .1 mm, Gauge
    if (n == '0.1mm' and m == 'GP'):
        for i in range(len(x)):
            ya.append(np.mean(y[i]/.01, axis=0))
            xa.append((x[i]+1)*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.1**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*.01*np.sqrt((.5/x[i])**2+(.01/.005)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
        
    #Error and average for .1 mm, Absolute
    if (n == '0.1mm' and m == 'AP'):
        for i in range(len(x)):
            ya.append(np.mean(y[i]/.01, axis=0))
            xa.append(x[i]*760)
            yerr.append(np.sqrt((np.std(y[i], axis=0)**2+.1**2+(ya[i]*.11565)**2)))
            xerr.append(x[i]*.01*np.sqrt((.01/x[i])**2+(.01/.005)**2)*760)
        coeffs = np.polyfit(x, ya, 1)
        trend = np.poly1d(coeffs)
        ya=np.array(ya)*1000
        yerr=np.array(yerr)*1000
       

    return ya, yerr, xa, xerr
