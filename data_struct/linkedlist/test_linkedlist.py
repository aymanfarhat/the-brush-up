from linkedlist import Node, LinkedList


def test_single_node():
    mynode = Node('Some data')

    assert 'Some data' == mynode.data

def test_empty_list():
    mylist = LinkedList()

    assert not len(mylist)
    assert not mylist.head

def test_append():
    mylist = LinkedList()

    assert 0 == len(mylist)

    assert 'one' == mylist.append('one').data
    assert 'two' == mylist.append('two').data
    assert 'three' == mylist.append('three').data

    assert 3 == len(mylist)


def test_getitem():
    mylist = LinkedList()

    mylist.append('one')
    mylist.append('two')
    mylist.append('three')

    try:
        mylist['one']
        assert True
    except KeyError:
       assert False

    try:
        mylist['two']
        assert True
    except KeyError:
       assert False, 'Not found!'

    try:
        mylist['something']
        assert False
    except KeyError:
       assert True 


def test_itemsiter():
    mylist = LinkedList()

    assert [] == list(iter(mylist))

    mylist.append('one')
    mylist.append('two')
    mylist.append('three')

    linked_to_list_iter = [n.data for n in mylist]

    assert ['one', 'two', 'three'] == linked_to_list_iter


def test_delete():
    mylist = LinkedList()

    mylist.append('one')
    mylist.append('two')
    mylist.append('three')

    del mylist['two']
    assert ['one', 'three'] == [n.data for n in mylist]

    del mylist['three']
    assert ['one'] == [n.data for n in mylist]

    del mylist['one']
    assert [] == [n.data for n in mylist]

    try:
        del mylist['something']
        assert False
    except KeyError:
        assert True
