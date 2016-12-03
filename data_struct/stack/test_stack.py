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

def test_sort_desc():
    mystack = Stack()

    mystack.push(8)
    mystack.push(2)
    mystack.push(5)
    mystack.push(3)
    mystack.push(1)

    assert [1, 3, 5, 2, 8] == [n.data for n in mystack]

    assert [8, 5, 3, 2, 1] == [n.data for n in mystack.sort_desc()]
