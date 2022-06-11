import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class Converter():
    '''Converting utility.

    '''
    def __init__(self):
        pass

    def convert_scatter_data(self, points: list, names: dict=None) -> pd.DataFrame():
        '''Convert abstract plot data to pandas dataframe.
            
        Args:
            point (list[tuple]): plots points.

        Kwargs:
            names (tuple): axises names for dataframe.

        Return:
            data (pd.DataFrame): converted data.

        '''
        x_array = []
        y_array = []
        for point in points:
            x_array.append(point[0])
            y_array.append(point[1])
        data = pd.DataFrame({names['x']: x_array, names['y']: y_array})
        return data

class Visualizer():
    '''Utility for visualizing modeling data.

    '''
    def __init__(self, style: str="darkgrid", palette: str="pastel", figsize: tuple=(8, 8), 
                                        space: tuple=(0, 10), names: tuple=('x', 'y'), title: str=None):
        sns.set_theme(style=style)
        sns.color_palette(palette)
        self.plot = plt.plot(figsize=figsize)
        self.conv = Converter()
        self.space = space
        self.names = {'x': names[0], 'y': names[1]}
        self.title = title
        plt.title(title)

    def lineplot_by_equation(self, b, a, color='b'):
        '''Show linear equation on the graph.

        Args:
            b (int): first coefficient.
            a (int): first coefficient.
        
        Kwargs:
            color (str): plot's color.

        '''
        data_x = np.linspace(self.space[0], self.space[1], 100)
        data_y = b + a*data_x
        data = pd.DataFrame({self.names['x']: data_x, self.names['y']: data_y})
        sns.lineplot(x=self.names['x'], y=self.names['y'], data=data, color=color).set_title(self.title)
    
    def scatterplot_by_points(self, points, color='r'):
        '''Show scatterplot by points on the graph.

        Args:
            points (list[tuple]): points of the graph.
        
        Kwargs:
            color (str): plot's color.

        '''
        data = self.conv.convert_scatter_data(points, names=self.names)
        plot = sns.scatterplot(x=self.names['x'], y=self.names['y'], data=data, color=color)
        ticks = np.arange(self.space[0], self.space[1]+1)
        plot.set_xticks(ticks)
        plot.set_yticks(ticks)
        plot.set_title(self.title)

    @staticmethod
    def show():
        '''Show plot.
        
        '''
        plt.show()

def main():
    print("Enter the amount of points")
    n = int(input())
    print("Enter coordinates")
    coords = []
    for i in range(n):
        x, y = map(int, input().split())
        coords.append((x, y))
    print("Enter linear coefficients")
    b, a = map(float, input().split())
    v = Visualizer(space=(0, 5))
    v.lineplot_by_equation(b, a)
    v.scatterplot_by_points(coords)
    v.show()

if __name__ == '__main__':
    main()
