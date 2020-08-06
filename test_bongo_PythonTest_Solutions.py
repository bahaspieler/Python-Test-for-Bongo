import unittest
from bongo_PythonTest_Solutions import Node, lca, NestedDictionaryDepth, NestedDictionaryObjectDepth, Person
from io import StringIO
from unittest.mock import patch

class Testleast_common_ancestor(unittest.TestCase):
    def setUp(self):
        root = Node(0)
        self.root = root

        root.left = Node(1)
        root.right = Node(2)
        root.left.left = Node(3)
        root.left.right = Node(4)
        root.left.right.left = Node(9)
        root.left.left.left = Node(7)
        root.left.left.right = Node(8)
        root.left.right.right = Node(10)
        root.right.left = Node(5)
        root.right.left.left = Node(11)
        root.right.right = Node(6)

        self.a = {'key1':1, 'key2': {'key3': 1,'key5':5}, 'key4': {'key5': 4}}

        self.person_a = Person('USer', '1', None)
        self.person_b = Person("User", '2', self.person_a)
        self.b = {'key1': 1, 'key2': {'key3': 1, 'key4': {'key5': 4, 'user': self.person_b}}}


    def test_lca(self):
        print('\n<<--Test for Least Common Ancestor-->>\n')
        test_result = lca(self.root, 7, 3).value
        self.assertEqual(test_result, 3)

    def test_NestedDictionaryDepth(self):
        print('\n<<--Test for NestedDictionaryDepth-->>\n')
        expected_StdOut = 'key1 1\n' \
                           'key2 1\n' \
                           'key3 2\n' \
                           'key5 2\n' \
                           'key4 1\n' \
                           'key5 2\n'
        with patch('sys.stdout', new=StringIO()) as StdOut:
            NestedDictionaryDepth(self.a)
            self.assertEqual(StdOut.getvalue(), expected_StdOut)

    def test_NestedDictionaryObjectDepth(self):
        print('\n<<--Test for NestedDictionaryObjectDepth-->>\n')
        expected_StdOut = 'key1 1\n' \
                          'key2 1\n' \
                          'key3 2\n' \
                          'key4 2\n' \
                          'key5 3\n' \
                          'user 3\n' \
                          'first_name 4\n' \
                          'last_name 4\n' \
                          'father 4\n' \
                          'first_name 5\n' \
                          'last_name 5\n' \
                          'father 5\n'
        with patch('sys.stdout', new=StringIO()) as StdOut:
            NestedDictionaryObjectDepth(self.b)
            self.assertEqual(StdOut.getvalue(), expected_StdOut)

if __name__ == "__main__":
    unittest.main()