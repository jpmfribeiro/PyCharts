from highcharts.charts.pie_chart import PieChart

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