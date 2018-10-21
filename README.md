# ransom
Detection algorithm:
 
A: File name matches ANY of the known templates in Patterns.txt
B: Content of the file has a potential Bitcoin address
C: Content of the file has more than 50% of known ransomware keywords from Keywords.txt
 
If the input file matches A, B and C, print ‘YES’ to the screen.
If the input file matches B and C, print ‘LIKELY’ to the screen.
If the input file matches A and C, print ‘LIKELY’ to the screen.
For all other combinations, print ‘NO’ to the screen.


Patterns.txt – A TXT file with known ransom notes templates
Exact strings (e.g. FILES_BACK.txt)
Regular expressions (start with ^ or end with $)
Keywords.txt – A TXT file with known ransomware keywords
 
Test files:
afF0293aaaff222200BC8a9Cfeff0001.txt

PLEASE_READ_ME.txt

main.py: Takes the cli input and returns the result

ransom_file_classifier.py: Collects the results from A,B,C and computes the decision ("YES", "NO", "LIKELY")

ransom_heuristics.py: Implements the Detection algorithm for A, B and C.

Other miscellaneous files:

tests-contanins the test script: test_ransom_heuristics.py that runs pytest to test ransom_heuristics.py with positive and negative inputs

data-a test directory containing test input files.

The __init__.py files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name, such as string , from unintentionally hiding valid modules that occur later (deeper) on the module search path.


To run the tests

```shell
$ pip install requirements.txt
$ pytest
```


