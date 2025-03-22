from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    
    def __init__(self, tag, value = None, props = None):
        super().__init__(tag, value, props)
        self.props = props

    def to_html(self):
        nodeString = ""

        if self.value == None:
            raise ValueError("to_html Value not given")
        
        if self.tag == None:
            return f"{self.value}"
        
        if self.props == None:
            nodeString = f"<{self.tag}>{self.value}</{self.tag}>"
            return nodeString

        nodeString = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return nodeString