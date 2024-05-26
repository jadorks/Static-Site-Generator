def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    res = []

    for block in blocks:
        if len(block) > 0:
            res.append(block.strip())

    return res


