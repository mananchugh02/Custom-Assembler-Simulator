import matplotlib.pyplot as plt
import math as m

def plot_graph(cycleN,memAddress):
    
    print("\n")
    plt.scatter(cycleN,memAddress, color='black')
    plt.title('SCATTER PLOT', fontsize=10)
    plt.xlabel('Cycle Number ->', fontsize=10)
    plt.ylabel('Memory Address ->', fontsize=10)
    plt.show()