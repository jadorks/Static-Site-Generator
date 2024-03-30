class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented

    def props_to_html(self):
        attr_string = ""
        if self.props:
            for key, value in self.props.items():
                attr_string += f" {key}={value}"
        return attr_string

    def __repr__(self) -> str:
        return "HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
