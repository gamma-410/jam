# Create.main.py
# jam.main.py

import os
import glob
import markdown

title = "jam - PythonSSG"
fileName = glob.glob('content/*.md')

for name in fileName:

    mdOpen = open(name, 'r')
    mdData = mdOpen.read()

    md = markdown.Markdown()  # Create an instance?

    formatMdData = md.convert(mdData)  # To convert md to html, use md.convert.

    html = open('assets/base.html')  # Define the HTML template.
    htmlData = html.read()
    formatData = htmlData.format(title, formatMdData)  # Put the title and formatted md into the template.


for htmlName in fileName:
    name = os.path.splitext(os.path.basename(htmlName))[0]

    print("jam 🍓: ", name+".md", " >>> ", "Creating", name+".html")

    htmlFileName = name+'.html'
    writeHTMLFile = open("generate/"+htmlFileName, 'w')
    writeHTMLFile.write(formatData)
    writeHTMLFile.close()

