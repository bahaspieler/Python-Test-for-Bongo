'''
Finding Depth of keys of Nested Dictionaries.
'''

# depth_default = 0

def NestedDictionaryDepth(dictionary, depth_default = 0):
    depth_default = depth_default + 1
    if len(dictionary) > 0:
        for keys, values in dictionary.items():
            print(keys, depth_default)
            if isinstance(values, dict):
                NestedDictionaryDepth(values, depth_default)


a = {'key1':1, 'key2': {'key3': 1,'key5':5}, 'key4': {'key5': 4}}


print("\n\n1. Key Depth Output for:--\n{'key1':1, 'key2': {'key3': 1,'key5':5}, 'key4': {'key5': 4}} \n")
NestedDictionaryDepth(a)



'''
Finding Depth of keys of Nested Dictionaries with having a python object.
'''
# depth_default = 0
class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


def NestedDictionaryObjectDepth(dictionary, depth_default = 0):
    depth_default = depth_default + 1
    if isinstance(dictionary, Person):
        dictionary_obj = vars(dictionary)
        for tag, val in dictionary_obj.items():
            print(tag, depth_default)
            NestedDictionaryObjectDepth(val, depth_default)
    if isinstance(dictionary, dict):
        if len(dictionary) > 0:
            for key, values in dictionary.items():
                print(key, depth_default)
                NestedDictionaryObjectDepth(values, depth_default)

person_a = Person('USer', '1', None)
person_b = Person("User", '2', person_a)

b = {'key1':1, 'key2': {'key3': 1, 'key4': {'key5': 4, 'user': person_b}}}
print("\n\n2. Key Depth Output for:--\n{'key1':1, 'key2': {'key3': 1, 'key4': {'key5': 4, 'user': person_b}}} \n")
NestedDictionaryObjectDepth(b)



'''
Least Common Ancestor:-

Recursion method (Recursive Tree Traversal) is used to reduce the required time and space.

Time - complexity:-
    O(m+n) ~ O(n) where, m = number of boundaries
                         n = number of nodes
    as this method needs one traversal to determine the
    least common ancestor from the binary tree.

Space - complexity:-
    O(n)
    as the Recursive Tree Traversal doesn't use any kind of
    datastructure to store the position of the ancestores
    of the nodes.
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None



def lca(root, node1, node2):
    if root is None:
        return None

    if node1 == root.value or node2 == root.value:
        return root

    left_lca = lca(root.left, node1, node2)

    right_lca = lca(root.right, node1, node2)

    if left_lca != None and right_lca != None:
        return root

    if left_lca is not None:
        return left_lca
    else:
        return right_lca


#Creating the Tree

root = Node(0)
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


node1 = 7
node2 = 3
least_common_ancestor = lca(root, node1, node2).value

print('\n\n3. Least common ancestor of {0} and {1} is :-  {2}'.format(node1, node2, least_common_ancestor))
