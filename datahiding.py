class solution:
    __privateCounter = 0

    def sum(self):
        self.__privateCounter += 3
        print(self.__privateCounter)


count = solution()
count.sum()
count.sum()
print(count._solution__privateCounter)


# class Solution:
#     __privateCounter = 0
#
#     def sum(self):
#         self.__privateCounter += 1
#         print(self.__privateCounter)
#
#
# count = Solution()
# count.sum()
# count.sum()
#
# # Here we have accesed the private data
# # member through class name.
# print(count._Solution__privateCounter)

