---
layout: post
title: "Jekyll on Ubuntu"
tags: jekyll
---

## Install

Install Ruby

```bat
sudo apt-get install ruby-full build-essential zlib1g-dev
```

Adding environment variables to ~/.bashrc

```sh
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Finally, install Jekyll and Bundler:

```bat
gem install jekyll bundler
```

## Start local github service

```bat
cd ggangliu.github.io
jekyll serve --watch
```

Then, localhost:4000

## How to create a subscribe form on Jekyll blog

[How to create a subscribe form on Jekyll blog](https://blog.webjeda.com/jekyll-subscribe-form/#how-to-create-a-subscribe-form-on-jekyll-blog)
[Jekyll Contact Form Creation with Added Security](https://blog.webjeda.com/jekyll-contact-form/)
