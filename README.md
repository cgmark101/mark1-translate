# Mark1 Translator

This is a small tool to translate from Google Translate, base on mtranslate by [mouuff](https://github.com/mouuff)

It was reduce to the minimum expression and converted to use requests

# Install
It is highly recommended to use it inside a virtual enviroment for your project, but can be install globally

Note: this instructions are made for ubuntu

```bash
$ pip3 install mark1_translate
```

```bash
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install mark1_translate
$ python3
```

# Example

## On interactive console type

```py
>>> from mark1_translate imprt translate
>>> translate('hola mundo', 'en', 'auto')
'Hello World'
```

## On a project

```py
from mark1_translate imprt translate

t = translate('hola mundo', 'en', 'auto')

print(t)
```


