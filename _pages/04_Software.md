---
layout: page
title: Software
show_position: home
permalink: /Software/
---

## Compiler

### Compiler Knowledge

{% for tag in site.tags %}
{% if tag[0] == "compiler" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}

### LLVM

{% for tag in site.tags %}
{% if tag[0] == "llvm" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}

## API

### OpenCL

{% for tag in site.tags %}
{% if tag[0] == "opencl" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}

### OpenGL

{% for tag in site.tags %}
{% if tag[0] == "opengl" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}


## Software

{% for tag in site.tags %}
{% if tag[0] == "software" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}