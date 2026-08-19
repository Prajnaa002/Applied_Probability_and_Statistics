import matplotlib.pyplot as plt

def birthday_problem(n):
    prob = 1
    x = []
    y = []

    for i in range(1,n+1):
        prob *= (365-i+1)/365
        x.append(i)
        y.append(prob*100)

    plt.plot(x,y)
    plt.xlabel("Number of people")
    plt.ylabel("Probability(%)")
    plt.grid()
    plt.show()

birthday_problem(365)


