window.SITE_REPO = 'https://github.com/snrahulsn/siribhoovalaya';
// Shared header and footer for every page; marks the current page in the nav.
(function () {
  const pages = [["index.html#film", "Video"], ["read.html", "How it's read"], ["chapters.html", "Read the poem"], ["texts.html", "Hidden texts"], ["play.html", "Try it out"]];
  const here = (location.pathname.split("/").pop() || "index.html").replace(/^chapter\.html$/, "chapters.html");
  const nav = pages.map(([href, label]) => `<a href="${href}"${href.split("#")[0] === here ? ' aria-current="page"' : ""}>${label}</a>`).join("") + `<a href="siribhuvalaya-data.zip" download title="Grids, Kannada text, English drafts, hidden texts and checks · zip, 2.8 MB">Download data</a><a class="nav-cta" href="help.html">Help</a>`;
  document.body.insertAdjacentHTML("afterbegin",
    `<header class="site-head"><div class="frame"><a class="logo" href="index.html"><img src="favicon.svg" alt="">Siribhūvalaya</a><nav class="site-nav" aria-label="Main">${nav}</nav></div></header>`);
  document.body.insertAdjacentHTML("beforeend",
    `<footer class="site-foot"><div class="frame"><span>With thanks to Yellappa Shastri, who acquired the manuscript and spent his life on it; Karlamangalam Srikantaiah and K. Ananthasubba Rao, who worked with him and typed out its tables; Sudharthi of Hassan, who traced its hidden texts by hand; Anil Kumar Jain; Aruhant Mehta, whose public code reads its grids; and <a href="https://www.youtube.com/@kagwadspkumudendarthi" target="_blank" rel="noopener">Dr S. P. Kagwad</a>. Their material was invaluable in validating our output.</span><span>Grids from the National Archives of India (Abhilekh Patal, Acc. 507). Data, tools and corrections on <a href="${window.SITE_REPO}" target="_blank" rel="noopener">GitHub</a>.</span><span>A non-commercial project. Nothing here is for sale.</span></div></footer>`);
})();
// Links that do not exist yet: fill these in when they do.
window.SITE_LINKS = { github: "https://github.com/snrahulsn/siribhoovalaya", youtube: "zEp2OFqFVb8", howto: "" };
// Page-visit counter (GoatCounter: no cookies, private dashboard). Not counted on local previews.
if (!/^(localhost|127\.0\.0\.1)$/.test(location.hostname)) {
  const s = document.createElement('script'); s.async = true; s.src = 'https://gc.zgo.at/count.js';
  s.dataset.goatcounter = 'https://siribhoovalaya.goatcounter.com/count'; document.head.appendChild(s);
}
