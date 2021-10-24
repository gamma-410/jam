# pySSG
Markdown -> HTML StaticSiteGenerator.

## How to use
- install
```shell
$ git clone https://github.com/moka-drip/pySSG.git
$ pip install markdown
```
- 1.main.py <code>line:33</code>
```python
formatData = htmlData.format("----", mdData)
# "----" = siteTitle.
```


- 2.writing markdown.
```
---

YYYY・MM・DD
# Title.

---

  {article}

---
```

- 3.terminal
```shell
$ python3 main.py (----)
generate: ----.md >> ----.html 
``` 

## license
MIT license.

## Copyright
Copyright 2021 dr-notes.work (@moka-drip.)
