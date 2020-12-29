# Okaeri

*Okaeri (おかえり)* is a simple homepage generator written in Python. It's mainly composed of 4 files:

* `okaeri.py`
* `links.oka`
* Inside `html`:
    - `homepage.html`
    - `template.html`
    - `+ css files`
    
### Dependencies
* [Mako](http://www.makotemplates.org/)

### How to use
First, you'd like to edit `links.oka` to fit your own needs. In this file, we'll have sections
like the following:
```
# download
nyaa https://nyaa.si/
libgen https://libgen.pw/
mangadex https://mangadex.org/

# images
pixiv https://www.pixiv.net/
wikiart https://www.wikiart.org/

# etc.
archwiki https://wiki.archlinux.org/
tvtropes http://tvtropes.org/
vndb https://vndb.org/
```
Where every line starting with `#` corresponds to a different section (or
"category"), and every line following it until the next `#` are the items of said section. Each item has a label + url pair. 

For example, we can read the hierarchy as it follows: `nyaa https://nyaa.si/` is an *item* of *section* `# download`, where `nyaa` is the *label* for the `https://nyaa.si/` *url*.

After modifying `links.oka`, you need to run `make [theme]`, where `[theme]` is the name of one of the css files available (if no theme is specified, it'll default to `dark`). `okaeri.py` will parse `links.oka` and create individual tuples with the required information. With Mako, we'll generate our `homepage.html` using the file `template.html` as a template.

To finally see the results, open `homepage.html` in your favorite browser. If
you want different looks, you can always modify `template.html` and the css files to fit your tastes.
