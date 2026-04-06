# SL-Identicon

![Sample Icon](output/1sample.png)
![Sample Icon](output/2sample.png)
![Sample Icon](output/3sample.png)
![Sample Icon](output/4sample.png)

Byte-sized identicon generation in Python. Inspired by [GitHub's Identicons](https://github.blog/news-insights/company-news/identicons/), which are used for default profile images.

## How to setup

Set up the python virtual environment:

```
python -m venv env
```

or

```
python3 -m venv env
```

Install pip packages:

```
pip install pillow
```

## How to run

To execute the program, ensure the virtual environment is active:

```
source ./env/bin/activate
```

and then run the following from the repo root:

```
python main.py <username>
```

or

```
python3 main.py <username>
```

where `<username>` is an optional argument to generate an identicon for the given username.
