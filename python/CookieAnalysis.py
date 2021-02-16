#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from python.MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE
n, bins, patches = plt.hist(times, bins=100,alpha=0.7, fill = True,
hatch='/',histtype='step', linewidth=1, edgecolor='k', density = True)

# plot formating options
plt.xlabel('Time between missing cookies [days]')
plt.ylabel('Probability')
plt.title('rate of' + ' {0:.2f}'.format(rate) + ' cookies / day')
plt.grid(axis='y', alpha=0.75)
plt.yscale('log')
# save figure as a pdf file
plt.savefig('times.pdf')
plt.close()

n, bins, patches = plt.hist(times_avg, bins=100,alpha=0.7, fill = True,
hatch='/',histtype='step', linewidth=1, edgecolor='k', density = True)

# plot formating options
plt.xlabel('Average time between missing cookies [days]')
plt.ylabel('Probability')
plt.title(str(Nmeas)+ ' measurements / experiment with rate'+ 
' {0:.2f}'.format(rate) + ' cookies / day')
plt.grid(axis='y', alpha=0.75)
plt.yscale('log')
# save figure as a pdf file
plt.savefig('times_avg.pdf')
