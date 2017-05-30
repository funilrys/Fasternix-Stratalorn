# Fasternix Stratalorn (Transifex Translators)

> Python module/library for saving the list of translators of a given Transifex project into a JSON file.

## Versions

**Current version of the repository:** _1.0.0_ 
**Transifex API version:** _2_

## Freatures

- Works with python3.x **ONLY**
- Access transifex project details
- Get list of translators of a whole project

## Installation

### From Github

```bash
https://github.com/funilrys/Fasternix-Stratalorn.git
cd Fasternix-Stratalorn && python setup.py install
```

## Create executable

```bash
# This allow you to execute fasternix-stratalorn from everywhere into the terminal
ln -s /usr/lib/python3.6/site-package/fasternix_stratalorn/__init__.py /usr/bin/fasternix-stratalorn
```

--------------------------------------------------------------------------------

# How to contribute?

To contribute, you have to **send a new [Pull Request](https://github.com/funilrys/Fasternix-Stratalorn/compare)** after you **[forked](https://github.com/funilrys/Fasternix-Stratalorn/pulls#fork-destination-box)** and edited the script(s).

## :warning: WARNING :warning:

### DO NOT FORGET

- To sign your commit(s) with **"Signed-off by: FirstName LastName < email at service dot com >"** _**and/or**_ simply **sign your commit(s)** with **PGP** _(Please read more [here](https://github.com/blog/2144-gpg-signature-verification))_.
- All **contributions/modifications** must be done under **the `dev` or a new branch** if you plan to **send a new [Pull Request](https://github.com/funilrys/Fasternix-Stratalorn/compare)**.
- :warning::warning::warning: Every **contributions/modifications** which are under **master** _(exception for minor changes)_ **will not be merged**.

--------------------------------------------------------------------------------

# Example of usage

```bash
# This save the output into your current location
$ fasternix-stratalorn
Transifex username: funilrys
Transifex password:
Transifex project_slug: hello-world-fake
List of af translators obtained
[...]
List of vi_VN translators obtained
You can find your list of translators into /home/funilrys/translators.json =)
```

--------------------------------------------------------------------------------

# License

```
MIT License

Copyright (c) 2017 Nissar Chababy <contact at funilrys dot com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
