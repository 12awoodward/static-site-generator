from __future__ import annotations


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list[HTMLNode] | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self):
        html = ""
        if self.props:
            for key, value in self.props.items():
                html += f' {key}="{value}"'
        return html

    def add_child(self, child: HTMLNode):
        if self.children is None:
            self.children = []
        self.children.append(child)

    def __repr__(self):
        return f"HMTLNode(tag={self.tag}|props={self.props}|value={self.value}|children={self.children})"
