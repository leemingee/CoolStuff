'''
Created by Ming Li at 2019-01-23

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''
from unittest import TestCase

class TestNode(TestCase):
    def test_add_child(self):
        self.fail()


def main():
    n = Node(1, 1, 1)
    ans = n.__str__()
    print(ans)


if __name__ == '__main__':
    main()