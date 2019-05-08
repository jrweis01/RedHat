import pytest
from index import GetDataFromFile


def test_find_single_match_in_line():
    txt = ["The rain in Spain"]
    re_expression = "^The.*Spain$"

    stdin_obj = GetDataFromFile(re_expression)
    found_match, found_lines = stdin_obj.search_data_content(txt, 'py test')
    assert found_match


def test_find_two_matches_in_line():
    txt = ["The rain in Spain"]
    re_expression = "ai"

    stdin_obj = GetDataFromFile(re_expression)
    found_match, found_lines = stdin_obj.search_data_content(txt, 'py test')
    assert len(found_lines) == 2


def test_find_matches_with_regex_space_in_line():
    txt = ["hello world. Its a beautiful world, isn't it! hello world: Would you like me to say hello-world to you anymore?\n"]
    re_expression = "h[a-zA-Z]{4} world"

    stdin_obj = GetDataFromFile(re_expression)
    found_match, found_lines = stdin_obj.search_data_content(txt, 'py test')
    print len(found_lines)
    assert len(found_lines) == 2


def test_find_email_in_line():
    txt = ["work address is joshua.weiss@silverbolt.com"]
    re_expression = "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    stdin_obj = GetDataFromFile(re_expression)
    found_match, found_lines = stdin_obj.search_data_content(txt, 'py test')
    assert found_match


def test_find_two_emails_in_line():
    txt = ["my emial adress is jrweiss@gmail.com, it used to be josh@weisscoaching.com "]
    re_expression = "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    stdin_obj = GetDataFromFile(re_expression)
    found_match, found_lines = stdin_obj.search_data_content(txt, 'py test')
    assert len(found_lines) == 2


def test_count_timestamps_in_log():
    import os
    this_file = os.getcwd() + "\\VBox.log"
    if os.path.isfile(this_file):
        f = open(this_file, 'r')
        txt = f.readlines()
        f.close()
        re_expression = "\d{2}:\d{2}:\d{2}.\d{5}"

        stdin_obj = GetDataFromFile(re_expression)
        found_match, found_lines = stdin_obj.search_data_content(txt, 'py test')
        # print(len(found_lines))
        assert len(found_lines) == 1947
    else:
        print("File does not exist: " + this_file)
        assert False


def test_find_three_emails_in_paragraph():
    domains = ["gmail", "weisscoaching", "silverbolt"]
    txt = ["this is the first line of junk",
           "my name is Joshua Weiss",
           "my emial adress is jrweiss@gmail.com, it used to be josh@weisscoaching.com ",
           "my number is 0543331950", "",
           "work address is joshua.weiss@silverbolt.com"]
    re_expression = "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    stdin_obj = GetDataFromFile(re_expression)
    found_match, found_lines = stdin_obj.search_data_content(txt, 'py test')
    print(found_lines)
    for domain in domains:
        found_domain = False
        for line in found_lines:
            if line["matched_text"].find(domain) > -1:
                found_domain = True
        if not found_domain:
            assert False
    assert True


def main():
    test_find_matches_with_regex_space_in_line()


if __name__ == "__main__":
    main()


