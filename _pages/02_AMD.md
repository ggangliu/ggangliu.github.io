---
layout: page
title: AMD
show_position: home
permalink: /AMD/
---

## GCN1 Architecture

{% for tag in site.tags %}
{% if tag[0] == "amd" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}

### first-riscv

#### Architecture Design

- register_file
- alu
- csr
- mem
  - rom
  - ram
