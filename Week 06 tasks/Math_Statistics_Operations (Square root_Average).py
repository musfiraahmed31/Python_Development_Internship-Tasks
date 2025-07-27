import math
import statistics

Numbers = [4, 9, 16, 25, 36]

SquareRoots = [math.sqrt(num) for num in Numbers]
print("Square Roots:", SquareRoots)

Average = statistics.mean(Numbers)
print("Average of the list:", Average)
