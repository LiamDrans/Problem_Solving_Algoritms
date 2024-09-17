import pytest
from linked_lists.linked_lists import Node, LinkedList


@pytest.fixture
def linked_list():
    linked_list = LinkedList()
    linked_list.add("Obj.")
    linked_list.add("Rhm.")
    linked_list.add("Jpz.")
    linked_list.add("Wz.")
    return linked_list


def test_create_Node_from_data():
    node = Node("Obj.")
    assert node.data == "Obj."
    node2 = Node("Rhm.")
    assert node2.data == "Rhm."
    node3 = Node(11114)
    assert node3.data == 11114


def test_add_single_node_to_linked_list():
    test_list = LinkedList()
    test_list.add("Obj.")
    assert test_list.head.data == "Obj."


def test_add_two_nodes_to_linked_list():
    test_list = LinkedList()
    test_list.add("Obj.")
    assert test_list.head.data == "Obj."
    test_list.add("Rhm.")
    assert test_list.head.next.data == "Rhm."


def test_add_multiple_nodes_to_linked_list(linked_list):
    first_node = linked_list.head
    second_node = first_node.next
    third_node = second_node.next
    fourth_node = third_node.next
    assert second_node.data == "Rhm."
    assert third_node.data == "Jpz."
    assert fourth_node.data == "Wz."
    assert len(linked_list) == 4


def test_linked_list_listing(linked_list):
    assert linked_list.listing() == ["Obj.", "Rhm.", "Jpz.", "Wz."]


def test_delete_head_note_of_linked_list(linked_list):
    first_node = linked_list.head
    second_node = first_node.next
    third_node = second_node.next
    linked_list.delete(first_node)
    assert linked_list.head == second_node
    assert linked_list.head.next == third_node


def test_delete_inner_nodes_of_linked_list(linked_list):
    first_node = linked_list.head
    second_node = first_node.next
    third_node = second_node.next
    fourth_node = third_node.next
    linked_list.delete(second_node)
    assert third_node == first_node.next
    assert second_node.next is None
    assert linked_list.listing() == ["Obj.", "Jpz.", "Wz."]
    assert len(linked_list) == 3
    linked_list.delete(third_node)
    assert fourth_node == first_node.next
    assert third_node.next is None
    assert linked_list.listing() == ["Obj.", "Wz."]
    assert len(linked_list) == 2


def test_delete_tail_nodes_of_linked_list(linked_list):
    first_node = linked_list.head
    second_node = first_node.next
    third_node = second_node.next
    fourth_node = third_node.next
    linked_list.delete(fourth_node)
    assert linked_list.listing() == ["Obj.", "Rhm.", "Jpz."]


def test_delete_node_by_string_method_of_linked_list(linked_list):
    linked_list.delete("Rhm.")
    assert linked_list.listing() == ["Obj.", "Jpz.", "Wz."]
    linked_list.delete("Wz.")
    assert linked_list.listing() == ["Obj.", "Jpz."]
    assert len(linked_list) == 2


def test_reverse_nodes_of_linked_list(linked_list):
    linked_list.reverse()
    assert linked_list.listing() == ["Wz.", "Jpz.", "Rhm.", "Obj."]


def test_find_nodes_in_linked_list(linked_list):
    first_node = linked_list.head
    second_node = first_node.next
    third_node = second_node.next
    fourth_node = third_node.next
    assert linked_list.find("Obj.") == (True, 0)
    assert linked_list.find("Jpz.") == (True, 2)
    assert linked_list.find(second_node) == (True, 1)
    assert linked_list.find("KV.") == (False, None)
    assert linked_list.find(fourth_node) == (True, 3)
