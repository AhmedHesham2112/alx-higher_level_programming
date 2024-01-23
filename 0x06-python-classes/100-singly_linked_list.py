#!/usr/bin/python3
"""
Define a class Node.
"""


class Node():
    """
    Represent a Node
    """
    def __init__(self, data, next_node=None):
        """
        initialize a new Node

        Args:
            data (int): the data of the new node.
            next_node: can be None or must be a Node
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if (not isinstance(next_node, Node) and next_node is not None):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        get node data
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        get next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""
Define a class Singly Linked List.
"""


class SinglyLinkedList():
    """
    Represent a singly linked list
    """
    def __init__(self):
        """
        initialize a new Node
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts new nodes into singly linked list in sorted order

        Args:
        value: int data for node
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        tmp = self.__head
        if new.data < tmp.data:
            new.next_node = self.__head
            self.__head = new
            return

        while (tmp.next_node is not None) and (new.data > tmp.next_node.data):
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
        return

    def __str__(self):
        """
        String representation of singly linked list needed to print
        """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += "\n"
        return string
