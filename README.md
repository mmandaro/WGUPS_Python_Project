# WGUPS_Python_Project

Summary:
A program that reads in address, distance, and package csv files and extracts the data to determine what packages will be delivered from what trucks
and in what order to meet delivery deadlines and not violate any constraints (for example packages that must be delivered together). Package data is
loaded into a chaining hash table, and the nearest neighbor algorithm is used to determine the delivery trucks routes they will take to deliver 
packages on time. A user interface is provided that allows display of all packages after completion and each trucks mileage, all packages status at 
a given time, or any one package status at a given time.

Project Requirements:
-Deliver all packages by their individual deadlines while following all of the constraints given by the special instructions in the package file.

-Use a self adjusting data structure to store package data. This project implements a chaining hash table.

-Ensure the chosen self adjusting data struucture has functions to insert data, update data, delete data, and look up data.

-Provide an interface for the user to view the status and info of any package at any time, and the total mileage traveled by all trucks. 

-Utilize a self-adjusting algorithm to determine a route for the trucks to deliver packages on time. This project implements the nearest neighbor
algorithm.

