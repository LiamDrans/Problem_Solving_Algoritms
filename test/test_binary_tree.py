import pytest
from src.binary_tree import BinaryTree, Node

@pytest.fixture
def binary_tree():

    binary_tree = BinaryTree()
    tree_list = [
        "Obj.",
        "Leffe.",
        "Rhm.",
        "Lewelyn.",
        "Lerix.",
        "Relic.",
        "Rhein.",
        "Lullaby.",
    ]
    for i in tree_list:
        binary_tree.append(i)
    return binary_tree


def test_creation_of_binary_tree():

    test_tree = BinaryTree("Obj.")
    assert isinstance(test_tree.root, Node)
    assert test_tree.root.data == "Obj."


def test_appends_to_left_and_right_of_root_in_binary_tree():

    test_tree = BinaryTree()
    tree_list = ["Obj.", "Leffe.", "Rhm."]
    for i in tree_list:
        test_tree.append(i)
    assert isinstance(test_tree.root.left, Node)
    assert isinstance(test_tree.root.right, Node)
    assert test_tree.root.left.data == "Leffe."
    assert test_tree.root.right.data == "Rhm."


def test_appends_to_multiple_levels_of_the_binary_tree(binary_tree):

    assert binary_tree.root.left.data == "Leffe."
    assert binary_tree.root.right.data == "Rhm."
    assert binary_tree.root.left.left.data == "Lewelyn."
    assert binary_tree.root.left.right.data == "Lerix."
    assert binary_tree.root.right.left.data == "Relic."
    assert binary_tree.root.right.right.data == "Rhein."
    assert binary_tree.root.left.left.left.data == "Lullaby."
    assert binary_tree.len == 8

def test_find_on_binary_tree(binary_tree):

    assert binary_tree.find("Lerix.") == ("Lerix.", 5)
    assert binary_tree.find("Lullaby.") == ("Lullaby.", 8)
    assert binary_tree.find("Obj.") == ("Obj.", 1)
    binary_tree.append("Luluru.")
    assert binary_tree.find("Luluru.") == ("Luluru.", 9)


def test_adding_100_to_binary_tree_and_using_find():
    test_tree = BinaryTree()
    for i in range(100)[1:]:
        test_tree.append(i)
    test_tree.append("Obj.")
    assert test_tree.find(64) == (64, 64)
    assert test_tree.find("Obj.") == ("Obj.", 100)

def test_delete_root_node(binary_tree):
    binary_tree.delete("Obj.")
    assert binary_tree.find("Obj.") is False
    assert binary_tree.root.data == "Lullaby."
    assert binary_tree.len == 7
    assert binary_tree.root.right.data == "Rhm."
    assert binary_tree.root.left.data == "Leffe."

def test_delete_position_5_node(binary_tree):
    binary_tree.delete("Lerix.")
    assert binary_tree.find("Lerix.") is False
    assert binary_tree.find("Lullaby.") == ("Lullaby.", 5)
    assert binary_tree.len == 7

def test_delete_end_node(binary_tree):
    binary_tree.delete("Lullaby.")
    assert binary_tree.find("Lullaby.") is False
    assert binary_tree.len == 7

def test_delete_position_3_node(binary_tree):
    binary_tree.delete("Rhm.")
    assert binary_tree.find("Lullaby.") == ("Lullaby.", 3)
    assert binary_tree.find("Relic.") == ("Relic.", 6)
    assert binary_tree.find("Rhein.") == ("Rhein.", 7)