# Sphinx Document

```
sphinx-quickstart docs
```

Now to render it with the new content, you can use the sphinx-build command as before, or leverage the convenience script as follows:

``` sh
cd docs
sphinx-build -M html docs/source/ docs/build/
make html
```

## Other format document

- Epub

make epub

- PDF

latex:

``` sh
make latexpdf
```

easypdf:

``` sh
make simplepdf
or
sphinx-build -M simplepdf .\docs\source\ .\docs\build
```

rst2pdf:

``` sh
sphinx-build -b pdf doc/source doc/build
```

- autobuild

``` sh
sphinx-autobuild ./source ./build/html --host=0.0.0.0 --port=80 --open-browser

:: python -m http.server -d ./build/html -b 0.0.0.0 80

```

## Reference

- <https://www.sphinx-doc.org/en/master/tutorial/first-steps.html>
- <https://sphinx-simplepdf.readthedocs.io/en/latest/index.html>