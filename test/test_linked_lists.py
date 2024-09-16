from linked_lists.linked_lists import Node, LinkedList

def test_create_Node_from_element():
    node = Node("Obj.")
    assert node.element == "Obj."
    node2 = Node("Rhm.")
    assert node2.element == "Rhm."
    node3 = Node(11114)
    assert node3.element == 11114

def test_create_add_single_node_to_linked_list():
    linked_list = LinkedList()
    linked_list.add("Obj.")
    assert linked_list._head.element == "Obj."