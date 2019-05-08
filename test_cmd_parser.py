import pytest
import index


def test_invalid_regular_expression():
    cmd_line_parameters = ["test CMD Parser", "[", "-"]
    is_re_valid, regex, input_sources, underscore, color, machine = index.parse_cmd_line(cmd_line_parameters)

    assert not is_re_valid


def test_valid_email_regular_expression():
    cmd_line_parameters = ["test CMD Parser", "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", "-"]
    is_re_valid, regex, input_sources, underscore, color, machine = index.parse_cmd_line(cmd_line_parameters)

    assert is_re_valid


def test_color():
    cmd_line_parameters = ["test CMD Parser", "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", '-c', "-"]
    is_re_valid, regex, input_sources, underscore, color, machine = index.parse_cmd_line(cmd_line_parameters)

    assert color


def test_underscore():
    cmd_line_parameters = ["test CMD Parser", "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", '-u', "-"]
    is_re_valid, regex, input_sources, underscore, color, machine = index.parse_cmd_line(cmd_line_parameters)

    assert underscore


def test_underscore_uppercase():
    cmd_line_parameters = ["test CMD Parser", "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", '-U', "-"]
    is_re_valid, regex, input_sources, underscore, color, machine = index.parse_cmd_line(cmd_line_parameters)

    assert underscore


def test_machine():
    cmd_line_parameters = ["test CMD Parser", "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", '-m', "-"]
    is_re_valid, regex, input_sources, underscore, color, machine = index.parse_cmd_line(cmd_line_parameters)

    assert machine


def test_machine_and_underscore():
    cmd_line_parameters = ["test CMD Parser", "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", '-m', '-u', "-"]
    is_re_valid, regex, input_sources, underscore, color, machine = index.parse_cmd_line(cmd_line_parameters)

    assert machine and underscore


def test_empty_input_source():
    cmd_line_parameters = ["test CMD Parser", "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", '-m', '-u']
    is_re_valid, regex, input_sources, underscore, color, machine = index.parse_cmd_line(cmd_line_parameters)

    assert input_sources[0] == '-' and len(input_sources) == 1


def test_multiple_input_sources():
    cmd_line_parameters = ["test CMD Parser", "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", '-m',
                           '-u',"C:\\Users\\joshua\\Documents\\red_hat\\VBox.log", '-',
                           "C:\\Users\\joshua\\Documents\\red_hat\\doesntexist.log"]
    is_re_valid, regex, input_sources, underscore, color, machine = index.parse_cmd_line(cmd_line_parameters)

    assert input_sources[1] == '-' and len(input_sources) == 3


def main():
    test_invalid_regular_expression()


if __name__ == "__main__":
    main()