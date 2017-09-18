# coding=utf-8
import math

n = 100001
for i in range(n):
    if i % 2 == 1:
        if i % 3 == 0:
            if i % 4 == 1:
                if i % 5 == 4:
                    if i % 6 == 3:
                        if i % 7 == 5:
                            if i % 8 == 1:
                                if i % 9 == 0:
                                    print(i)

                                    # if i > 5000:
                                    #     break
    i = i + 1

# i = 1001
# while i > 0:
#     while i % 2 == 1:
#         while i % 3 == 0:
#             while i % 4 == 1:
#                 while i % 5 == 4:
#                     while i % 6 == 3:
#                         while i % 7 == 5:
#                             while i % 8 == 1:
#                                 while i % 9 == 0:
#                                     print(i)
#     i = i - 1
