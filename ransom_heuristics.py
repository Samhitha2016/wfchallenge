#!/usr/bin/env python

"""ransom_heuristics.py: Implements filename pattern matching, finding bitcoin addresses and black listed keywords from input file contents"""

__author__= "Samhitha Sathyanarayana"
__Date__="20th Oct 2018"

import re
from functools import lru_cache


@lru_cache(1)
def keywords_pattern():
    """Opens the file "keywords.txt", strips all the empty lines and caches the contents of the file and returns a list of all the file contents (keywords)
        Args:
            filename-"keywords.txt" and this is always present hence doesnt throw any exception.
            lru_cache is used so as to cache the contents of this file so that running the program multiple times with multiple test inputs would not be a memory or disk space
            intensive operation that is often associated with file handling and opening
        Returns:
            set(lines): This is done so as to easily match the keywords in the list with that of the words in the file content.
            """
    with open("keywords.txt", 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    return set(lines)



@lru_cache(1)
def blacklisted_file_patterns():
    """Opens the file "patterns.txt", strips all the empty lines and caches the contents of the file and returns a set of all malicious filename patterns.
        Args:
            filename-"patterns.txt" and this is always present hence doesnt throw any exception.
            lru_cache is used so as to cache the contents of this file so that running the program multiple times with multiple test inputs would not be a memory or disk space
            intensive operation that is often associated with file handling and opening
        Returns:
            set(lines): This is done so as to easily match the patterns in the list with that of the words in the file content.
    """
    with open("patterns.txt", 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    return set(lines)


def filename_has_blacklisted_patterns(file_name):
    """Searches if the filename matches any of the blacklisted or bad patterns in "patterns.txt".
        Args:
            file_name which is the filename supplied by the user from cli or the extracted filename from the absolute path supplied by the user.
        Returns:
            True if the filename matches ANY of the patterns in patterns.txt (either exact match or regex match) and False if no match is found.
    """
    generic_re = re.compile('|'.join(blacklisted_file_patterns()))
    if generic_re.search(file_name):
        return True
    else:
        return False


def file_content_has_bitcoin_address(file_content):
    """Checks if the filename content has any bitcoin addresses. Bitcoin addresses usually begin with a 1 or 3 indicating the possible destination for a payment.
        They are 25-36 alphanumeric characters long and exclude the uppercase letter "O", uppercase letter "I", lowercase letter "l", and the number "0"
        which are never used to prevent visual ambiguity.".
        Args:
            file_content which is the file content obtained from ransom_file_classifier after reading the contents of the file supplied by the user..
        Returns:
            True if the file content contains any bitcoin addresses and False if no match is found.
    """
    bitcoin_address_regex = re.compile('[13][a-km-zA-HJ-NP-Z1-9]{25,34}')
    if bitcoin_address_regex.search(file_content):
        return True
    else:
        return False


def file_content_has_ransom_keywords(file_content):
    """Checks if the filename content has any blacklisted/ransom keywords in keywords.txt. This is implemented by doing a pattern match on
     only the words in a file by excluding all the punctutation and checking if those words match exactly with the words in keywords.txt
      Match is executed by performing an intersection of set in python.

        Args:
            file_content which is the file content obtained from ransom_file_classifier after reading the contents of the file supplied by the user..
        Returns:
            True if the file content contains any ransom/blacklisted keywords in keywords.txt and False if no match is found.
    """
    blacklisted_keywords = keywords_pattern()
    words = re.findall(re.compile('\w+'), file_content.lower())
    blacklisted_words = blacklisted_keywords.intersection(words)
    if len(blacklisted_words) > len(blacklisted_keywords) / 2:
        return True
    else:
        return False


