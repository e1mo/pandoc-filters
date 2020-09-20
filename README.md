# Pandoc-Filters

Pandoc has support for custom filters. CodiMD offers a style of `[name=foobar]` to display the name besides a little user icon. Our Dokuwiki installation over at @chaos-jetzt however, has all the user-pages in the `name:` namespace. Therefore, we need a mapping.

## Installation

```bash
git clone https://github.com/e1mo/pandoc-filters.git
cd pandoc-filters
pip3 install -r requirements.txt
ln -s codimd-name-to-dokuwiki-name.py ~/.local/bin/codi2dokuwiki
```

## Usage

Now you can pass `codi2dokuwiki` as a pandoc filter like so:

```
pandoc myfile.md -t dokuwiki --filter codi2dokuwiki
```

You can also download a CodiMD pad and pass it directly to pandoc:

```bash
$ curl -s https://demo.codimd.org/2vvSltaARLyjioyz2kpFeQ/download/markdown |
        pandoc -f markdown -t dokuwiki --filter=codi2dokuwiki

====== TOP 1 (e1mo) ======

  * We are going to have a walk in the park with [[name:dumbledore|dumbledore]]
  * This has been apprechiated by [[name:Linus|Linus]]
```

The markdown for this example is:

```markdown
# TOP 1 [name=e1mo]

- We are going to have a walk in the park with [name=dumbledore]
- This has been apprechiated by [name=Linus]
```

## License

Released under the [BSD-3-Clause](LICENSE) by [Moritz 'e1mo' Fromm](https://github.com/e1mo/)
