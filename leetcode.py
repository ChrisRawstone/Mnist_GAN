
import openai

openai.Completion.create(
  engine="davinci",
  prompt="Make a list of astronomical observatories:"
)

# class Solution(object):
#     def addTwoN umbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#
#         l1=l1[::-1]
#         l2=l2[::-1]
#
#         l1num =''.join([str(x) for x in l1])
#         l2num =''.join([str(x) for x in l2])
#
#         result1=int(l1num)+int(l2num)
#
#         result2 = [int(x) for x in str(result1)]
#         result2=result2[::-1]
#
#         return result2
#
# yolo=Solution()
#
# print(yolo.addTwoNumbers([1,2,3],[3,4,5]))