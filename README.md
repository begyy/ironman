<img src="http://i.imgur.com/qjeYbqX.png" width="350" align="right" alt="iron man" />

# Ironman

[![Build Status](https://travis-ci.org/kratsg/ironman.svg?branch=master)](https://travis-ci.org/kratsg/ironman)
[![Coverage Status](https://coveralls.io/repos/kratsg/ironman/badge.svg?branch=master&service=github)](https://coveralls.io/github/kratsg/ironman?branch=master)
[![Code Health](https://landscape.io/github/kratsg/ironman/master/landscape.svg?style=flat)](https://landscape.io/github/kratsg/ironman/master) [![Docs](https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat)](http://iron-man.readthedocs.org/en/latest/)

## What is Ironman?

Ironman is a general purpose software toolbox to be run on L1Calo hardware with embedded processors (SoCs).

Look how easy it is to use

```
    import ironman
    # Get your stuff done
    ironman.engage()
```

## Features

- Be awesome
- Make things faster

# Getting Started

## Installing

Install ironman by running

```
pip install ironman
```

## Developing

If it is your first time...

```
git clone git@github.com:kratsg/ironman
cd ironman && mkvirtualenv ironman
pip install -r requirements.txt
```

and then afterwards...

```
workon ironman
python setup.py develop
... do work here ...
pip uninstall ironman
```

### Testing

```
tox
```

or with

```
py.test
```

## Contributing

- [Issue Tracker](https://github.com/kratsg/ironman/issues)
- [Source Code](https://github.com/kratsg/ironman)

## Support

If you are having issues, let us know.

# Tutorial

Since we will be predominantly using Twisted within the Zynq to manage the Reactor workflow ("callbacks"), I suggest reading through [this tutorial](http://krondo.com/?page_id=1327) on your own time to get up to speed on how it works and some details of sockets.

I'm following the guide based on `sandman` [here](https://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)

## To Do

- split udp and tcp into different, separate protocols: http://stackoverflow.com/questions/33224142/twisted-protocol-that-simultaneously-handles-tcp-and-udp-at-once

## Ideas

- make it like twisted.web - we build Request objects which need to find Resource objects that provide actions (maybe too complicated, try and simplify?) [link](http://twistedmatrix.com/trac/browser/trunk/twisted/web)


