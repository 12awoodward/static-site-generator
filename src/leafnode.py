from htmlnode import *
from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self, tag: str | None, value: str, props: dict[str, str] | None = None
    ):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if not self.value:
            if self.tag == "img":
                return f"<{self.tag}{self.props_to_html()}> "

            raise ValueError("leaf nodes must have a value")

        if not self.tag:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def add_child(self, child: HTMLNode):
        raise Exception("Leaf Nodes do not have children")
