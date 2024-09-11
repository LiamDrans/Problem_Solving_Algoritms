from boggle.boggle import boggle


def test_board_word_invalid_characters():
    assert boggle([["3", "h"],
                   ["l", "1"]], "helo") == False
    assert boggle([["e", "h"],
                   ["l", "l"]], "h311") == False


def test_boggle_2x2_square():
    board = [["e", "l"], ["l", "h"]]
    assert boggle(board, "hell") == True
    assert boggle(board, "hole") == False
    assert boggle(board, "heel") == False
    assert boggle(board, "lelh") == True


def test_boggle_3x3_square():
    board = [["e", "l", "b"], ["l", "h", "o"], ["o", "w", "a"]]
    assert boggle(board, "hollow") == True
    assert boggle(board, "lelhowao") == True
    assert boggle(board, "heelo") == False
    assert boggle(board, "xuyzy") == False


def test_boggle_4x4_square():
    board = [
        ["e", "s", "d", "d"],
        ["n", "a", "d", "z"],
        ["i", "a", "d", "z"],
        ["z", "y", "o", "r"],
    ]
    assert boggle(board, "enaz") == True
    assert boggle(board, "ddddzzr") == True
    assert boggle(board, "ziayo") == True
    assert boggle(board, "heelo") == False
    assert boggle(board, "xuyzy") == False
