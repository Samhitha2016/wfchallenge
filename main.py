#!/usr/bin/env python

"""main.py: Takes the cli arguement from the user and displays the result"""

__author__= "Samhitha Sathyanarayana"
__Date__="20th Oct 2018"


import argparse
import os
import ransom_file_classifer

if __name__ == '__main__':

    """Takes a cli input from a user.

        Based on the filename and filecontents, it prints the decision on the screen. "Yes", "No" or "Likely".

        Args:
            file_path: A filename or an absolute file path from the user input.
            

        Returns:
           A status which is either one of "Yes", "No" or "Likely" based on the final decision from the program ransom_file_classifier.

        Raises:
            error: "the following arguments are required: file_path"- If no cli argument is supplied.
            Prints an error message if the file doesnt exist or a valid filename or filepath isn't supplied.
        """

    parser = argparse.ArgumentParser(description='Example Command Line Parser')
    parser.add_argument('file_path', action="store", default=True)
    args = parser.parse_args()


    if not os.path.isfile(args.file_path):
        print ("File doesn't exists. Please supply a valid file")
        exit()


    status = ransom_file_classifer.classify_file(args.file_path)
    print(status)
