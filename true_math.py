import math
from math import inf
def true_divide(first,second):
    if second != 0:
        div_true = first / second
        return div_true
    else:
        return math.inf

# result3 = true_divide(49, 7)
# result4 = true_divide(15, 0)
#
# print(result3)
# print(result4)