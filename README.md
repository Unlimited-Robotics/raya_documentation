# raya_documentation
Documentation related to RaYa

## Prepare environment
### Install virtual environments
```bash
sudo apt install python3-venv
```

### Create virtual environmet and install requirements
```bash
python3 -m venv raya-documentation-venv
source raya-documentation-venv/bin/activate
pip install -r requirements.txt
```

### Install PyRaya inside 
```bash
python3 -m venv raya-documentation-venv
source raya-documentation-venv/bin/activate
pip install -r requirements.txt
```

### Pandoc util

Convert MD to RST with pandoc
```bash
sudo apt install pandoc

# set columns to 100
pandoc table.md --from markdown --columns=100 --to rst -s -o table.rst
```

## install sphinx theme
```bash

git submodule update --init
git submodule update --remote

python3 -m pip install -e sphinx-wagtail-theme/.
```
