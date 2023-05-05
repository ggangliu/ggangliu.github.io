---
layout: page
title: Contact
show_position: home
permalink: /Contact/
---

Questions, comments, and discussions can be posted on [ggangliu](https://groups.google.com/g/ggangliu).

<form action="https://formspree.io/f/mlekangy" method="POST">
  <label>
    Your email:
    <input type="email" name="email">
  </label>
  <label>
    Your message:
    <textarea name="message"></textarea>
  </label>
  <button type="submit">Send</button>
</form>
<input type="hidden" name="_next" value="thanks.html" />
<input type="text" name="_gotcha" style="display:none" />

## Project

{% for tag in site.tags %}
{% if tag[0] == "project" %}
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}