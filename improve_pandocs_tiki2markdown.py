import sys
import re
import os

file_name = sys.argv[1]

with open(file_name) as file:
    lines = file.readlines()

lines_count = len(lines)

for i in range(lines_count):
    lines[i] = lines[i].replace('\[\[', '[').replace('\]', ']').replace("\\\_\\\_\s*(.*?)\s*\\\_\\\_", "**\1**").replace("{CODE}", "\n```").replace("{CODE()}", "\n```\n").replace("~tc~", "<!--").replace("~/tc~", "-->")

    # TODO: If a code block starts with indentation, the indentation should be added for every line of the code block in Markdown.
    # TODO: Make sure closing code blocks always happens on a newline

# TODO: add conversion of tables. An example:

'''

|------------------------------------------------------------------------------|
| **Initiating author** | DrOteonu                                             |
| **Conceived by**      | DrOteonu (around May, 2024)                          |
| **Start date**        |                                                      |
| **Contributers**      | Kemueira, DrOteonu (DrO), Aeduin, [TODO finish list] |

<!-- Original tiki format:
||**Initiating author**|DrOteonu
**Conceived by**|DrOteonu (around May, 2024)
**Start date**|
**Contributers**|Kemueira, DrOteonu (DrO), Aeduin, [TODO finish list]
||
-->

'''

if os.path.splitext(file_name)[1].lower()[1:] == "pandoc_tiki2md":
    new_file_name = file_name.replace('.pandoc_tiki2md', '.md')
else:
    new_file_name = file_name + '.md'

with open(new_file_name, 'w') as file:
    file.writelines(lines)
