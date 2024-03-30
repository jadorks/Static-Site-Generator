class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        attr_string = ""
        if self.props:
            for key, value in self.props.items():
                attr_string += f' {key}="{value}"'
        return attr_string

    def __repr__(self) -> str:
        return "HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError()

        if self.tag:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return self.value
