# Implementing queue using 2 stacks

# 1. This method will make sure that the first entered element stays on the top of stack1
# 2. so, that deQueue operation just pops out from stack1
# 3. To put the element at top of stack1, stack2 is used.

# 4. enQueue(q, x)
#    4.1 while stack1 is not empty, push everything from stack1 to stack2
#    4.2 now, push the new incoming element 'x' to stack1
#    4.3 now, push entire stack2 element to stack1. this way last inserted element will come on top.
#    4.4 Time Complexity : O(n)


# 5. deQueue(q)
#    5.1 if stack1 is empty, then nothing to return 
#    5.2 pop an item from stack1 and return


