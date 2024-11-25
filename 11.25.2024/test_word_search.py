import word_search

def test_word_search_is_found():
    word_to_search = "hello"
    
    expected = "hello"
    
    actual = word_search.single_word_search(word_to_search)

    assert actual == expected

def test_word_search_is_not_found():
    word_to_search = "pumpkin"

    expected = None

    actual = word_search.single_word_search(word_to_search)

    assert actual == expected
