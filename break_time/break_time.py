import webbrowser
import time

total_breaks = 3
break_count = 0

print("Program started on " + time.ctime())
while (break_count < total_breaks):
    time.sleep(3)
    webbrowser.open(
        "https://www.youtube.com/watch?v=GyiQtznyCGU&list=PLvRupt4A76wA0tGOqo2gksWwo4U3Q6Kcm")
    break_count += 1
