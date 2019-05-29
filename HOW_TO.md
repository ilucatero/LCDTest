# HOW TO RUN IT

## Install locally

This script, it requires Python3.7 and pip3.

To be able to run this script locally, just create a Python virtual env.

Linux version:

```console
virtualenv venv
source venv/bin/activate
pip install --upgrade pip
pip install --upgrade setuptools
# below line may require a previous yum/apt install for : unixodbc-dev, python3.7-dev
pip install -r requirements.txt
```

Windows version:

```console
python -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip
pip install --upgrade setuptools
pip install -r requirements.txt
```

Before exit, once you've done, exit the virtual env:

```console
deactivate
```

## Run unit test

```python
python test/testMain.py
```