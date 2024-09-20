import pytest
from binary_tree.binary_tree import BinaryTree, Node

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