import sum

def test_sum_recursion():
    sum_of = 10
    expected = 55

    actual = sum.sum_of_number_recursion(sum_of)

    assert expected == actual