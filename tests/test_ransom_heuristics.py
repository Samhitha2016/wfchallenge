#!/usr/bin/env python

"""test_ransom_heuristics.py: A testfile that tests ransom_heuristics for different positive and negative inputs"""

__author__ = "Samhitha Sathyanarayana"
__Date__ = "20th Oct 2018"



'''This module checks for false positives and false negative matches for all the methods listed in ransom_heuristics.py. In order to test the methods,
do 
1) pip install requirement.txt that ensures that a specifi version of pytest gets installed and once that is done, to test your algorithm
2) run pytest

All the data or test input files are locates in /test/data. The original test files "PLEASE_READ_ME.txt and afF0293aaaff222200BC8a9Cfeff0001.txt are also in data directory.'''





import ransom_heuristics
import os



TEST_DATA_DIR = "tests/data"


def test_blacklisted_patterns_matches():
    """A test case that tests for matches for the method blacklisted_patterns_matches() in ransom_heuristics.py

        Args:
            test_cases: a list containing various patterns where atleast one of them could be a potential match


        Returns:
            A pass "Ran the test successfully" and a time if the test runs successfully else it throws an Assertion Error.

        Raises:
            An assertion error.
    """
    test_cases = [
        'YOUR_FILES_ARE_LOCKED.txt',
        'read_this_file.txt',
        'FILES_BACK.txt',
        'README_.TXT',
        'How to decrypt your files.txt',
        'ransomed.html',
        'README HOW TO DECRYPT YOUR FILES.HTML'
    ]
    for test_case in test_cases:
        assert ransom_heuristics.filename_has_blacklisted_patterns(test_case)


def test_blacklisted_patterns_no_matches():
    """A test case that tests for  no matches for the method blacklisted_patterns_matches() in ransom_heuristics.py

        Args:
            test_cases: a list containing various patterns where none of them are a potential match


        Returns:
            A pass "Ran the test successfully" if there was no match and a time if the test runs successfully else it throws an Assertion Error.

        Raises:
            An assertion error if 'good_file.txt' matched the patterns.
    """
    test_cases = ['good_file.txt']
    for test_case in test_cases:
        assert not ransom_heuristics.filename_has_blacklisted_patterns(test_case)


def test_ransom_bitcoins_matches():
    """A test case that tests for matches for the ransom_bitcoins_matches() in ransom_heuristics.py

        Args:
            test_files: a list of files containing various bitcoin address patterns where atleast one of file contents could have a bitcoin address.

        Returns:
            A pass "Ran the test successfully" and a time if the test runs successfully else it throws an Assertion Error.

        Raises:
            An assertion error if any of the inputs doesnt match bitcoin address in neither 'bitcoins_positive_1.txt' nor 'bitcoins_positive_2.txt'
    """
    test_files = ['bitcoins_positive_1.txt', 'bitcoins_positive_2.txt']
    for test_file in test_files:
        assert ransom_heuristics.file_content_has_bitcoin_address(open(os.path.join(TEST_DATA_DIR, test_file)).read())


def test_ransom_bitcoins_no_matches():
    """A test case that tests for no matches for the ransom_bitcoins_matches() in ransom_heuristics.py

        Args:
            test_cases: a list of files containing various bitcoin address patterns where  none of file contents have a bitcoin address.

        Returns:
            A pass "Ran the test successfully" and a time if the test runs successfully else it throws an Assertion Error.

        Raises:
            An assertion error if any of the inputs match the address in 'bitcoins_negative_1.txt'.
    """
    test_cases = ['bitcoins_negative_1.txt']
    for test_case in test_cases:
        assert not ransom_heuristics.file_content_has_bitcoin_address(
            open(os.path.join(TEST_DATA_DIR, test_case)).read())


def test_ransom_keywords_matches():
    """A test case that tests for matches for the ransom_keywords_matches() in ransom_heuristics.py

        Args:
            test_cases: a list of files containing various keywords where atleast few of them match the keywords from "keywords.txt" exactly.

        Returns:
            A pass "Ran the test successfully" and a time if the test runs successfully else it throws an Assertion Error.

        Raises:
            An assertion error if there is no match for 50% of the keywords in 'keywords_positive.txt'.
    """
    test_cases = ['keywords_positive.txt']
    for test_case in test_cases:
        assert ransom_heuristics.file_content_has_ransom_keywords(open(os.path.join(TEST_DATA_DIR, test_case)).read())


def test_ransom_keywords_no_matches():
    """A test case that ensures that tests doesnt matches for the ransom_keywords_matches() in ransom_heuristics.py

        Args:
            test_cases: a list of files containing various keywords where none of them match the keywords from "keywords.txt" exactly.

        Returns:
            A pass "Ran the test successfully" and a time if the test runs successfully else it throws an Assertion Error.

        Raises:
            An assertion error if there is 50% match for the keywords in 'keywords_negative.txt'.
    """
    test_cases = ['keywords_negative.txt']
    for test_case in test_cases:
        assert not ransom_heuristics.file_content_has_ransom_keywords(
            open(os.path.join(TEST_DATA_DIR, test_case)).read())