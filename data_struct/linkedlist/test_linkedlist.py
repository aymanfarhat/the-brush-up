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


def test_prepend():
    mylist = LinkedList()

    mylist.prepend('one')
    mylist.prepend('two')
    mylist.prepend('three')
    mylist.prepend('four')
    mylist.prepend('five')

    assert ['five', 'four', 'three', 'two', 'one'] == [n.data for n in mylist]


def test_reverse_new():
    original_list = LinkedList()

    original_list.append('one')
    original_list.append('two')
    original_list.append('three')
    original_list.append('four')
    original_list.append('five')

    reverse = original_list.reverse_new()

    assert ['five', 'four', 'three', 'two', 'one'] == [n.data for n in reverse]


def test_reverse():
    mylist  = LinkedList()

    mylist.append('one')
    mylist.append('two')
    mylist.append('three')
    mylist.append('four')
    mylist.append('five')

    mylist.reverse()

    assert ['five', 'four', 'three', 'two', 'one'] == [n.data for n in mylist]

    mylist  = LinkedList()

    mylist.append('one')
    mylist.append('two')
    mylist.append('three')

    mylist.reverse()

    assert ['three', 'two', 'one'] == [n.data for n in mylist]

    mylist  = LinkedList()

    mylist.append('one')
    mylist.append('two')

    mylist.reverse()

    assert ['two', 'one'] == [n.data for n in mylist]

    mylist  = LinkedList()

    mylist.append('one')
    mylist.reverse()

    assert ['one'] == [n.data for n in mylist]

def test_remove_duplicates():
    mylist  = LinkedList()

    mylist.append('one')
    mylist.append('two')
    mylist.append('three')
    mylist.append('four')
    mylist.append('five')
    mylist.append('four')
    mylist.append('five')
    mylist.append('five')
    mylist.append('two')

    mylist.remove_duplicates()

    assert ['one', 'two', 'three', 'four', 'five'] == [n.data for n in mylist]

def test_k_last():
    mylist  = LinkedList()

    mylist.append('one')
    mylist.append('two')
    mylist.append('three')
    mylist.append('four')
    mylist.append('five')

    assert 'five' == mylist.get_k_last(1).data
    assert 'three' == mylist.get_k_last(3).data
    assert 'two' == mylist.get_k_last(4).data
    assert 'one' == mylist.get_k_last(5).data

    try:
        mylist.get_k_last(6).data
        assert False
    except KeyError:
        assert True

    try:
        mylist.get_k_last(6).data
        assert False
    except:
        assert True

def test_partition():
    mylist  = LinkedList()

    mylist.append(1)
    mylist.append(3)
    mylist.append(5)
    mylist.append(2)
    mylist.append(8)
    mylist.append(8)
    mylist.append(1)
    mylist.append(4)

    assert [1, 3, 2, 1, 4, 5, 8, 8] == [n.data for n in mylist.partition(4)]
    assert [1, 2, 1, 3, 5, 8, 8, 4] == [n.data for n in mylist.partition(2)]
