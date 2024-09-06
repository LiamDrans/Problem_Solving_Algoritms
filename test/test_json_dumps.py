from json_dumps.json_dumps import json_dumps
import json


def test_json_dumps_works_with_single_key_dicts():
    test = {"one": "is a number"}
    assert json_dumps(test) == json.dumps(test)


def test_json_dumps_works_with_long_dictionaries():
    test = {"one": 1, "two": 2, "three": 3}
    test2 = {
        "one": 1,
        "two": 2,
        "three": {"un": 1, "deus": 2, "tres": {"yat": 1, "yee": 2, "san": 3, "say": 4}},
    }
    test_list = [test, test2]
    for test in test_list:
        assert json_dumps(test) == json.dumps(test)


def test_json_dumps_returns_correct_json_with_integers():
    test = {"one": 1}
    test2 = {"one": {2: "two"}}
    test3 = {"one": {"two": {"three": 3}}}
    test_list = [test, test2, test3]
    for test in test_list:
        assert json_dumps(test) == json.dumps(test)


def test_json_dumps_returns_correct_json_with_boolean():
    test = {"one": True}
    test2 = {True: {True: False}}
    test3 = {True: {True: False}, "True": True, False: {False: True}, "False": False}
    test_list = [test, test2, test3]
    for test in test_list:
        assert json_dumps(test) == json.dumps(test)


def test_json_dumps_returns_correct_json_with_list():
    test = {"one": [1]}
    test2 = {True: {True: [1, "2", True]}}
    test3 = {12: [{"inner_key": [True, "True"]}]}
    test4 = {12: [{"inner_key": [{"double_inner": "True"}]}]}
    test5 = {
        12: [
            {
                "inner_key": [
                    {
                        "double_inner": "True",
                        "more_trouble": {"triple_inner": [101, 102]},
                    }
                ]
            }
        ]
    }
    test_list = [test, test2, test3, test4, test5]
    for test in test_list:
        assert json_dumps(test) == json.dumps(test)


def test_json_dumps_returns_correct_json_with_tuple():
    test = {"one": (11, 101, 12, 111)}
    test2 = {
        12: (
            {
                "inner_key": [
                    {
                        "double_inner": "True",
                        "more_trouble": {"triple_inner": [101, 102]},
                    },
                    103,
                ]
            },
            104,
        )
    }
    test_list = [test, test2]
    for test in test_list:
        assert json_dumps(test) == json.dumps(test)


def test_json_dumps_returns_string():
    assert isinstance(json_dumps({"one": {"two": {"three": 3}}}), str)

def test_json_dumps_on_list_returns_correct_result():
    test = [1, 2, 3, 4]
    test2 = [1, 2, [True, "True"]]
    test3 = [1, [2, True], 3 , [4 , False, ["inner_list"]], "five"]
    test4 = [1, 2, {3:4, 5:6, True:False}]
    test5 = [{True: [True, "Rekieta", {False: "False"}, 1], 2:"Two"}, {"final_dict":"wow"}]
    test_list = [test, test2, test3, test4, test5]
    for test in test_list:
        assert json_dumps(test) == json.dumps(test)

def test_json_dumps_on_tuple_returns_correct_result():
    test = (1, 2, 3, 4)
    test2 = (1, 2, (True, "True"))
    test3 = (1, [2, True], 3 , [4 , False, ["inner_list"]], "five")
    test4 = (1, 2, {3:4, 5:6, True:False})
    test5 = ({True: [True, "Rekieta", {False: "False"}, 1], 2:"Two"}, {"final_dict":"wow"})
    test_list = [test, test2, test3, test4, test5]
    for test in test_list:
        assert json_dumps(test) == json.dumps(test)

def test_json_dumps_on_single_element_returns_correct_result():
    test = True
    test2 = 12
    test3 = "String"
    test_list = [test, test2, test3]
    for test in test_list:
        assert json_dumps(test) == json.dumps(test)