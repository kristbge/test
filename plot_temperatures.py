import pandas as pd
from matplotlib import pyplot as plt
from my_statistics import compute_statistics
import click 



@click.command()
@click.option('--num_measurements', help='Number of temperatures to read and plot', type=int, required=True)
@click.option('--inputfile', help= 'The inpuyt data file', requried=True)
@click.option('--inputfile', help= 'The output image file name', requried=True)

def main(num_measurements, inputfile, outputfile):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")


    def read_data_from_file(file_name, num_measurements: int,  
                            column_name) -> list[float]:
        data = pd.read_csv(file_name, nrows=num_measurements)
        return data[column_name]


    def plot_temperatures(temperatures, mean, outputfile):
        # plot results
        plt.xlabel('Number of measurements')
        plt.ylabel('Air temperature')
        plt.plot(temperatures, "r-")
        plt.axhline(y=mean, color="b", linestyle="--")
        plt.savefig(f"{num_measurements}.png")
        #plt.show()
        plt.clf()

    for num_measurements in [25, 50, 100]:
        temperatures = read_data_from_file(inputfile, num_measurements, outputfile)

        mean = compute_statistics(temperatures, num_measurements)

        plot_temperatures(temperatures, mean, num_measurements)

if __name__ == '__main__':
