def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_dict = {}
    while len(phrase) > 0:
        letter_dict[phrase[0]] = phrase.count(phrase[0])
        phrase = phrase.replace(phrase[0],'')
    return letter_dict