---
layout: page
title: Chips
show_position: home
permalink: /Chips/
---

## Nvidia

{% for tag in site.tags %}
{% if tag[0] == "nvidia-chips" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}

## AMD

{% for tag in site.tags %}
{% if tag[0] == "amd-chips" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}

## Other-chips

{% for tag in site.tags %}
{% if tag[0] == "other-chips" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}
