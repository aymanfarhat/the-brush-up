from queue import Queue

def test_enqueue():
    myqueue = Queue()
    
    myqueue.enqueue('one')
    myqueue.enqueue('two')
    myqueue.enqueue('three')
    myqueue.enqueue('four')

    assert ['one', 'two', 'three', 'four'] == [n for n in myqueue]
