#!/usr/bin/env python3

import markdown

# Simple conversion in memory
md_text = '# Hello\n\n**Text**'
html = markdown.markdown(md_text)
print(html)
