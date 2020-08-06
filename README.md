# Problem Solutions for Bongo Python Code Test
This repository contains two scripts of Bongo Python Code Test including a Unit Test to test the functions.

##### bongo_PythonTest_Solutions.py
To run the script execute `python bongo_PythonTest_Solutions.py` or `python3 bongo_PythonTest_Solutions.py` in your cmd/terminal.

##### test_bongo_PythonTest_Solutions.py
To run the unittest execute `python test_bongo_PythonTest_Solutions.py` or `python3 test_bongo_PythonTest_Solutions.py` in your cmd/terminal.

###### Least Common Ancestor \[Explanation\]
Recursion method (Recursive Tree Traversal) is used to reduce the required time and space.

Time-complexity:- 

    O(m+n) ~ O(n) where, m = number of boundaries
                         n = number of nodes
    as this method needs one traversal to determine the
    least common ancestor from the binary tree.

Space-complexity:-

    O(n)
    as the Recursive Tree Traversal doesn't use any kind of
    datastructure to store the position of the ancestores
    of the nodes.
