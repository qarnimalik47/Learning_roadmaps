"""Build the web copies of the CCNA module slides from export_slides.ps1's PNG files.

    python tools/build_slides.py --png C:/temp/slide-png --decks slides --out slides

Writes, for every slide of every module:
  slides/m<N>/<nnn>.webp     the slide at 1600x900, shown in the slide viewer
  slides/m<N>/t/<nnn>.webp   a 400x225 thumbnail for topic cards and the filmstrip
and slides/text.js, the words on each slide (read from the .pptx files), which the
Revision tab uses to search the slides and to describe each slide to screen readers.

Which slides make up each topic, and the quick-revision picks, live in index.html (SLIDE_MODULES).
"""
import argparse
import json
import os
import re
import zipfile
from xml.etree import ElementTree as ET

from PIL import Image

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}
FULL, THUMB = (1600, 900), (400, 225)


def slide_paths(z):
    """Slide XML paths in presentation order."""
    pres = ET.fromstring(z.read("ppt/presentation.xml"))
    rels = ET.fromstring(z.read("ppt/_rels/presentation.xml.rels"))
    target = {r.get("Id"): r.get("Target") for r in rels}
    ids = [s.get("{%s}id" % NS["r"]) for s in pres.find("p:sldIdLst", NS)]
    return ["ppt/" + target[i].lstrip("/").replace("ppt/", "") for i in ids]


def slide_text(xml):
    """Every paragraph on the slide (text boxes, tables and groups), in reading order."""
    out = []
    for para in ET.fromstring(xml).iter("{%s}p" % NS["a"]):
        t = "".join(x.text or "" for x in para.iter("{%s}t" % NS["a"]))
        t = re.sub(r"\s+", " ", t.replace("\u00a0", " ")).strip()
        if t and t.lower() != "made with gamma" and (not out or out[-1] != t):
            out.append(t)
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--png", required=True, help="folder with m1, m2, ... from export_slides.ps1")
    ap.add_argument("--decks", required=True, help="folder with the Module N ... .pptx files")
    ap.add_argument("--out", required=True, help="the site's slides folder")
    a = ap.parse_args()

    text = {}
    for name in sorted(os.listdir(a.decks)):
        m = re.match(r"Module (\d+) .*\.pptx$", name)
        if not m:
            continue
        mod = m.group(1)
        with zipfile.ZipFile(os.path.join(a.decks, name)) as z:
            text[mod] = [slide_text(z.read(p)) for p in slide_paths(z)]

        src = os.path.join(a.png, "m" + mod)
        dst = os.path.join(a.out, "m" + mod)
        os.makedirs(os.path.join(dst, "t"), exist_ok=True)
        pngs = sorted(f for f in os.listdir(src) if f.endswith(".png"))
        if len(pngs) != len(text[mod]):
            raise SystemExit(f"Module {mod}: {len(pngs)} PNG files but {len(text[mod])} slides in {name}")
        for f in pngs:
            im = Image.open(os.path.join(src, f)).convert("RGB")
            webp = f[:-4] + ".webp"
            im.resize(FULL, Image.LANCZOS).save(os.path.join(dst, webp), "WEBP", quality=82, method=6)
            im.resize(THUMB, Image.LANCZOS).save(os.path.join(dst, "t", webp), "WEBP", quality=70, method=6)
        print(f"Module {mod}: {len(pngs)} slides")

    with open(os.path.join(a.out, "text.js"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("/* Words on each CCNA module slide, by module, in slide order. Built by tools/build_slides.py. */\n")
        fh.write("window.DT_SLIDE_TEXT=" + json.dumps(text, ensure_ascii=False, separators=(",", ":")) + ";\n")
    print("text.js written")


if __name__ == "__main__":
    main()
