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

n,bins,patched = plt.hist(students, [1,2,3,4,5], density=1)

plt.xticks([1,2,3,4,5])
plt.grid(True)
plt.title("Probability Mass Function of Students' Year in College")
plt.xlabel("Random Variable: College Year (1-4)")
plt.ylabel("Probability")
plt.show()
