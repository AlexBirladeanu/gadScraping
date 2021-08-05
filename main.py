import csv

with open('deniro.csv') as csv_file:
    standings = []

    csv_rows = csv.reader(csv_file)
    csv_rows = list(csv_rows)

    columns = csv_rows[0]

    for row in csv_rows[1:]:
        standings.append({
            column: value for column, value in zip(columns, row)
        })

with open('deniro.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file)
    new_row = ['2019', ' 100', "The Irishman"]
    standings.append({
        column: value for column, value in zip(columns, new_row)
    })
    csv_writer.writerows([team_data.values() for team_data in standings])


for i in standings:
    print(i)
