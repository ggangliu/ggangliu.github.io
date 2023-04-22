---
layout: page
title: Computer Architecture
show_position: home
permalink: /computer_architecture/
---

## Computer Architecture

## Nvidia GPU Architecture

{% for tag in site.tags %}
{% if tag[0] == "nvidia-arch" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}

## AMD GPU Architecture

{% for tag in site.tags %}
{% if tag[0] == "amd-arch" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}

## Other GPU Architecture

{% for tag in site.tags %}
{% if tag[0] == "other-arch" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}