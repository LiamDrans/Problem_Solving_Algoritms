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

def test_add_multiple_nodes_to_linked_list():
    linked_list = LinkedList()
    linked_list.add("Obj.")
    first_node = linked_list.head
    linked_list.add("Rhm.")
    second_node = first_node.next
    linked_list.add("Jpz.")
    third_node = second_node.next
    linked_list.add("Wz.")
    fourth_node = third_node.next
    assert second_node.data == "Rhm."
    assert third_node.data == "Jpz."
    assert fourth_node.data == "Wz."
    assert len(linked_list) == 4
    assert linked_list.listing() == ['Obj.', 'Rhm.', 'Jpz.', 'Wz.']
