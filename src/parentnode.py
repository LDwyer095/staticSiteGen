from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):

        if self.tag == None:
            raise ValueError("to_html Tag in parent not given")
        
        if self.children == None:
            raise ValueError("to_html Children in parent not given")
        
        nodeString = ""

        for child in self.children:
            nodeString += child.to_html()
           
        return f"<{self.tag}{self.props_to_html()}>{nodeString}</{self.tag}>"
    

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
