# Tiki to Markdown
This repository contains an incomplete script for converting Tiki syntax to Markdown.

Below is a list of what currently is implemented. Please suggest improvements by creating a new issue or pull request.
- Converts named links. Tiki: `[https://example.com|display_name]`, MD: `[display_name](https://example.com)`
- Removes brackets around non-named links. Tiki: `[https://example.com]`, MD: `https://example.com`
- Convert headers. Tiki: `!!section`, MD: `## section`
- Converts bullet lists, considering indentation. Tiki:
  ```
  list:
  * item1
  ** subitem1
  **subitem2
  ++next_line_of_subitem2
  * item2
  ```
  MD:
  ```
  list:
  - item1
    - subitem1
    - subitem2
      next_line_of_subitem2
  - item2
  ```