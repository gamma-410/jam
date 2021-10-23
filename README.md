# pySSG
Markdown -> HTML StaticSiteGenerator.

## How to use
- pip install markdown
```shell
$ pip install markdown
```
- 1.main.py <code>line:33</code>
```python
formatData = htmlData.format("----", mdData)
# "----" = siteTitle.
```
- 2.terminal
```shell
$ python3 main.py (----.md) (----.html)
generate: -----.md >> ----.html 
```

## license
MIT license.
