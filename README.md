# Sum up 23 November's world news in one image

Entry for the make.fun bounty
[`news-image-20261123`](https://make.fun/bounty/news-image-20261123):
a program that writes one image summing up the world's news of
Monday 23 November 2026.

The image is a newspaper front page. Lead story: the COP31 climate talks
in Turkey collapse — the longest UN climate summit on record ends with no
deal. Also covered: Ukraine's naval drones sinking a Russian warship off
Libya, Iran's heaviest missile week in a year, a deadly factory fire in
Indonesia, the Democrats winning 258 US House seats, Bitcoin plunging to
$55,100, and the capture of "El Chapo Isidro" in Mexico.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). Running it
twice writes the same bytes.

## License

MIT — see `LICENSE`.
