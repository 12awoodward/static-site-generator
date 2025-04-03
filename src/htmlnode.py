class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html = ""
        for key, value in self.props.items():
            html += f' {key}="{value}"'
        return html
    
    def __repr__(self):
        return f"HMTLNode(tag={self.tag}|props={self.props}|value={self.value}|children={self.children})"