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

def test_clear():

    mylist = LinkedList()

    mylist.append('one')
    mylist.append('two')
    mylist.append('three')
    
    mylist.clear()

    assert [] == [n.data for n in mylist]

def test_del_node():
    mylist = LinkedList()

    mylist.append('one')
    mylist.append('two')
    mylist.append('three')
    mylist.append('four')
    mylist.append('five')


    five = mylist['five']

    try:
        mylist.del_node(five)
        assert False
    except KeyError:
        assert True

    one = mylist['one']
    mylist.del_node(one)

    assert ['two', 'three', 'four', 'five'] == [n.data for n in mylist]

    three = mylist['three']
    mylist.del_node(three)

    assert ['two', 'four', 'five'] == [n.data for n in mylist]
    
    four = mylist['four']
    mylist.del_node(four)

    assert ['two', 'five'] == [n.data for n in mylist]
    
    two = mylist['two']
    mylist.del_node(two)

    assert ['five'] == [n.data for n in mylist]
    
    five = mylist['five']
    mylist.del_node(five)

    assert [] == [n.data for n in mylist]
