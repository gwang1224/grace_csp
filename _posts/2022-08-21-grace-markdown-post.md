---
toc: true
layout: post
description: A minimal example of using markdown with fastpages.
categories: [markdown]
title: Markdown Post Tips
image: images/code.png

---
# Grace's First Markdown Post 🤪

## Setup

# Heading 1
## Heading 2
### Heading 3
#### Heading 4

- Markdown file format: 
    - `YEAR-MONTH-DAY-filename.md`
- include Python code
- *italics*
- **bold**
- `code font text`
- create [links](https://github.com/gwang1224/repository_1)
- lists
    1. item 1
    2. item 2

> quotation

{% include alert.html text="Alert Box!" %}

{% include info.html text="Info Box!" %}

![]({{ site.baseurl }}/images/graceblog.png "Grace Blog Photo")

General preformatted text:

    # Do a thing
    do_thing()

Python code and output: [^1]

```python
# Prints 'Hello World'
print("Hello World")
```

    Hello World

Shell command
```shell
echo "hello world"
./some_script.sh --option "value"
wget https://example.com/cat_photo1.png
```

Yaml
```yaml
key: value
- another_key: "another value"
```

Cool Tables

| I | like |
|-|-|
| tables | :) |

{% twitter https://twitter.com/AP_Trevor/status/1540016855691190274 %}

[^1]: This is a footnote
