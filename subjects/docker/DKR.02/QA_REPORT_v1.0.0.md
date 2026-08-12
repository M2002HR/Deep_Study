# گزارش بررسی PDF - DS-DKR-02 / v1.0.0

## نتیجه

**PASS**

این گزارش برای همان PDF نهایی‌ای است که از candidate رسمی GitHub Actions با Run ID `31617684197` تأیید و promote شده است. موفق‌شدن build به‌تنهایی کافی نبود؛ candidate دقیق دانلود، preflight، render و صفحه‌به‌صفحه بررسی شد. candidate اولیه به دلیل سه defect دیداری/فونت رد شد و فقط نسخه refined پس از rebuild کامل پذیرفته شد.

## مشخصات artifact

- Document ID: `DS-DKR-02`
- Curriculum ID: `DKR.02`
- عنوان: `نصب، Editions، Platforms و Distribution`
- نسخه: `1.0.0`
- Research cutoff: `2026-08-12`
- تعداد صفحه: `42`
- اندازه صفحه: A4
- SHA256 source نهایی: `7bde2f120b8f36f4ffbf8a1f1613e1a97300eea94bf419baf5273054938a94f5`
- SHA256 خود PDF: `109e9d47c69cdecc33ab5e70be8e13baf7a224edc8a172b88fe33a69cadb0ab6`
- GitHub Actions Run: `31617684197`
- Artifact: `dkr02-study-pdf-candidate`
- SHA256 بسته artifact: `baeca59735bc2a7c18a5325772eff5fc8fcf161f8ad25cd7e438b4ac76c86492`

## بررسی پژوهش و Scope

Scope مستقیماً از syllabus `DKR.02` استخراج شد و با upstream `DKR.01` و downstream `DKR.03` consistency-audit شد. ادعاهای version-sensitive در روز `2026-08-12` از مستندات رسمی Docker دوباره verify شدند. موضوع‌های owned توسط `DKR.03`، `DKR.30`، `DKR.31`، `DKR.34` و platform modules عمداً فقط تا boundary لازم معرفی شده‌اند تا duplication و granularity drift رخ ندهد.

سند شامل install/deployment model، Engine/Desktop/CLI boundaries، package-managed و static installation، rootful/rootless deployment shape، Linux/macOS/Windows differences، Docker contexts و endpoint selection، API/client-daemon compatibility، component/version inventory، secure remote access، failure/debugging playbook، Linux/remote-context labs، optional rootless lab، evidence table، misconception/challenge/interview/teach-back و Mastery Checklist است.

## بررسی فنی نهایی

- PDF سالم، قابل بازشدن، searchable و غیررمزشده است.
- page count دقیقاً `42` و page size برابر A4 است.
- `U+FFFD` در متن استخراج‌شده وجود ندارد.
- فقط `Vazirmatn`، `Vazirmatn-Medium` و `Vazirmatn-Bold` در candidate نهایی استفاده شده‌اند و هر سه embedded هستند.
- fallback قبلی `DejaVu Sans` و وزن oblique پس از اصلاح source حذف شد.
- footer و شماره صفحه‌های خودکار با ارقام فارسی render می‌شوند؛ Document ID، version، command و identifierهای فنی عمداً Latin باقی مانده‌اند.
- جدول‌ها مطابق checklist اصلی وسط‌چین و از نظر عمودی متوازن شدند.
- کادر تزئینی مستقل از ناحیه متن و حدود `5mm` از لبه کاغذ است.

### فاصله واقعی محتوای اصلی از لبه کاغذ

- چپ: `22.00mm`
- راست: `21.94mm`
- بالا: `22.39mm`
- پایین: `24.45mm`

همه سمت‌ها از حداقل `20mm` بیشتر هستند.

### فاصله واقعی محتوای اصلی از کادر

- چپ: `17.00mm`
- راست: `16.94mm`
- بالا: `17.39mm`
- پایین: `19.45mm`

همه سمت‌ها از حداقل `14mm` بیشتر هستند.

## چرخه Visual QA

### Candidate اول - رد شد

candidate اولیه 42 صفحه بود و mechanical checks را پاس کرده بود، اما full-page visual QA سه defect آشکار کرد:

1. شماره‌های خودکار footer و TOC به شکل Latin render می‌شدند؛
2. subtitle ترکیبی فارسی/انگلیسی روی cover از نظر bidi ترتیب مطلوب نداشت؛
3. دو glyph دیاگرام و italic markup باعث font fallback به `DejaVu Sans`/وزن oblique شده بود.

طبق `MASTER_PDF_PROMPT.md` این candidate canonical نشد. defectها در source/CSS اصلاح، PDF از صفر rebuild و کل Visual QA تکرار شد.

### Candidate refined - PASS

همه `42` صفحه‌ی **همان candidate refined رسمی GitHub** با `180 DPI` render و بدون sampling بررسی شدند.

موارد زیر در کل سند کنترل شدند:

- cover و bidi؛
- TOC واقعی RTL، نقطه‌چین‌ها و اعداد فارسی؛
- Vazirmatn و نبود fallback؛
- headings و orphanها؛
- paragraph flow و فضای سفید؛
- tableها و center/middle alignment؛
- boxها و شکست صفحه؛
- code blockها، URLها، commandها و LTR isolation؛
- کادر و فاصله متن از آن؛
- footer و page number؛
- clipping، overlap، glyph خراب یا blank page غیرعادی؛
- references و long URLs.

این صفحات جداگانه در اندازه کامل نیز بررسی شدند:

- صفحه 1: cover؛
- صفحه 2: فهرست مطالب؛
- صفحه 11: جدول مقایسه؛
- صفحه 29: Lab/remote-context topology و code blocks؛
- صفحه 32: evidence table؛
- صفحه 41: references و URLهای بلند؛
- صفحه 42: پایان سند و changelog.

هیچ defect واضح باقی‌مانده‌ای که publication را block کند مشاهده نشد.

## ریزدانگی و زمان مطالعه

این سند 42 صفحه است و برای حدود **4 تا 7 ساعت مطالعه فعال** همراه با prediction، Lab، failure drills، interview و teach-back طراحی شده است. mastery milestone آن مشخص است: learner باید بتواند deployment مناسب را انتخاب/نصب کند، component/version provenance را inventory کند، بفهمد CLI به کدام daemon/context متصل است و failureهای نصب، permission، context، API و remote-access را evidence-driven debug کند.

## وضعیت publication و learner

- وضعیت سند: `published-canonical`.
- وضعیت learner برای `DKR.02`: `not-started`.
- readiness عملی `META.DKR.02`: هنوز `pending` و باید قبل از Lab واقعی evidence ثبت شود.
- mastery `DKR.01` با انتشار این سند تغییر نمی‌کند.

**Published ≠ Mastered.** آماده‌شدن DKR.02 مسیر مطالعه را دور نمی‌زند؛ learner progression همچنان باید gateهای prerequisite را با evidence پاس کند.
