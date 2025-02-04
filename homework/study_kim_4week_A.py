from collections import deque

def find_last_card(n):
    queue=deque(range(1,n+1))               #1~n in queue, range(1,n+1)=>make number list of 1~n
                                            #ex) n=5, queue=deque([1,2,3,4,5])
    while len(queue)>1:                     #rotate before last card is one
        queue.popleft()                     #remove top card   ex) queue=deque([2,3,4,5])
        queue.append(queue.popleft())       #second card->move to the end   ex) queue=deque([3,4,5,2])
        
    return queue[0]                            #return last card

n=int(input("Input the digit: "))
print(find_last_card(n))