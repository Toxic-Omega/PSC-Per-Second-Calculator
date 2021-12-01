import re
import os
import time

print("""
__________  __________________  
\______   \/   _____/\_   ___ \ 
 |     ___/\_____  \ /    \  \/ 
 |    |    /        \\     \____
 |____|   /_______  / \______  /
                  \/         \/ 

    Per Second Calculator
""")
second = int(input("Enter Number : "))
print("")
minute = second * 60
hour = minute * 60
tenhours = hour * 10
day = hour * 24
print(re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', "Per Second : %d" %second))
print(re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', "Per Minute : %d" %minute))
print(re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', "Per Hour : %d" %hour))
print(re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', "Per 10 Hours : %d" %tenhours))
print(re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', "Per Day : %d" %day))
