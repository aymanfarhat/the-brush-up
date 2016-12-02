from stack import Stack

def test_insert():
    mystack = Stack()

    assert None == mystack.pop()

    mystack.push('mydata')
    mystack.push('mydata2')

    assert 'mydata2' == mystack.pop()
    assert 'mydata' == mystack.pop()
    assert None == mystack.pop()


def test_peek():
    mystack = Stack()

    assert None == mystack.pop()

    mystack.push('mydata')
    mystack.push('mydata2')

    assert 'mydata2' == mystack.peek()
    assert 'mydata2' == mystack.pop()
    assert 'mydata' == mystack.peek()