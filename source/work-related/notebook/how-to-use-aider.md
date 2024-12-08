# Aider

<https://aider.chat/docs/install.html>

## Get API Key

- API Key
  anthropic
  
  ~~~ bash
  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
  ~~~
  
  Gemini

  ~~~ bash
  AIzaSyCS0y9ifGp6BsuVJNaqgQmZUDC__2QKZVo
  ~~~

  setx GEMINI_API_KEY AIzaSyCS0y9ifGp6BsuVJNaqgQmZUDC__2QKZVo
  aider --model gemini/gemini-1.5-pro-latest

  //List models available from Gemini
  aider --models gemini/

## Install

- windows install
  ~~~
  $ pip install aider-chat
  $ aider --openai-api-key sk-xxx... --4turbo
  $ aider
  ~~~
- Linux install
  ~~~
  $ pip install aider-chat
  $ aider --anthropic-api-key sk-xxx... --opus
  $ aider
  ~~~


## Optional

- store your key
  setx OPENAI_API_KEY sk-... in Windows PowerShell
  export OPENAI_API_KEY=sk-... on Linux or Mac
  

- Enable playwright
  playwright install --with-deps chromium

- Enable voice coding
  For Linux, do sudo apt-get install libportaudio2

- Add aider to your editor
  VS Code
  <https://marketplace.visualstudio.com/items?itemName=MattFlower.aider>

- Install development versions of aider
  python -m pip install git+https://github.com/paul-gauthier/aider.git
  python -m pip install -e .