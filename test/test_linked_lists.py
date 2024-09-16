from linked_lists.linked_lists import Node, LinkedList

def test_create_Node_from_data():
    node = Node("Obj.")
    assert node.data == "Obj."
    node2 = Node("Rhm.")
    assert node2.data == "Rhm."
    node3 = Node(11114)
    assert node3.data == 11114

def test_add_single_node_to_linked_list():
    linked_list = LinkedList()
    linked_list.add("Obj.")
    assert linked_list.head.data == "Obj."

def test_add_two_nodes_to_linked_list():
    linked_list = LinkedList()
    linked_list.add("Obj.")
    assert linked_list.head.data == "Obj."
    linked_list.add("Rhm.")
    assert linked_list.head.next.data == "Rhm."

def test_add_three_nodes_to_linked_list():
    linked_list = LinkedList()
    linked_list.add("Obj.")
    assert linked_list.head.data == "Obj."
    linked_list.add("Rhm.")
    assert linked_list.head.next.data == "Rhm."
    linked_list.add("Jpz.")
    assert linked_list.head.next.data == "Rhm."
    assert linked_list.head.next.next.data == "Jpz."