def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiou'
    vowels_in_string = []
    position_of_vowels = []
    s_as_list = list(s)

    for i in range(len(s_as_list)):
        if s_as_list[i].lower() in vowels:
            vowels_in_string.append(s_as_list[i])
            position_of_vowels.append(i)

    position_of_vowels.reverse()

    for i in range(len(position_of_vowels)):
        s_as_list[position_of_vowels[i]] = vowels_in_string[i]
        
    return ''.join(s_as_list)
    
