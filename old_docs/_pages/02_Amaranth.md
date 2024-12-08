---
layout: page
title: Amaranth
show_position: home
permalink: /Amaranth/
---

## Digital Design

{% for tag in site.tags %}
{% if tag[0] == "digitial-design" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}

## [Amaranth HDL](https://amaranth-lang.org/docs/amaranth/latest/)

{% for tag in site.tags %}
{% if tag[0] == "amaranth" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}
