from numpy.random import normal
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

students=[]
mergedStudents=[]
i=1
year=1
fig = plt.Figure()

while i<=3190:
    if  i == 1001:
        year=2
    elif i == 1851:
        year=3
    elif i == 2574:
        year=4
    students.append(year)
    mergedStudents.append(year)
    i+=1
i=1
year=6
while i<=190:
    if i == 40:
        year=7
    elif i == 90:
        year=8
    mergedStudents.append(year)
    i+=1

cdf = fig.add_subplot(211)
n,bins,patched = plt.hist(students, [1,2,3,4,5], density=1, color='green')

plt.xticks([1,2,3,4,5])
plt.grid(True)
plt.title("Probability Mass Function of Students' Year in College")
plt.xlabel("Random Variable: College Year (1-4)")
plt.ylabel("Probability")
plt.show()

plt.hist(students, [1,2,3,4,5], density=1, color='cyan', cumulative=True)

plt.xticks([1,2,3,4,5])
plt.grid(True)
plt.title("Cumulative Distribution Function")
plt.xlabel("Random Variable: College Year (1-4)")
plt.ylabel("Probability")

plt.show()

######################
## To Find the Mean And Standard Deviation/Variance



## Mean
print("The expected year (mean) of a student is:",int(np.mean(students)))

## Standard Deviation/Variance
print("The Variance of the year of students is:",np.std(students))

################
## Finding the median & mode of both universities

## medians
print("Median of University A:",np.median(students))
print("Median of University B:",np.median(mergedStudents))

## modes

print("Mode of University A:",stats.mode(students))
print("Mode of University B:",stats.mode(mergedStudents))