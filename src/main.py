import os
import pathlib
import shutil
from block_markdown import markdown_to_html_node


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_path_entries = os.listdir(dir_path_content)

    for entry in dir_path_entries:
        path = os.path.join(dir_path_content, entry)

        if os.path.isfile(path):
            if pathlib.Path(path).suffix == ".md":
                dst = os.path.join(dest_dir_path, f"{pathlib.Path(path).stem}.html")
                generate_page(path, template_path, dst)
        else:
            dst = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(path, template_path, dst)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = ""
    template = ""

    with open(from_path, "r") as markdown_file, open(
        template_path, "r"
    ) as template_file:
        markdown = markdown_file.read()
        template = template_file.read()

    content = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)

    page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    dest_dirname = os.path.dirname(dest_path)

    if not os.path.exists(dest_dirname):
        os.makedirs(dest_dirname)

    with open(dest_path, "w") as f:
        print(page, file=f)


def extract_title(markdown):
    blocks = markdown.split("\n")
    for block in blocks:
        if block.startswith("# "):
            return block.lstrip("# ").strip()
    raise ValueError("No header title")


def copy_source_to_destination(source, destination):
    if not os.path.exists(source):
        raise ValueError("Source directory does not exist")

    if not os.path.exists(destination):
        os.mkdir(destination)
    else:
        shutil.rmtree(destination)
        os.mkdir(destination)

    static_files = os.listdir(source)

    for entry in static_files:
        path = os.path.join(source, entry)

        if os.path.isfile(path):
            shutil.copy(path, destination)
        else:
            dst = os.path.join(destination, entry)
            copy_source_to_destination(path, dst)


def main():
    copy_source_to_destination("static", "public")
    generate_pages_recursive("content", "template.html", "public")


main()
