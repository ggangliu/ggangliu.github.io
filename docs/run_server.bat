sphinx-autobuild ./source ./docs --host=0.0.0.0 --port=80 --open-browser

:: python -m http.server -d .\docs -b 0.0.0.0 80