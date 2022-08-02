# 🍓 jam
markdown -> HTML PageGenerator.

## How to use 
- clone jam
- install <code>markdown</code>
```bash
$ git clone https://github.com/gamma-410/jam.git
$ cd jam
$ pip install markdown
```

## (1) generate HTML
### customize <code>main.py</code> <code>line: 9</code>

```python
title = " (HTML Pages Name) "

```
### customize <code>base.html</code>   
assets/base.html
```html
<!doctype html>
<html lang="ja">
  
<head>
<meta charset="utf-8"><meta name="robots" content="noindex,nofollow">
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{}</title>
<link rel="stylesheet" href="style.css">
</head>

<body>
{}
</body>
  
<html>
```

### make <code>markdownFile</code>
content/ ~ .md
```md
(date)
---
(title)
---
・・・




---

```

### run <code>main.py</code>
```bash
$ python3 main.py
~ .md  >>>  Creating ~ .html
```


## (2) generate Index Pages.
### remove comment out <code>main.py</code> <code>line:20 ~ 29</code> and <code>57 ~ 75</code>
```python

# ブログ機能を追加しました！ 使用する場合はコメントを外してください！

# mdデータを準備
    indexMdOpen = open('assets/index.md', encoding='utf-8')
    s = indexMdOpen.read()

    name1 = os.path.splitext(os.path.basename(htmlName))[0]
    s = '- [' + name1 + ' - ' + date + ']' + '(' + name1 + '.html)  \n' + s
    
    indexMdOpen = open('assets/index.md', 'w', encoding='utf-8')
    indexMdOpen.write(s)

    indexMdOpen.close()
```

```python
# ブログ機能を追加しました！ 使用する場合はコメントを外してください！

mdOpen = open('assets/index.md', 'r', encoding="utf-8")
mdData = mdOpen.read()
md = markdown.Markdown()  # Create an instance?

formatMdData = md.convert(mdData)  # To convert md to html, use md.convert.

html = open('assets/base.html', 'r', encoding="utf-8")  # Define the HTML template.
htmlData = html.read()
formatData = htmlData.format(title, formatMdData)  # Put the title and formatted md into the template.

# 表示処理
name = os.path.splitext(os.path.basename(htmlName))[0]

print("jam: ", "index.md", " >>> ", "Creating", "index.html")

htmlFileName = 'index.html'
writeHTMLFile = open("generate/"+htmlFileName, 'w', encoding="utf-8")
writeHTMLFile.write(formatData)
writeHTMLFile.close()
```

## license
MIT