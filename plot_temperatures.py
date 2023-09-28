import pandas as pd
from matplotlib import pyplot as plt



def read_data_from_file(file_name, num_measurements: int,  
                        column_name) -> list[float]:
    data = pd.read_csv(file_name, nrows=num_measurements)
    return data[column_name]


def compute_statistics(temperatures: list[float], 
                       num_measurements: int) -> float:
    mean = sum(temperatures) / num_measurements
    return mean

def plot_temperatures(temperatures, mean, num_measurements):
    # plot results
    plt.xlabel('Number of measurements')
    plt.ylabel('Air temperature')
    plt.plot(temperatures, "r-")
    plt.axhline(y=mean, color="b", linestyle="--")
    plt.savefig(f"{num_measurements}.png")
    plt.show()
    plt.clf()

for num_measurements in [25, 50, 100]:
    temperatures = read_temperatures_from_file(num_measurements)

    mean = compute_statistics(temperatures, num_measurements)

    plot_temperatures(temperatures, mean, num_measurements)