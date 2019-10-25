def phrase_search(example_objects: list, str_to_find: str) -> int:
    for example_object in example_objects:

        id = int(example_object.get('id'))
        phrase = str(example_object.get('phrase')).lower()
        slots = list(example_object.get('slots'))
        str_to_find = str_to_find.lower()

        if not len(example_object) > 0 \
                or not (id > 0) \
                or not len(phrase) <= 120 \
                or not len(slots) <= 50:
            pass

        # if template in string
        if ("{" in phrase) and ("}" in phrase):

            # if one variable
            if phrase.count("{") == 1:
                for x in slots:
                    if str_to_find in (phrase.split("{")[0]+"{}").format(x.lower()):
                        return id

            # if two variables
            elif phrase.count("{") == 2:
                for x in slots:
                    for y in slots:
                        if str_to_find in (phrase.split("{")[0]+"{}" + phrase.split("{")[1].split("}")[1]+"{}").format(x.lower(),y.lower()):
                            return id

        # or simple string without variables
        elif str_to_find in phrase:
            return id

    # nothing found
    return 0

if __name__ == "__main__":
    """ 
    len(object) != 0
    object["id"] > 0
    0 <= len(object["phrase"]) <= 120
    0 <= len(object["slots"]) <= 50
    """
    object = [
        {"id": 1, "phrase": "Hello world!", "slots": []},
        {"id": 2, "phrase": "I wanna {pizza}", "slots": ["pizza", "BBQ", "pasta"]},
        {"id": 3, "phrase": "Give me your power", "slots": ["money", "gun"]},
        {"id": 4, "phrase": "I wanna {eat} and {drink}", "slots": ["pizza", "BBQ", "pepsi", "tea"]},
    ]

    assert phrase_search(object, 'I wanna pasta') == 2
    assert phrase_search(object, 'Give me your power') == 3
    assert phrase_search(object, 'Hello world!') == 1
    assert phrase_search(object, 'I wanna nothing') == 0
    assert phrase_search(object, 'Hello again world!') == 0
    assert phrase_search(object, 'I need your clothes, your boots & your motorcycle') == 0
    assert phrase_search(object, 'I wanna BBQ and tea') == 4



