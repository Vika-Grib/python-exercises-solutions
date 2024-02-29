"""3.	Вывести на экран следующую последовательность символов:
	* * * * * * *
	  * * * * *
	    * * *
	      *
	    * * *
	  * * * * *
	* * * * * * *
"""

n = 7
sym = '*'

for i in range(n, 0, -2):
    s = str(sym * i) #sym*заданное количество раз i-тое
    space_count = int((n - i)/2)  # i = len(s), т.е. int((n - len(s))/2)
    s = s.rjust(space_count + i) #должно указывать на общее число символов в строк, а не только на пробелы, поэтому у множаем на i
    print(s)
for i in range(3, n+1, 2):
    s = str(sym * i)
    space_count = int((n - i)/2)
    s = s.rjust(space_count + i)
    print(s)