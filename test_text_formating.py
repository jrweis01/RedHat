import pytest
from index import OutPut


def test_format_text():
    data = [{'line_number': 2, 'file_name': 'py test', 'length_text_found': 17, 'pos': 19,
             'line_text': 'my emial adress is jrweiss@gmail.com, it used to be josh@weisscoaching.com ',
             'matched_text': 'jrweiss@gmail.com'},
            {'line_number': 2, 'file_name': 'py test', 'length_text_found': 22, 'pos': 52,
             'line_text': 'my emial adress is jrweiss@gmail.com, it used to be josh@weisscoaching.com ',
             'matched_text': 'josh@weisscoaching.com'},
            {'line_number': 5, 'file_name': 'py test', 'length_text_found': 27, 'pos': 16,
             'line_text': 'work address is joshua.weiss@silverbolt.com', 'matched_text': 'joshua.weiss@silverbolt.com'}]
    output = OutPut(1, 1, 1, data)
    formatted_ok = output.format_results()

    assert formatted_ok


def test_underscore_format_text():
    data = [{'line_number': 2, 'file_name': 'py test', 'length_text_found': 17, 'pos': 19,
             'line_text': 'my emial adress is jrweiss@gmail.com, it used to be josh@weisscoaching.com ',
             'matched_text': 'jrweiss@gmail.com'},
            {'line_number': 2, 'file_name': 'py test', 'length_text_found': 22, 'pos': 52,
             'line_text': 'my emial adress is jrweiss@gmail.com, it used to be josh@weisscoaching.com ',
             'matched_text': 'josh@weisscoaching.com'},
            {'line_number': 5, 'file_name': 'py test', 'length_text_found': 27, 'pos': 16,
             'line_text': 'work address is joshua.weiss@silverbolt.com', 'matched_text': 'joshua.weiss@silverbolt.com'}]
    output = OutPut(1, 0, 0, data)
    formatted_ok = output.format_results()

    assert formatted_ok


def test_color_format_text():
    data = [{'line_number': 2, 'file_name': 'py test', 'length_text_found': 17, 'pos': 19,
             'line_text': 'my emial adress is jrweiss@gmail.com, it used to be josh@weisscoaching.com ',
             'matched_text': 'jrweiss@gmail.com'},
            {'line_number': 2, 'file_name': 'py test', 'length_text_found': 22, 'pos': 52,
             'line_text': 'my emial adress is jrweiss@gmail.com, it used to be josh@weisscoaching.com ',
             'matched_text': 'josh@weisscoaching.com'},
            {'line_number': 5, 'file_name': 'py test', 'length_text_found': 27, 'pos': 16,
             'line_text': 'work address is joshua.weiss@silverbolt.com', 'matched_text': 'joshua.weiss@silverbolt.com'}]
    output = OutPut(0, 1, 0, data)
    formatted_ok = output.format_results()

    assert formatted_ok


def main():
    test_color_format_text()


if __name__ == "__main__":
    main()