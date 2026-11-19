from DataStructures.List import array_list as sll

def new_queue():
    return sll.new_list()

def enqueue(my_queue, element):
    sll.add_last(my_queue, element)
    return my_queue

def dequeue(my_queue):
    if sll.is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty')
    element = sll.remove_first(my_queue)
    return element

def peek(my_queue):
    if sll.is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty')
    return sll.first_element(my_queue)

def is_empty(my_queue):
    return sll.is_empty(my_queue)

def size(my_queue):
    return sll.size(my_queue)