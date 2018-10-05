from numpy.random import normal
import matplotlib.pyplot as plt

students=[]

i=0

while i<1000:
    students.append(1)
    i+=1
i=0
while i<850:
    students.append(2)
    i+=1
i=0
while i<730:
    students.append(3)
    i+=1
i=0
while(i<621):
    students.append(4)
    i+=1


#n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

n,bins,patched = plt.hist(students, [1,2,3,4,5], density=1)
#plt.axis([1,4,0,1])
plt.xticks([1,2,3,4,5])
plt.grid(True)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

print(students)
