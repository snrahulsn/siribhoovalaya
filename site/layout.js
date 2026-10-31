window.SITE_REPO = 'https://github.com/snrahulsn/siribhoovalaya';
// Shared header and footer for every page; marks the current page in the nav.
(function () {
  const pages = [["index.html#film", "Video"], ["read.html", "How it's read"], ["chapters.html", "Read the poem"], ["texts.html", "Hidden texts"], ["play.html", "Try it out"]];
  const here = (location.pathname.split("/").pop() || "index.html").replace(/^chapter\.html$/, "chapters.html");
  const nav = pages.map(([href, label]) => `<a href="${href}"${href.split("#")[0] === here ? ' aria-current="page"' : ""}>${label}</a>`).join("") + `<a href="siribhuvalaya-data.zip" download title="Grids, Kannada text, English drafts, hidden texts and checks · zip, 2.8 MB">Download data</a><a class="nav-cta" href="help.html">Help</a>`;
  const ico = {
    gh: '<svg viewBox="0 0 16 16" aria-hidden="true"><path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38v-1.34c-2.23.48-2.7-1.07-2.7-1.07-.36-.92-.89-1.17-.89-1.17-.73-.5.06-.49.06-.49.8.06 1.23.83 1.23.83.72 1.22 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.78-.2-3.65-.89-3.65-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.6 7.6 0 0 1 4 0c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48v2.2c0 .21.15.46.55.38A8 8 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>',
    x: '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M18.9 2H22l-6.8 7.8L23 22h-6.2l-4.9-6.4L6.3 22H3.2l7.3-8.3L1 2h6.4l4.4 5.8L18.9 2zm-1.1 18h1.7L6.3 3.9H4.5L17.8 20z"/></svg>',
    yt: '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4l6.3 3.6-6.3 3.6z"/></svg>',
    ig: '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor"/></svg>',
    share: '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M12 3v13M7 8l5-5 5 5M5 13v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6"/></svg>'
  };
  const social = `<div class="social"><a href="${window.SITE_REPO}" target="_blank" rel="noopener" aria-label="GitHub" title="GitHub">${ico.gh}</a><a href="https://x.com/the_indophile" target="_blank" rel="noopener" aria-label="The Indophile on X" title="X">${ico.x}</a><a href="https://www.youtube.com/channel/UCsVH0ZIvAbplkY_3YhCI4fg" target="_blank" rel="noopener" aria-label="The Indophile on YouTube" title="YouTube">${ico.yt}</a><a href="https://www.instagram.com/the_indophile_labs/" target="_blank" rel="noopener" aria-label="The Indophile on Instagram" title="Instagram">${ico.ig}</a><button type="button" class="share-btn" aria-label="Share this page">${ico.share}<span>Share</span></button><div class="share-menu" hidden><a data-share="x" target="_blank" rel="noopener">Post on X</a><a data-share="wa" target="_blank" rel="noopener">WhatsApp</a><button type="button" data-share="copy">Copy link</button></div></div>`;
  document.body.insertAdjacentHTML("afterbegin",
    `<header class="site-head"><div class="frame"><a class="logo" href="index.html"><img src="favicon.svg" alt="">Siribhūvalaya</a><nav class="site-nav" aria-label="Main">${nav}</nav></div></header>`);
  document.body.insertAdjacentHTML("beforeend",
    `<footer class="site-foot"><div class="frame"><span>With thanks to Yellappa Shastri, who acquired the manuscript and spent his life on it; Karlamangalam Srikantaiah and K. Ananthasubba Rao, who worked with him and typed out its tables; Sudharthi of Hassan, who traced its hidden texts by hand; Anil Kumar Jain; Aruhant Mehta, whose public code reads its grids; and <a href="https://www.youtube.com/@kagwadspkumudendarthi" target="_blank" rel="noopener">Dr S. P. Kagwad</a>. Their material was invaluable in validating our output.</span><span>Grids from the National Archives of India (Abhilekh Patal, Acc. 507). Data, tools and corrections on <a href="${window.SITE_REPO}" target="_blank" rel="noopener">GitHub</a>.</span><span>A non-commercial project. Nothing here is for sale. Follow The Indophile on <a href="https://www.youtube.com/channel/UCsVH0ZIvAbplkY_3YhCI4fg" target="_blank" rel="noopener">YouTube</a> and <a href="https://x.com/the_indophile" target="_blank" rel="noopener">X</a>, and <a href="https://www.instagram.com/the_indophile_labs/" target="_blank" rel="noopener">Instagram</a>.</span>${social}</div></footer>`);
  // Side rail with the same links; a small tab slides it in and out (remembered per visitor).
  document.body.insertAdjacentHTML("beforeend", `<aside class="side-rail" aria-label="Share and follow">${social}<button type="button" class="rail-tab" aria-label="Hide or show share links"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M15 6l-6 6 6 6"/></svg></button></aside>`);
  const rail = document.querySelector(".side-rail");
  try { if (localStorage.getItem("railHidden") === "1") rail.classList.add("hidden"); } catch (e) {}
  rail.querySelector(".rail-tab").addEventListener("click", () => {
    rail.classList.toggle("hidden");
    try { localStorage.setItem("railHidden", rail.classList.contains("hidden") ? "1" : "0"); } catch (e) {}
  });
  // Share: the phone's own share sheet where there is one, else a small menu (X, WhatsApp, copy link).
  document.querySelectorAll(".social").forEach((box) => {
    const btn = box.querySelector(".share-btn"), menu = box.querySelector(".share-menu");
    const url = location.origin + location.pathname, text = document.title;
    menu.querySelector('[data-share="x"]').href = "https://x.com/intent/post?url=" + encodeURIComponent(url) + "&text=" + encodeURIComponent(text);
    menu.querySelector('[data-share="wa"]').href = "https://wa.me/?text=" + encodeURIComponent(text + " " + url);
    menu.querySelector('[data-share="copy"]').addEventListener("click", (e) => {
      navigator.clipboard && navigator.clipboard.writeText(url).then(() => { e.target.textContent = "Copied"; setTimeout(() => { e.target.textContent = "Copy link"; }, 1500); });
    });
    btn.addEventListener("click", () => {
      if (navigator.share) { navigator.share({title: text, url}).catch(() => {}); return; }
      menu.hidden = !menu.hidden;
    });
    document.addEventListener("click", (e) => { if (!box.contains(e.target)) menu.hidden = true; });
  });
})();
// Links that do not exist yet: fill these in when they do.
window.SITE_LINKS = { github: "https://github.com/snrahulsn/siribhoovalaya", youtube: "5zayw_RwuP8", howto: "" };
// Page-visit counter (GoatCounter: no cookies, private dashboard). Not counted on local previews.
if (!/^(localhost|127\.0\.0\.1)$/.test(location.hostname)) {
  const s = document.createElement('script'); s.async = true; s.src = 'https://gc.zgo.at/count.js';
  s.dataset.goatcounter = 'https://siribhoovalaya.goatcounter.com/count'; document.head.appendChild(s);
}
