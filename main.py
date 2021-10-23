# Create.main.py
# pySSG.main.py

import sys
import markdown

args = sys.argv
fileName = args[1]

mdOpen = open(fileName+'.md', 'r')
mdData = mdOpen.read()

md = markdown.Markdown()  # Create an instance?

formatMdData = md.convert(mdData)  # To convert md to html, use md.convert.

htmlData = '''
<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex,nofollow">
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
{}
</body>
<html>
'''  # Define the HTML template.

formatData = htmlData.format("Hello, pySSG.", formatMdData)  # Put the title and formatted md into the template.

print("generate: " + args[1]+'.md' + " >>> " + args[1]+'.html')
htmlFileName = args[1]+'.html'
writeHTMLFile = open(htmlFileName, 'w')
writeHTMLFile.write(formatData)
