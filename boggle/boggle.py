"""Script to simulate the board game, Boggle"""

def boggle(board, word):
    """Main game function"""

    if not board_checker(board):
        return False
    else:
        indices = board_to_tuples(board)

    print(indices)

    word_lst = [x if x.isalpha() else False for x in word]
    
    if False in word_lst:
        print(False, "invalid word")
        return False
    
    char_indices = {}
    for x in set(word_lst):
        for index in indices:
            if x in index:
                if x in char_indices:
                    char_indices[x].append((index[1], index[2]))
                else:
                    char_indices[x] = [(index[1], index[2])]

    list_indices = []

    for x in word_lst:
        if x not in char_indices:
            print(f"False, '{x}' not in board")
            print("Invalid board")
            return False
        else:
            list_indices.append(char_indices[x])

    all_paths_list = list(cartesian_product(list_indices))

    for path in all_paths_list:
        if path_checker(path):
            return True

    return False


def board_checker(board):
    """Checks whether board is valid or not"""

    valid = True

    for sub_lst in board:
        for char in sub_lst:
            if char.isalpha() is False:
                valid = False
                break

    return valid


def board_to_tuples(board):
    """ "converts the boggle board to a series of character indices"""

    indices = set()
    for i, sub_lst in enumerate(board):
        for j, char in enumerate(sub_lst):
            indices.add((char, i, j))
    return indices


def cartesian_product(ar_list):
    """Takes the list of paths and returns all possible paths through the board"""

    if not ar_list:
        yield ()
    else:
        for a in ar_list[0]:
            for prod in cartesian_product(ar_list[1:]):
                yield (a,) + prod


def path_checker(arg_set):
    """Checks each path through the board to determine if they are all valid moves, i.e. only 1 away in each direction."""

    if len(set(arg_set)) < len(arg_set):
        print(arg_set, False, "dups")
        return False

    direction_list = [
        (i[0] - j[0], i[1] - j[1]) for i, j in zip(arg_set[:-1], arg_set[1:])
    ]

    for direction in direction_list:
        if (
            direction[0] < -1
            or direction[0] > 1
            or direction[1] < -1
            or direction[1] > 1
        ):
            print(arg_set, False, "leaps")
            return False
    print(arg_set, True)
    return True

