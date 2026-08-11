# Prompt - Full Visual QA

PDF candidate را صفحه‌به‌صفحه render کن و **تمام صفحات** را inspect کن.

برای هر صفحه بررسی کن:
- clipping/overlap/glyph corruption;
- Vazirmatn consistency;
- RTL/LTR ordering and punctuation;
- border/margins/footer/page number;
- heading orphan/widow;
- tables/boxes/code blocks;
- blank/underfilled page anomalies;
- citations/URLs;
- TOC alignment and page numbers.

خروجی: `PASS` فقط اگر defect واضح صفر باشد؛ در غیر این صورت defect list شامل page number + exact fix. پس از fix، full review از اول تکرار شود.
