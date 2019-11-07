import os
import csv


def csv_writer(row):
    with open('User_Query.csv', 'a')as file:
        writer = csv.writer(file)
        print(row)
        from click import pause
        pause()
        writer.writerows([row])

