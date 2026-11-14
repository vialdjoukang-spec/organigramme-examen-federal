import { chromium } from "playwright-core";
import { readFileSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";

const html = resolve(process.argv[2]);
const outDir = resolve(process.argv[3]);
const ids = JSON.parse(readFileSync(process.argv[4], "utf8"));
mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch({
  executablePath: "/usr/bin/google-chrome",
  args: ["--no-sandbox", "--disable-dev-shm-usage"],
});
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const erreurs = [];
page.on("console", (msg) => {
  if (msg.type() === "error") erreurs.push(msg.text());
});
page.on("pageerror", (err) => erreurs.push(String(err)));

await page.goto("file://" + html, { waitUntil: "networkidle" });
await page.click('button[data-o="examens"]');
await page.waitForSelector("#p-examens .rail button");
await page.evaluate(() => {
  const b = [...document.querySelectorAll("#p-examens .rail button")].find((x) => x.querySelector("b")?.textContent.trim() === "2");
  if (!b) throw new Error("onglet imagerie introuvable");
  b.click();
});
let frame = null;
for (let i = 0; i < 40 && !frame; i++) {
  frame = page.frames().find((fr) => fr.url().includes("#o-img"));
  if (!frame) await page.waitForTimeout(200);
}
if (!frame) throw new Error("iframe du recensement introuvable");
await frame.waitForSelector(".dxb");

for (const id of ids) {
  await frame.evaluate((ident) => {
    const tab = document.getElementById(ident.startsWith("EXP-") ? "o-exp" : "o-img");
    if (tab) tab.click();
    const bouton = document.querySelector(`.dxb[data-dx="${ident}"]`);
    if (!bouton) throw new Error("fenêtre absente " + ident);
    bouton.click();
  }, id);
  await frame.waitForSelector(".gm", { timeout: 8000 });
  await frame.waitForTimeout(200);
  await frame.locator("#voile .fen").screenshot({ path: resolve(outDir, `${id}.png`), animations: "disabled", timeout: 20000 });
  if (id === "IMG-158") {
    await frame.evaluate(() => { const b = document.querySelector('[data-act="anat"]'); if (b) b.click(); });
    await frame.waitForTimeout(150);
    await frame.locator("#voile .fen").screenshot({ path: resolve(outDir, "IMG-158-anatomie.png"), animations: "disabled", timeout: 20000 });
  }
  if (id === "IMG-134") {
    await frame.evaluate(() => document.querySelector('[data-act="fleches"]').click());
    await frame.waitForTimeout(150);
    await frame.locator("#voile .fen").screenshot({ path: resolve(outDir, "IMG-134-fleches.png"), animations: "disabled", timeout: 20000 });
    await frame.evaluate(() => document.querySelector('[data-act="code"]').click());
    await frame.waitForTimeout(100);
    await frame.locator(".gm-code").screenshot({ path: resolve(outDir, "IMG-134-couleurs.png"), animations: "disabled", timeout: 20000 });
  }
  await frame.evaluate(() => document.querySelector("#voile .fen > .ferme").click());
  await frame.waitForTimeout(80);
}

await browser.close();
const utiles = erreurs.filter((e) => !/favicon/i.test(e));
if (utiles.length) {
  console.error(JSON.stringify(utiles, null, 2));
  process.exit(1);
}
console.log("captures", ids.length, "sans erreur de console");
