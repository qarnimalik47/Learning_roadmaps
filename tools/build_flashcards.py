"""Build flashcards.js from the Anki decks in CCNA-Flashcards/.

The Revision tab reads every card from flashcards.js, so students never have to
download a deck or install Anki. Run this again after adding or changing a deck:

    pip install zstandard          (only needed once; newer decks are compressed)
    python tools/build_flashcards.py

It reads each .apkg (a zip holding an Anki SQLite database), keeps the Front and
Back of every note in the deck's own order, cleans the HTML down to bold, italic,
underline, superscript, subscript and line breaks, and writes flashcards.js next
to index.html. Card ids come from Anki's note ids, so revision progress survives
a rebuild.
"""
import html
import json
import os
import re
import sqlite3
import sys
import tempfile
import zipfile
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DECKS = os.path.join(ROOT, "CCNA-Flashcards")
OUT = os.path.join(ROOT, "flashcards.js")

INLINE = {"b": "b", "strong": "b", "i": "i", "em": "i", "u": "u", "sup": "sup", "sub": "sub"}
BLOCK = {"div", "p", "li", "ul", "ol", "tr", "table", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "pre"}


class Clean(HTMLParser):
    """Keep a few inline tags, turn blocks and <br> into line breaks, drop the rest."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.open = [], []

    def brk(self):
        self.out.append("\n")

    def handle_starttag(self, tag, attrs):
        if tag == "br" or tag in BLOCK:
            self.brk()
        elif tag in INLINE:
            t = INLINE[tag]
            self.out.append(f"<{t}>")
            self.open.append(t)

    def handle_startendtag(self, tag, attrs):
        if tag == "br":
            self.brk()

    def handle_endtag(self, tag):
        if tag in BLOCK:
            self.brk()
        elif tag in INLINE:
            t = INLINE[tag]
            if t in self.open:
                while self.open:
                    x = self.open.pop()
                    self.out.append(f"</{x}>")
                    if x == t:
                        break

    def handle_data(self, data):
        self.out.append(html.escape(data.replace("\xa0", " "), quote=False))

    def result(self):
        s = "".join(self.out) + "".join(f"</{t}>" for t in reversed(self.open))
        s = re.sub(r"<(b|i|u|sup|sub)>(\s*)</\1>", r"\2", s)
        s = re.sub(r"[ \t]+", " ", s)
        s = re.sub(r" *\n *", "\n", s)
        s = re.sub(r"\n{3,}", "\n\n", s).strip()
        return s.replace("\n", "<br>")


def clean(fragment):
    p = Clean()
    p.feed(fragment)
    p.close()
    return p.result()


def b36(n):
    s, d = "", "0123456789abcdefghijklmnopqrstuvwxyz"
    while True:
        n, r = divmod(n, 36)
        s = d[r] + s
        if not n:
            return s


def open_db(z, tmp):
    names = z.namelist()
    path = os.path.join(tmp, "collection.db")
    if "collection.anki21b" in names:
        try:
            import zstandard
        except ImportError:
            sys.exit("This deck needs the zstandard package: pip install zstandard")
        with open(path, "wb") as f:
            f.write(zstandard.ZstdDecompressor().stream_reader(z.read("collection.anki21b")).read())
    else:
        with open(path, "wb") as f:
            f.write(z.read("collection.anki21" if "collection.anki21" in names else "collection.anki2"))
    return sqlite3.connect(path)


def natural(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]


def main():
    decks, seen, total = [], set(), 0
    for fn in sorted((f for f in os.listdir(DECKS) if f.lower().endswith(".apkg")), key=natural):
        with tempfile.TemporaryDirectory() as tmp, zipfile.ZipFile(os.path.join(DECKS, fn)) as z:
            con = open_db(z, tmp)
            rows = con.execute(
                "select n.id, n.flds from cards c join notes n on n.id = c.nid "
                "where c.ord = 0 order by c.type, c.due, n.id"
            ).fetchall()
            con.close()
        cards = []
        for nid, flds in rows:
            parts = flds.split("\x1f")
            front, back = clean(parts[0]), clean(parts[1] if len(parts) > 1 else "")
            if not front:
                continue
            cid = b36(nid)
            while cid in seen:
                cid += "x"
            seen.add(cid)
            cards.append([cid, front, back])
        decks.append({"f": fn, "c": cards})
        total += len(cards)
        print(f"{len(cards):4}  {fn}")
    body = json.dumps({"decks": decks}, ensure_ascii=True, separators=(",", ":"))
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("/* CCNA flashcards from the Anki decks in CCNA-Flashcards/, for the Revision tab. "
                "Built by tools/build_flashcards.py: rebuild it rather than editing by hand. */\n")
        f.write(f"window.CCNA_FLASHCARDS={body};\n")
    print(f"{total} cards from {len(decks)} decks -> {os.path.relpath(OUT, ROOT)} ({os.path.getsize(OUT) // 1024} KB)")


if __name__ == "__main__":
    main()
