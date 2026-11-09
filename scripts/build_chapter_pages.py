"""Write one static page per chapter (site/chapter-N.html) from site/chapter.html and the verse data.

Search engines skipped chapter.html?c=N because every URL served the same empty shell that filled itself by
script. Each chapter page now carries its own title, description, canonical URL and every verse in the HTML.
Run at deploy time (pages.yml) so corrections merged into the data show up on the next publish.
"""
import html
import json
import re
from pathlib import Path
from urllib.parse import urlencode

SITE = Path(__file__).resolve().parent.parent / "site"
BASE = "https://siribhoovalaya.com/"
REPO = "https://github.com/snrahulsn/siribhoovalaya"
FILES = ["1_8", "9_20", "21_33", "34_46", "47_59"]

tpl = (SITE / "chapter.html").read_text(encoding="utf-8")
chapters = json.loads((SITE / "data/chapters.json").read_text(encoding="utf-8"))
verses = {}
for f in FILES:
    for v in json.loads((SITE / f"data/verses_{f}.json").read_text(encoding="utf-8")):
        verses.setdefault(v["chapter"], []).append(v)

esc = lambda s: html.escape(s or "", quote=True)
GENERIC_DESC = "One chapter of the Siribhoovalaya, decoded from its number grids: each verse in Kannada, Roman letters and English, with a link to suggest corrections."
GENERIC_TITLE = "Siribhūvalaya chapter: Kannada text and English translation"


def issue(c, v):
    current = "\n\n".join(x for x in [v.get("kannada"), v.get("restored") or v.get("words"), v.get("translation")] if x)[:3000]
    return REPO + "/issues/new?" + urlencode({"template": "correction.yml", "title": f"Correction: chapter {c}, verse {v['n']}",
                                              "where": f"{c}.{v['n']}", "current": current})


def verse_html(c, v):
    by = v.get("corrected_by") or []
    credit = f'<span class="small muted"> · Corrected by {esc(", ".join("@" + u for u in by))}</span>' if by else ""
    return (f'<article class="v" id="v{v["n"]}"><div class="n"><a href="#v{v["n"]}" title="Link to this verse" style="text-decoration:none">{v["n"]}</a></div><div>'
            f'<div class="kn">{esc(v.get("kannada"))}</div><div class="ro">{esc(v.get("restored") or v.get("words"))}</div>'
            f'<div class="tr"><span class="tag">Rough machine translation</span><div class="mt">{esc(v.get("translation"))}</div></div>'
            f'<div class="add"><a class="linkbtn" target="_blank" rel="noopener" href="{esc(issue(c, v))}">Suggest a correction</a>{credit}</div></div></article>')


def page(c):
    summary = chapters[c - 1]["s"]
    title = f"Siribhūvalaya chapter {c}: Kannada text and English translation"
    desc = f"Chapter {c} of the Siribhūvalaya (Siribhoovalaya), decoded from its number grids into Kannada with an English draft. {summary}"
    url = f"{BASE}chapter-{c}.html"
    out = tpl.replace(GENERIC_TITLE, esc(title)).replace(GENERIC_DESC, esc(desc))
    out = out.replace(f'content="{BASE}chapter.html"', f'content="{url}"')
    out = out.replace("<!-- /seo -->", f'<link rel="canonical" href="{url}">\n<!-- /seo -->', 1)
    prev = f'<a class="btn" href="chapter-{c - 1}.html">← Chapter {c - 1}</a>' if c > 1 else "<span></span>"
    nxt = f'<a class="btn" href="chapter-{c + 1}.html">Chapter {c + 1} →</a>' if c < 59 else "<span></span>"
    main = f"""<main>
  <div class="frame top">
    <p class="eyebrow"><a href="chapters.html" style="text-decoration:none">Read the poem</a> / Chapter {c}</p>
    <h1>Chapter {c}</h1>
    <p class="lede" style="max-width:820px">{esc(summary)}</p>
    <div class="pager">{prev}{nxt}</div>
    <div class="signbar"><span>Read Old Kannada? Every verse has a link to suggest a correction.</span></div>
  </div>
  <div class="frame"><div class="verses">{"".join(verse_html(c, v) for v in sorted(verses.get(c, []), key=lambda v: v["n"]))}</div></div>
</main>"""
    out = re.sub(r"<main>.*?</main>", lambda _: main, out, count=1, flags=re.S)
    # the template's own script builds the page from ?c=; the static page needs only the shared layout script
    out = re.sub(r"<script>\s*const c = .*?</script>", "", out, count=1, flags=re.S)
    return out


for c in range(1, 60):
    (SITE / f"chapter-{c}.html").write_text(page(c), encoding="utf-8")
print("wrote 59 chapter pages")
