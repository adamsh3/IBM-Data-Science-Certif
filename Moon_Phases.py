"""Hunter Adams MATH 3450 Homework 5"""

import pandas as pd
from scipy.fft import fft
import numpy as np
import matplotlib.pyplot as plt

cols = [0,1,2]
MoonPhases = pd.read_excel (r'/Users/hunteradams/Desktop/MATH 3450 HW/Moon_Phase_Data.xlsx', usecols = cols)
MoonPhasesIllum = MoonPhases[['Illumination']]
MoonPhasesDist = MoonPhases[['Distance']]
Moon_Illum_Array = np.array(MoonPhases['Illumination'])
Moon_Dist_Array =  np.array(MoonPhases['Distance'])
MoonPhasesIllumFFT = fft(Moon_Illum_Array)
MoonPhasesDistFFT = fft(Moon_Dist_Array)

plt.subplot(211)
plt.plot(MoonPhasesIllum['Illumination'])
plt.title("Illumination of Moon during Phases")
plt.ylabel("Illumination percentage")
plt.subplot(212)
plt.plot(abs(MoonPhasesIllumFFT))
plt.ylabel("Illumination percentage (FFT)")
plt.xlabel("Number of days (1 - 1028)")
plt.show()

plt.subplot(211)
plt.plot(MoonPhasesDist['Distance'])
plt.title("Distance of Moon from Earth (Seattle, WA)")
plt.ylabel("Distance (Miles)")
plt.subplot(212)
plt.plot(abs(MoonPhasesDistFFT))
plt.ylabel("Distance (Miles)(FFT)")
plt.xlabel("Number of days (1 - 1027)")
plt.show()

"""
Explaining the Data: I wanted to analyze moon data for my homework 5. 
I went ahead and graphed both the illumination (phases) and the distance. 
Right off the bat I knew that the illumination was going to be period, but 
when I was looking at the distance data I wasn't too sure if it would be 
periodic, but to my surprise it was. I found the distance graph to be
really cool, because it looks like there are 'big' periods and 'small' periods. 
After talking to James, i learned that the moon and earth are sort of swinging 
each other around the sun throughout the orbit and that is why we see the graph 
that is displayed.
"""

"""
When analyzing the dominant components in illumination, we see a spike at x = 0, x = 36
x = 75, x = 952, x = 991, and x = 1024. All of these can be explained because at these points the
system has more energy there than the other points because with moon phases, the phases are periodic
over a 28 day interval.
When analyzing the dominant components in illumination, we see a spike at x = 0, x = 39, and x = 988. 
Similar to the illumination, this is because the distance is also periodic, however, 
its periodic over a what seems to be a 226 day period (zoomed in on the graph and approx.)
"""

"""
If we were to try and recreate the original data with our FFT, we would simply eliminate any 
modes that are @ 0 or close to zero. In regard to the physical system, this tell us that since its periodic
we are able to cut out the modes that are at zero and the ones that are on the opposite sides of the zero mode.
"""

