import { chromium } from "playwright-core";
import { writeFileSync } from "node:fs";

const url = process.argv[2];
const dest = process.argv[3];
const selecteur = process.argv[4] || "canvas, img, svg";
const browser = await chromium.launch({
  executablePath: "/usr/bin/google-chrome",
  args: ["--no-sandbox", "--disable-dev-shm-usage"],
});
const page = await browser.newPage({ viewport: { width: 1100, height: 800 } });
await page.goto(url, { waitUntil: "domcontentloaded", timeout: 25000 });
const cible = page.locator(selecteur).first();
await cible.waitFor({ timeout: 8000 });
const png = await cible.screenshot({ timeout: 15000 });
writeFileSync(dest, png);
await browser.close();
