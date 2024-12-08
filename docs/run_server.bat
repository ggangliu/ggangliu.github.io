sphinx-autobuild ./docs/source ./docs/build/html --host=0.0.0.0 --port=80 --open-browser

:: python -m http.server -d .\docs\html -b 0.0.0.0 80