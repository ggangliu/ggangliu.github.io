---
layout: page
title: Other Chips
show_position: home
permalink: /Other/
---

## Loogson

{% for tag in site.tags %}
{% if tag[0] == "other-chips" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}
