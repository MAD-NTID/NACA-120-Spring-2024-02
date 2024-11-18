import my_functions

def test_get_area_circle():
    radius = 5
    expected = 78.53981633974483

    result = my_functions.get_area_circle_with_radius(radius)

    assert result == expected

def test_get_area_rectangle():
    length = 6
    width = 4
    expected = 24

    result = my_functions.get_area_rectangle(length, width)

    assert result == expected