# Conda

## be used with conda

conda list -e > package_conda.txt
conda create --name <env> --file package_conda.txt

## be used with conda env

``` sh
conda env export > environment.yaml 
conda env create -f environment.yaml
```

## be used with pip

pip freeze > package_conda.txt
pip install -r package_conda.txt