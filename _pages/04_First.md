---
layout: page
title: First
show_position: home
permalink: /First/
---

## first-riscv

### Architecture Design

- register_file
- alu
- csr
- mem
  - rom
  - ram

{% for tag in site.tags %}
{% if tag[0] == "first" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}
