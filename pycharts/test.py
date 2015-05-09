from pycharts.charts.pie_chart import PieChart
from pycharts.charts.stacked_bar_chart import StackedBarChart
from highcharts_plotter import HighChartsPlotter

data = [
                    ['Firefox',   45.0],
                    ['IE',       26.8],
                    ['Chrome', 12.8],
                    ['Safari',    8.5],
                    ['Opera',     6.2],
                    ['Others',   0.7]
        ]

data_label = "Browser share"

title = "Browser market shares at a specific website, 2014"

piechart = PieChart(title, data_label, data)

print piechart.to_javascript()

title2 = "How do tourists spend their money?"

categories2 = ['Americans', 'Italians', 'Chinese', 'Brazilians', 'Germans']

data2 = [
                ('Bakery', [5, 3, 4, 7, 2]),
                ('Bars and Restaurants', [2, 2, 4, 3, 8]),
                ('Shopping', [10, 8, 7, 6, 9]),
                ('Jewelry', [5, 5, 2, 3, 3]),
                ('Hotel', [8, 8, 6, 7, 6])
]

y_title2 = 'Total money spent'

stackedchart = StackedBarChart(title2, categories2, data2, y_title=y_title2)

print stackedchart.to_javascript()

plotter = HighChartsPlotter()
plotter.plot(stackedchart)