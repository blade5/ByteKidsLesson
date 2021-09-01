import xlsxwriter

workbook = xlsxwriter.Workbook('chart.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': 1})
headings = ['Month', 'Education', 'Groceries', 'Entertainment']
worksheet.write_row('A1', headings, bold)

# Write some data to add to plot on the chart.
data = [
    ['January', 'February', 'March', 'April'],
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [3, 6, 9, 12],
]

worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])
worksheet.write_column('D2', data[3])

# Create a new Chart object.
chart = workbook.add_chart({'type': 'column'})

# Configure the chart. In simplest case we add one or more data series.
chart.add_series({
    'name':       '=Sheet1!$B$1',
    'values':     '=Sheet1!$B$2:$B$5',
})

chart.add_series({
    'name':       '=Sheet1!$C$1',
    'values':     '=Sheet1!$C$2:$C$5',
})

chart.add_series({
    'name':       '=Sheet1!$D$1',
    'values':     '=Sheet1!$D$2:$D$5',
})

# Add a chart title and some axis labels.
chart.set_title({'name': 'Monthly Family Expenses'})
chart.set_x_axis({'name': 'Expenses'})
chart.set_y_axis({'name': 'Month'})

# Insert the chart into the worksheet.
worksheet.insert_chart('A7', chart)

workbook.close()
