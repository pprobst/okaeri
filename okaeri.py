#!/usr/bin/env python3
from mako.template import Template

class Link():
    def __init__(self, section, name, url):
        self.section, self.name, self.url = section, name, url

def parse_file(filename="links.oka"):
    sections = {}

    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("#"):
                sect_name = line[2:-1]
                sections[sect_name] = []
            elif line != "\n":
                sections[sect_name].append(line[:-1])

        return sections

def create_Links(sections):
    links = []

    for key, val in sections.items():
        for s in val:
            s = s.split(' ')
            links.append(Link(key, s[0], s[1]))

    return links


sections = parse_file()
zerudas = create_Links(sections)

tmpl = Template(filename='template.html', input_encoding='utf-8', output_encoding='utf-8')

with open("./html/homepage.html", 'wb') as f_out:
    f_out.write(bytes(tmpl.render(zerudas=zerudas, sections=sections)))
