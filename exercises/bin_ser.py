# Write two functions, one that serializes a binary tree, given its root node and
# one that deserializes the result of the first function from a string to a binary tree.



#     1
#    / \
#   2   3
#  /   / \
# 8   4   5


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"[{self.value}, {self.left!r}, {self.right!r}]"

"{13,{left},{right}}"

def serialize(node):

    if node is None:
        return "{}"

    parts = [str(node.value)]

    parts.append(serialize(node.left))
    parts.append(serialize(node.right))

    return "{" + ",".join(parts) + "}"


def strip_value(string):
    first_comma = string.find(",")
    value = int(string[1:first_comma])
    return value, string[first_comma+1:-1]

def deserialize(string):
    if string == "{}":
        return None

    value, children = strip_value(string)
    left_string = None
    right_string = None
    level = 0
    for i, c in enumerate(children):
        if c == "{":
            level += 1
        elif c == "}":
            level -= 1

        if level == 0:
            left_string = children[:i+1]
            right_string = children[i+2:]
            break

    node = Node(value)
    node.left = deserialize(left_string)
    node.right = deserialize(right_string)

    return node


root = Node(10)
root.left = Node(9)
root.right = Node(22)
root.right.right = Node(44)

data = serialize(root)
print(root, "=>", data) # {10,{9,{},{}},{}}

node = deserialize(data)
print(node)