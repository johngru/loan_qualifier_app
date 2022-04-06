# Qualifying Loan Application

![Growth of money over time](https://cdn.pixabay.com/photo/2017/08/30/07/52/money-2696219_1280.jpg)

This application compares a potential borrower's financial background against a database of lenders and their associated acceptance criteria for approval.  It returns a list of lenders that will accept the borrower's lending criteria.  Additionally, it prompts the user to save the qualifying loan list as a new CSV file, which is a new feature in this update.

---

## Technologies

This project is written using ```Python 3.7.11```.  Key libraries include ```fire 0.4.0``` for the interactive CLI, ```questionary 1.10.0``` for user prompts, and standard python packages for file name management ```pathlib```, csv file management ```csv```, and program exit control ```sys```.    

---

## Installation Guide

Before running the application, first install the following packages if you don't already have them installed in your development environment.

```python
  pip install fire
  pip install questionary
```
The run file of the application is ```app.py```.  To run, simply type the following in terminal:
```python
python app.py
``` 

---

## Usage

This application takes known lender acceptance criteria from a group of lenders and compares a potential borrower's financial metrics against this group.  It then populates a list of lenders that would accept the borrower's loan request.  The resultant lender list can be then be saved to a CSV file at a specified file location.

## To Start
To run the application, open a terminal, ```cd``` into the top directory of the files containing ```app.py```, and then simply type:
```python
python app.py
```
## Program flow

You will then be prompted to enter a file path to the group of lender rates.  The default, sample rate sheet is in the subfolder ```data``` and has file path ```./data/daily_rate_sheet.csv```.  After entering the path, press ```Enter```.

Next you will be prompted to enter the potential borrower's financial criteria for loan acceptance.  You will be asked to enter items such as credit score, total monthly debt, total montly income, desired loan amount, and the borrower's home value.  After each prompt, press ```Enter```.
After the question prompts, the application compares these criteria with the group of lenders and outputs a list of the subset of lenders that accept the conditions of the loan for the borrower.  

## Saving your work

You will be asked if you would like to save the qualifying loans to a CSV file.  To exit without saving, simply type ```n```, and the application will exit without saving.
To save the qualifying lenders to a CSV file, type ```Y```, and you will be prompted to enter the path and file name for the output file.  Make sure to include the *.csv extension to the end of your filename.  
After entering the path and filename, press ```Enter```.  The application will output a successful save notification and then exit.  Your output file will be located at the file location you specified at the prompt.

---

## Contributors

The seed code is from the course material from a UCBerkeley Extension program.  This updated version is written by John Gruenewald.<br><br>
For more information, contact **John Gruenewald**:<br>
**e-mail:** [john.h.gruenewald@gmail.com](mailto:john.h.gruenewald@gmail.com)<br> **linked-in:**  [jhgruenewald](https://www.linkedin.com/in/jhgruenewald/)<br>**twitter:**  [@GruenewaldJohn](https://twitter.com/GruenewaldJohn)<br>**medium:**  [@comput99](https://medium.com/@comput99)

---

## License

MIT License

Copyright (c) 2022 John Gruenewald
