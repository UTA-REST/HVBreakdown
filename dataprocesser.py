

# High Voltage Data Processing Program
#By: Logan Norman

import numpy as np

# Processing Function for Voltage Breakdown Data
# Input (x,y,n,m) = (Pressure (bar) , Voltage (kV), Electrode Seperation Distance (String), Pressure Range (String))
# Output (ya, yerr, xa, xerr, trend) = (Averaged Voltage (V), Voltage Error (V), Adjusted Pressure-Length (torr-cm), Pressure-Length Error (torr-cm), Trend line for data)

def processdat(x, y, n, m):
    yerr = []
    ya = []
    xa = []
    xerr = []

    if (m =='GP'):
        offset=1   # Gauge Pressure Offset
        gprec=.25*760    # Gauge Precision, torr
    if (m =='AP'):
        offset=0   # Absolute Pressure Offset
        gprec=.01*760   # Gauge Precision, torr
        
    d = float(n.replace('mm','')) # Convert distance to integer
    
    hysterr = .06 # hysteresis error, found by experiment
    
    timeerr = .06 # Time correction Factor
    
    if (n == '10mm'):
        ecorr = .06 # E field Correction Factor for 10 mm
        vprec = .1 # Voltage Gauge Precision +/- 0.1 kiloVolt
    if (n == '5mm'):
        ecorr = .03 # E field Correction Factor for 5 mm
        vprec = .1 # Voltage Gauge Precision +/- 0.1 kiloVolt
    if (n == '1mm'):
        ecorr = .01 # E field Correction Factor for 1 mm
        vprec = .1 # Voltage Gauge Precision +/- 0.1 kiloVolt
    if (n == '2mm'):
        ecorr = .01 # E field Correction Factor for 1 mm
        vprec = .1 # Voltage Gauge Precision +/- 0.1 kiloVolt
    if (n == '0.1mm'):
        ecorr = 0 # E field Correction Factor for 0.1 mm
        vprec = 0.005 #Voltage Gauge Precision for multimeter, +/- 5 Volts

    for i in range(len(x)):
        ya.append(np.mean(y[i], axis=0))
        xa.append((x[i]+offset)*d/10*760)  # offset adjustment and unit conversion, bar -> torr-cm
        yerr.append(ya[i]*np.sqrt((np.std(y[i], axis=0)/ya[i])**2+(vprec/ya[i])**2+(hysterr/ya[i])**2+timeerr**2+ecorr**2))  # Error Calculation for Voltage
        xerr.append(xa[i]*d/10*np.sqrt((gprec/xa[i])**2+(.1/(d/10))**2))  # Error Calculation for Pressure-Length
    coeffs = np.polyfit(x, ya, 1)
    trend = np.poly1d(coeffs)
    ya=np.array(ya)*1000  # Unit Conversion, V -> kV
    yerr=np.array(yerr)*1000  # Unit Conversion, V -> kV
        
    return ya, yerr, xa, xerr, trend
