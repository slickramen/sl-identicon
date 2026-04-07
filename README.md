# SL-Identicon

![Sample Icon](output/1sample.png)
![Sample Icon](output/2sample.png)
![Sample Icon](output/3sample.png)
![Sample Icon](output/4sample.png)

Byte-sized identicon generation in Python. Inspired by [GitHub's Identicons](https://github.blog/news-insights/company-news/identicons/), which are used for default profile images.

## How to set up

Set up the Python virtual environment:

```
python3 -m venv env
```

Activate the virtual environment:

```
source ./env/bin/activate
```

Install pip packages:

```
pip install pillow
```

## How to run

Run the following from the repo root:

```
python3 main.py <username>
```

where `<username>` is an optional argument to generate an identicon for the given username. If no username is provided, a default sample identicon will be generated.
