# Create.main.py
# jam.main.py

import os
import glob
import datetime
import markdown

title = "MyBlog"
fileName = glob.glob('content/*.md')
dt_now = datetime.datetime.now()
date = dt_now.strftime('%Y・%m・%d')

# i = 回数, name = 拡張子ついた名前, htmlName = 拡張子ついた名前
for (i, name, htmlName) in zip(range(len(fileName)), fileName, fileName): #

# ブログ機能を追加しました！ 使用する場合はコメントを外してください！

# # mdデータを準備
#     indexMdOpen = open('assets/index.md', encoding='utf-8')
#     s = indexMdOpen.read()

#     name1 = os.path.splitext(os.path.basename(htmlName))[0]
#     s = '- [' + name1 + ' - ' + date + ']' + '(' + name1 + '.html)  \n' + s

#     indexMdOpen = open('assets/index.md', 'w', encoding='utf-8')
#     indexMdOpen.write(s)

#     indexMdOpen.close()


# 表示処理
    mdOpen = open(name, 'r', encoding="utf-8")
    mdData = mdOpen.read()
    md = markdown.Markdown()  # Create an instance?

    formatMdData = md.convert(mdData)  # To convert md to html, use md.convert.

    html = open('assets/base.html', 'r', encoding="utf-8")  # Define the HTML template.
    htmlData = html.read()
    formatData = htmlData.format(title, formatMdData)  # Put the title and formatted md into the template.

# 表示処理
    name = os.path.splitext(os.path.basename(htmlName))[0]

    print("jam: ", name+".md", " >>> ", "Creating", name+".html")

    htmlFileName = name+'.html'
    writeHTMLFile = open("generate/"+htmlFileName, 'w', encoding="utf-8")
    writeHTMLFile.write(formatData)
    writeHTMLFile.close()
   


# ブログ機能を追加しました！ 使用する場合はコメントを外してください！

# mdOpen = open('assets/index.md', 'r', encoding="utf-8")
# mdData = mdOpen.read()
# md = markdown.Markdown()  # Create an instance?

# formatMdData = md.convert(mdData)  # To convert md to html, use md.convert.

# html = open('assets/base.html', 'r', encoding="utf-8")  # Define the HTML template.
# htmlData = html.read()
# formatData = htmlData.format(title, formatMdData)  # Put the title and formatted md into the template.

# # 表示処理
# name = os.path.splitext(os.path.basename(htmlName))[0]

# print("jam: ", "index.md", " >>> ", "Creating", "index.html")

# htmlFileName = 'index.html'
# writeHTMLFile = open("generate/"+htmlFileName, 'w', encoding="utf-8")
# writeHTMLFile.write(formatData)
# writeHTMLFile.close()
