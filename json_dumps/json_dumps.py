"""Program to perform the function of json.dumps on dictionary objs featuring recursive logic"""


def json_dumps(obj, separators=(',',':')):
    """Takes the dictionary to be converted to json format"""

    json_string = ""

    if isinstance(obj, dict):

        dictionary = obj
        dict_counter = 0

        for key in dictionary:

            dict_counter += 1
            json_key = key_to_json(key)

            if isinstance(dictionary[key], dict):

                json_string = json_dict(
                    json_key,
                    json_dumps(dictionary[key]),
                    dict_counter,
                    len(dictionary),
                    json_string,
                    separators
                )

            elif isinstance(dictionary[key], (list, tuple)):
                json_key = key_to_json(key)
                json_string = json_dict(json_key, json_dumps(dictionary[key]), dict_counter, len(dictionary), json_string, separators)

            else:
                json_key = key_to_json(key)
                json_value = value_to_json(dictionary[key])

                json_string = json_dict(
                    json_key, json_value, dict_counter, len(dictionary), json_string, 
                separators)

    elif isinstance(obj, (list, tuple)):

        list_counter = 0

        for item in obj:
            list_counter += 1

            if isinstance(item, (list, tuple, dict)):
                json_string = json_list(json_dumps(item), list_counter, len(obj), json_string, separators)

            else:
                json_item = value_to_json(item)
                json_string = json_list(str(json_item), list_counter, len(obj), json_string, separators)
    
    else:
        json_obj = value_to_json(obj)
        json_string += str(json_obj)

    return json_string


def key_to_json(key):
    """Converts the key of the json into what is expected in the json format - i.e. bool True -> true"""

    return [str(key).lower() if isinstance(key, bool) else key][0]

def value_to_json(value):
    """Converts the key of the json into what is expected in the json format - i.e. ..."""

    return [
        (
            f'"{value}"'
            if isinstance(value, str)
            else (str(value).lower() if isinstance(value, bool) else value)
        )
    ][0]


def json_dict(key, value, counter, length, json_string, separators):
    """Contains the string logic for converting a dictionary obj into json format"""

    if json_string == "" and length == 1:
        json_string += f'\u007b"{key}"{separators[1]} {value}\u007d'
    elif counter == 1:
        json_string += f'\u007b"{key}"{separators[1]} {value}{separators[0]} '
    elif length == counter:
        json_string += f'"{key}"{separators[1]} {value}\u007d'
    else:
        json_string += f'"{key}"{separators[1]} {value}{separators[0]} '

    return json_string

def json_list(item, counter, length, json_string, separators):
    """Contains the string logic for converting a base list into json format"""

    if length == 1:
        json_string += f"[{item}]"
    elif length > 1 and counter == 1:
        json_string += f"[{item}{separators[0]} "
    elif counter == length:
        json_string += f"{item}]"
    else:
        json_string += f"{item}{separators[0]} "
    
    return json_string

