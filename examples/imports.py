import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from settings import *
from data_structures.stack import StackUsingList, StackUsingDeque, StackUsingLifoQueue
from data_structures.queue import QueueUsingList, QueueUsingDeque, QueueUsingQueue
