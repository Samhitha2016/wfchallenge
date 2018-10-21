#!/usr/bin/env python

"""ransom_heuristics.py: Gives heuristics or hits for the conditions matched on A, B and C"""

__author__= "Samhitha Sathyanarayana"
__Date__="20th Oct 2018"



import ransom_heuristics
import os


def classify_file(file_path):
    """Reads the file contents and also extracts the filename if an absolute file path is supplied as an input. Gives a verdict that is a string-("YES", "NO" or "LIKELY") based on certains matches. The matches are under 3 categories.

        Args:
            is_ransom_filename_detected: This is a True or False value if the filename matches any blacklisted patterns contained in "Patterns.txt".
            is_bitcoin_address_detected: This is a True or False value if the file contents has any bitcoin address.
            is_ransom_keywords_detected: This is a true or False value if the file contents has more then 50% of keywords in "keywords.txt" file.


        Returns:
            a string that is either ("YES", "NO" or "LIKELY")

        Raises:
            No exception
        """


    file_content = open(file_path).read()
    file_name = os.path.basename(file_path)


    is_ransom_filename_detected = ransom_heuristics.filename_has_blacklisted_patterns(file_name)
    is_bitcoin_address_detected = ransom_heuristics.file_content_has_bitcoin_address(file_content)
    is_ransom_keywords_detected = ransom_heuristics.file_content_has_ransom_keywords(file_content)



    result = "NO"
    if is_ransom_keywords_detected:
        if is_ransom_filename_detected and is_bitcoin_address_detected:
            result = "YES"
        elif is_bitcoin_address_detected or is_ransom_filename_detected:
            result = "LIKELY"

    return result
