# Python Playground

## Install

```bash
$ pipenv install --dev
```

## Run test

```bash
$ pipenv run test
```

## Mocking in pytest

When importing full package in the main file...

```python
import urllib.request

def download_example_com():
    file, header = urllib.request.urlretrieve("https://example.com")
    return file, header
```

...we have to use the full path of the library in patching

```python
from playground import download_example_com

def test_download_example_com(mocker):
    mocker.patch("urllib.request.urlretrieve", return_value=(1, 2))
    assert download_example_com() == (1, 2)
```

When importing only a partial using `from / import` syntax...

```python
from random import randint


def generate_random():
    return randint(1, 101)
```

... we have to use our own package name and the imported function in patching

```python
from playground import generate_random

def test_generate_random_with_mocker(mocker):
    mocker.patch("playground.randint", return_value=6)
    assert generate_random() == 6
```

For using `mocker.patch` the `pytest-mock` package has to be installed.
Other option is using the `monkeypatch` feature which is built in `pytest`.

```python
from playground import generate_random

def test_generate_random_with_monkeypatch(monkeypatch):
    monkeypatch.setattr("playground.randint", lambda x, y: 5)
    assert generate_random() == 5
```