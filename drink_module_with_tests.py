# -*- coding: utf-8 -*-
# drink_module.py

def validate_drink_input(input_string):
    """
    Valida el ingreso de una nueva bebida según las especificaciones dadas.
    """
    parts = ''.join(input_string.split()).split(',')
    
    if not parts[0].isalpha() or not (2 <= len(parts[0]) <= 15):
        return False
    
    if len(parts) < 2 or len(parts) > 6:
        return False
    
    try:
        sizes = list(map(int, parts[1:]))
        if not all(1 <= size <= 48 for size in sizes):
            return False
        if sorted(sizes) != sizes:
            return False
    except ValueError:
        return False
    
    return True

# A continuación, los casos de prueba.

def test_invalid_input_1():
    assert not validate_drink_input("Tea")
    print("test_invalid_input_1 passed!")

def test_invalid_input_2():
    assert not validate_drink_input("123Coffee,1,2,3")
    print("test_invalid_input_2 passed!")

def test_invalid_input_3():
    assert not validate_drink_input("Latte,-1,0")
    print("test_invalid_input_3 passed!")

def test_valid_drink_name():
    assert validate_drink_input("Latte,1,2,3")
    print("test_valid_drink_name passed!")

def test_invalid_drink_name_short():
    assert not validate_drink_input("L,1,2,3")
    print("test_invalid_drink_name_short passed!")

def test_invalid_drink_name_long():
    assert not validate_drink_input("VeryLongDrinkName,1,2,3")
    print("test_invalid_drink_name_long passed!")

def test_valid_sizes():
    assert validate_drink_input("Latte,1,2,3,4,5")
    print("test_valid_sizes passed!")

def test_invalid_size_order():
    assert not validate_drink_input("Latte,1,3,2")
    print("test_invalid_size_order passed!")

def test_invalid_size_value():
    assert not validate_drink_input("Latte,0,49")
    print("test_invalid_size_value passed!")

def test_invalid_non_integer_size():
    assert not validate_drink_input("Latte,1,2.5")
    print("test_invalid_non_integer_size passed!")

def test_valid_with_spaces():
    assert validate_drink_input(" Latte , 1 , 2 , 3 ")
    print("test_valid_with_spaces passed!")

def test_more_than_five_sizes():
    assert not validate_drink_input("Latte,1,2,3,4,5,6")
    print("test_more_than_five_sizes passed!")

def test_valid_input_with_max_name_length():
    assert validate_drink_input("CappuccinoDrink,8,16")
    print("test_valid_input_with_max_name_length passed!")

def test_valid_input_with_min_name_length():
    assert validate_drink_input("Te,8,16")
    print("test_valid_input_with_min_name_length passed!")

def test_valid_input_with_single_size():
    assert validate_drink_input("Espresso,24")
    print("test_valid_input_with_single_size passed!")

def test_valid_input_with_max_size():
    assert validate_drink_input("Americano,48")
    print("test_valid_input_with_max_size passed!")

def test_valid_input_with_min_size():
    assert validate_drink_input("Cortado,1")
    print("test_valid_input_with_min_size passed!")

def test_invalid_input_with_sizes_in_descending_order():
    assert not validate_drink_input("Mocha,48,47,46")
    print("test_invalid_input_with_sizes_in_descending_order passed!")

def test_invalid_input_with_special_characters_in_name():
    assert not validate_drink_input("L@tte,4,8,12")
    print("test_invalid_input_with_special_characters_in_name passed!")

def test_invalid_input_with_numbers_in_name():
    assert not validate_drink_input("3spresso,4,8,12")
    print("test_invalid_input_with_numbers_in_name passed!")

def test_invalid_input_with_empty_size():
    assert not validate_drink_input("Latte,")
    print("test_invalid_input_with_empty_size passed!")

def test_invalid_input_with_only_name():
    assert not validate_drink_input("Latte")
    print("test_invalid_input_with_only_name passed!")

def test_invalid_input_with_excessive_spacing():
    assert validate_drink_input("  Latte  ,  2  ,  4  ,  6  ")
    print("test_invalid_input_with_excessive_spacing passed!")

def test_invalid_input_with_tab_characters():
    assert validate_drink_input("Latte\t,8\t,16\t")
    print("test_invalid_input_with_tab_characters passed!")

def test_invalid_input_with_non_numeric_sizes():
    assert not validate_drink_input("Latte,small,medium")
    print("test_invalid_input_with_non_numeric_sizes passed!")

def test_invalid_input_with_boundary_size_value_above():
    assert not validate_drink_input("Latte,48,49")
    print("test_invalid_input_with_boundary_size_value_above passed!")

def test_invalid_input_with_boundary_size_value_below():
    assert not validate_drink_input("Latte,0,1")
    print("test_invalid_input_with_boundary_size_value_below passed!")

def test_valid_input_with_upper_and_lower_case_name():
    assert validate_drink_input("LaTtE,3,6,9")
    print("test_valid_input_with_upper_and_lower_case_name passed!")





if __name__ == "__main__":
    import pytest
    pytest.main()
