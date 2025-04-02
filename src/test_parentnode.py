import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html_just_tag_and_children_one_layer(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), 
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        
    def test_to_html_just_tag_and_children_two_layer(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_just_tag_and_children_three_layer(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_just_tag_and_children_two_children(self):
        child1_node1= LeafNode("span", "child1")
        child2_node1 = LeafNode("span", "child2")
        node1 = ParentNode("n1",[child1_node1,child2_node1])

        child1_node2= LeafNode("span", "child1")
        child2_node2 = LeafNode("span", "child2")
        node2 = ParentNode("n2",[child1_node2,child2_node2])

        parent_node = ParentNode("p",[node1,node2])

        self.assertEqual(parent_node.to_html(), 
            "<p><n1><span>child1</span><span>child2</span></n1><n2><span>child1</span><span>child2</span></n2></p>")


if __name__ == "__main__":
    unittest.main()