from collections import OrderedDict
import domain.tutoringModel.generate_learning_path as LP
import pytest

generate_learning_path = LP.GenerateLearningPath()


def test_get_learning_path_correct_result():
    input_learning_style = {"AKT": 5, "INT": 9, "VIS": 9, "GLO": 9}
    # ZF-ÜB-#AN-#SE-RQ-AB-#ZL-#BE-FO
    learning_path = {
        'ZF': 99, 'ÜB': 14, 'SE': 5, 'AN': 5,
        'RQ': 4, 'AB': 0, 'ZL': -5, 'BE': -5, 'FO': -13}
    assert generate_learning_path.get_learning_path(
        input_learning_style) == learning_path


def test_get_learning_path_correct_result_2():
    input_learning_style = {"REF": 1, "SNS": 7, "VIS": 5, "SEG": 5}
    # result of Learning Path : AN-BE-AB-#SE-#ÜB-RQ-ZF-FO-ZL
    learning_path = {
        'AN': 11,  'BE': 8, 'AB': 7, 'SE': 6, 'ÜB': 6,
        'RQ': 1, 'ZF': 0, 'FO': -6, 'ZL': -11}

    assert generate_learning_path.get_learning_path(
        input_learning_style) == learning_path


def test_get_learning_path_correct_result_3():
    # 3- Test
    input_learning_style = {"AKT": 3, "SNS": 7, "VIS": 3, "GLO": 3}

    # result of Learning Path : ZF-AN-#SE-#ÜB-#AB-BE-FO-RQ-ZL
    learning_path = {'ZF': 99, 'AN': 13, 'SE': 10, 'ÜB': 10,
                     'AB': 10, 'BE': 7, 'FO': 0, 'RQ': -3, 'ZL': -13}
    assert generate_learning_path.get_learning_path(
        input_learning_style) == learning_path


def test_get_learning_path_correct_result_4():
    # 4- Test
    input_learning_style = {"AKT": 5, "SNS": 7, "VIS": 7, "GLO": 3}

    # result of Learning Path : ZF-AN-#SE-#ÜB-#AB-BE-FO-RQ-ZL
    learning_path = {'ZF': 99, 'AN': 19, 'SE': 12, 'ÜB': 12,
                     'AB': 10, 'BE': 5, 'FO': -2, 'RQ': -5, 'ZL': -19}
    assert generate_learning_path.get_learning_path(
        input_learning_style) == learning_path


def test_get_learning_path_with_empty_learning_style():
    learning_path = {'ZF': 0, 'AN': 0, 'SE': 0, 'ÜB': 0,
                     'AB': 0, 'BE': 0, 'FO': 0, 'RQ': 0, 'ZL': 0}
    assert generate_learning_path.get_learning_path() == learning_path


def test_get_learning_path_with_different_size_of_input_learning_style():
    input_learning_style = {"INT": 9, "VIS": 9, "GLO": 9}
    with pytest.raises(ValueError):
        generate_learning_path.get_learning_path(input_learning_style)


def test_get_learning_path_with_out_of_Range_input_learning_style_dimension():
    input_learning_style = {"AKT": 12, "INT": 2, "VIS": 11, "GLO": 9}
    with pytest.raises(ValueError):
        generate_learning_path.get_learning_path(input_learning_style)