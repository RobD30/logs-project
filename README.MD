# Welcome to my Logs Project

This project was created using Python version 3.6.1, please see requirements.txt for any further requirements.

### How to Run the program

1. Enter into the logs_project directory and ```run main.py```
2. Enjoy the wonderful output

### What this program do
This program was designed to return the results of several queries and is set up for the ease of use for the user in 
mind. By having to only run the ```main.py``` program it couldn't be easier to see the results you were looking for.

#### Errors So Far

1. Had problems getting it to accept the Password.
2. Had problems with the last query.
3. The most current error is

```Python
C:\Python36\python.exe C:/Users/Rob/PycharmProjects/logs_project/main.py
Top articles:
-------------------------
Traceback (most recent call last):
  File "C:/Users/Rob/PycharmProjects/logs_project/main.py", line 4, in <module>
    top_three_articles.print_top_three_articles()
  File "C:\Users\Rob\PycharmProjects\logs_project\modules\top_three_articles.py", line 25, in print_top_three_articles
    "' are " + formatter.format_num(items[0]) + '.')
IndexError: tuple index out of range

Process finished with exit code 1
```
I continued to have this problem until the teacher showed me the foolish ways of my off by one errors.
4. Now I just had a problem when I refactored changing the directory and project name in pycharm. Fixed it though.
5. After that I had many problems throwing a join in there for no reason I think lol.
6. Then wasn't getting any output at all because I left a ```pass``` in my print function.