import sys
import re
import os

file_name = sys.argv[1]

with open(file_name) as file:
    lines = file.readlines()

lines_count = len(lines)
for i in range(lines_count):
    no_closing_bracket_group = '([^\]]+)'
    def search_named_link():
        return re.search(f'\[{no_closing_bracket_group}\|{no_closing_bracket_group}\]', lines[i])

    match = search_named_link()
    while match is not None:
        # print(match.group(1), '    ', match.group(2))
        lines[i] = lines[i][:match.start()] + f'[{match.group(2)}]({match.group(1)})' + lines[i][match.end():]

        match = search_named_link()

    no_closing_bracket = '[^\]]+'
    def search_basic_link():
        return re.search(f'(\[)https?://{no_closing_bracket}(\])', lines[i])

    match = search_basic_link()
    while match is not None:
        if '|' not in match.group(0):
            lines[i] = lines[i][:match.start(1)] + lines[i][match.end(1):match.start(2)] + lines[i][match.end(2):]
        match = search_basic_link()

    if (match := re.match('^!+', lines[i])) is not None:
        lines[i] = "#" * (match.end() - match.start()) + " " + lines[i][match.end():]
    elif (match := re.match('^\++', lines[i])) is not None:
        lines[i] = "  " * (match.end() - match.start() - 1) + (" " if lines[i][match.end()] != " " else "") + " " + lines[i][match.end():]
    elif (match := re.match('^\*+', lines[i])) is not None:
        lines[i] = "  " * (match.end() - match.start() - 1) + "-" + (" " if lines[i][match.end()] != " " else "") + lines[i][match.end():]
    elif (match := re.match('^\#+', lines[i])) is not None: # numbered list 
        lines[i] = "  " * (match.end() - match.start() - 1) + "1." + (" " if lines[i][match.end()] != " " else "") + lines[i][match.end():]


for i in range(lines_count):
    lines[i] = lines[i].replace('[[', '[').replace("__", "**").replace("{CODE}", "\n```").replace("{CODE()}", "```\n")
    # TODO: If a code block starts with indentation, the indentation should be added for every line of the code block in Markdown.
    # TODO: Make sure closing code blocks always happens on a newline
        
if os.path.splitext(file_name)[1].lower()[1:] == "tiki":
    new_file_name = file_name.replace('.tiki', '.md')
else:
    new_file_name = file_name + '.md'

with open(new_file_name, 'w') as file:
    file.writelines(lines)
