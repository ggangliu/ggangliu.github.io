---
layout: page
title: RISCV
show_position: home
permalink: /RISCV/
---

## RISC-V Basic Knowledge

{% for tag in site.tags %}
{% if tag[0] == "riscv" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}

## First RISC-V

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
