# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csvpath,data,header=[]):
    """Writes a list of data to a CSV file with optional header arguement.
    Args:
        csvpath (Path): The path to write the csvfile.
        data (list): The list of data to be written to a CSV file.
        header (list, optional): Writes a header row if header arguement is provided 

    Returns:
        An output CSV file and print statement verifying successful saves.
    """
    with open(csvpath, "w") as f:
        csvwriter = csv.writer(f)
        #Writes optional header arguement to file first
        if(header!=[]):
            csvwriter.writerow(header)
        # Write the CSV data
        for row in data:
            csvwriter.writerow(row)
        print(f'Data successfully saved to {csvpath}')