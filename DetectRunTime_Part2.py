#Examples how print() amount behaves depending on n:

#Consistant RunTime:

print("Results don't change depending on the parameter n:")
def function1(n):
    print("--- nächstes n: " + str(n) + "---")
    for i in range(1, 6):
        print(str(i) + ". Durchlauf von 5")

for n in range(1, 6):
    function1(n)


#Linear RunTime:

print("Results change depending on the parameter n:")
def function2(n):
    print("--- nächstes n: " + str(n) + "---")

    for i in range(1, n + 1):
        print(str(i) + ". Durchlaufzeiten von " + str(n))

for n in range(1, 6):
    function2(n)

#Squared RunTime:
print("Results change depending on the parameter n^2:")
def function3(n):
    print("--- nächstes n: " + str(n) + "---")

    for j in range(1, n + 1):
        for i in range(1, n + 1):
            print("(i = " + str(i) + ", j = " + str(j) + ") -  Durchlauf, n = " + str(n))

for n in range(1, 6):
    function3(n)

#Plot of the different RunTimes:
import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.arange(1, 6), np.repeat(5, 5), label="Consistant RunTime")
plt.plot(np.arange(1, 6), np.arange(1, 6), label="Linear RunTime")
plt.plot(np.arange(1, 6), np.arange(1, 6) ** 2, label="Squared RunTime")
plt.legend()

plt.xlabel("n")
plt.ylabel("Amount of prints()")
plt.show()
