# P3 Logs Analysis

A python script run the sql scripts and return answers for 3 questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Views created in this project
For code readability, 3 views are created for question 3.
However, all the views created are temporary. They are created by python codes. Therefore every time you run the script, the temporary views will be created automatically.
Views:
failure - date and number of failed requests for each date
success - date and number of successful requests for each date;
failure_rate - date and failure rate for each date;

## Requirement
1. Computer (Mac or Windows OS)
2. Python 3.6.1 or above
3. Knowledge of command line

## Instruction
1. Open a terminal
2. Change to the project directory that contains python scripts.
3. Type "python main.py" in the terminal and the answers to the 3 questions should be displayed automatically to the terminal.
4. Enjoy!
