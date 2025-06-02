#Queue using Collection.dequeue
"""use Dequeue from collection it will append and pop fastly in both end. """
from collections import deque
queue = deque([2,3,4,5,6,8])
print("original queue: ",queue)
print(type(queue))

#Operations
#enqueue at last
queue.append(9)
print("after enqueue :", queue)

#dequeue at first
queue.popleft()
print("after deque: ",queue)
