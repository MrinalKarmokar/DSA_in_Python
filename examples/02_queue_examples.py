from imports import QueueUsingList,  \
                    QueueUsingDeque, \
                    QueueUsingQueue, \
                    CircularQueue

queueusinglist = QueueUsingList()
queueusinglist.enqueue(1)
queueusinglist.enqueue(2)
queueusinglist.enqueue(3)
print(queueusinglist)

queueusingdeque = QueueUsingDeque()
queueusingdeque.enqueue(1)
queueusingdeque.enqueue(2)
queueusingdeque.enqueue(3)
print(queueusingdeque)

queueusingqueue = QueueUsingQueue()
queueusingqueue.enqueue(1)
queueusingqueue.enqueue(2)
queueusingqueue.enqueue(3)
print(queueusingqueue)

circularqueue = CircularQueue(5)
print(circularqueue)
circularqueue.enqueue(1)
circularqueue.enqueue(2)
print(circularqueue)
circularqueue.enqueue(3)
print(circularqueue)
circularqueue.peek()
circularqueue.enqueue(4)
circularqueue.enqueue(5)
# circularqueue.enqueue(6)
print(circularqueue)
circularqueue.peek()
print(circularqueue.dequeue())
print(circularqueue.dequeue())
print(circularqueue.dequeue())
print(circularqueue)

