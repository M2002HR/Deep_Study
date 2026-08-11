# گزارش بررسی PDF - DS-DKR-01 / v1.0.0

## نتیجه

**PASS**

این گزارش برای همان PDF ساخته‌شده در GitHub Actions با Run ID `31470101597` است. موفق‌شدن build به‌تنهایی کافی نبود؛ خود candidate رسمی دوباره دانلود، اندازه‌گیری، render و کامل بررسی شد.

## مشخصات artifact

- Document ID: `DS-DKR-01`
- Curriculum ID: `DKR.01`
- عنوان: `تاریخچه و مدل ذهنی کانتینر`
- نسخه: `1.0.0`
- Research cutoff: `2026-08-11`
- تعداد صفحه: `37`
- اندازه صفحه: A4
- SHA256 خود PDF: `080aa14cfdc53cc08ccef66643b2bf9d798dfa6a384a6eaaa10423a1308c7b40`
- GitHub Actions Run: `31470101597`
- Artifact: `dkr01-study-pdf-candidate`
- SHA256 بسته artifact: `2d9c7c9cd4e632bcf7d2e405da24900a19dffa55055badf8303581b1088102c6`

## بررسی فنی

- PDF سالم و قابل بازشدن است.
- متن قابل جست‌وجو است و سند اسکن‌شده نیست.
- PDF رمزگذاری نشده است.
- فقط `Vazirmatn`، `Vazirmatn-Medium` و `Vazirmatn-Bold` استفاده شده‌اند و هر سه داخل PDF embedded هستند.
- کاراکتر خراب `U+FFFD` در متن استخراج‌شده پیدا نشد.
- کادر صفحه مستقل از ناحیه متن است و حدود 5mm از لبه کاغذ قرار دارد.

### فاصله واقعی محتوای اصلی از لبه کاغذ

- چپ: `22.00mm`
- راست: `21.94mm`
- بالا: `21.13mm`
- پایین: `24.98mm`

همه سمت‌ها از حداقل `20mm` بیشتر هستند.

### فاصله واقعی محتوای اصلی از کادر

- چپ: `17.00mm`
- راست: `16.94mm`
- بالا: `16.13mm`
- پایین: `19.98mm`

همه سمت‌ها از حداقل `14mm` بیشتر هستند.

## بررسی دیداری

همه `37` صفحه‌ی **همان candidate رسمی GitHub** با `180 DPI` render شدند و صفحه‌به‌صفحه دیده شدند. هیچ صفحه‌ای نمونه‌گیری نشد؛ همه صفحه‌ها بررسی شدند.

موارد زیر در تمام سند بررسی شدند:

- کادر و فاصله آن از متن؛
- RTL فارسی و ترکیب فارسی/انگلیسی؛
- فونت و وزن‌ها؛
- headingها و شکست صفحه؛
- جدول‌ها و باکس‌ها؛
- code blockها و commandها؛
- شماره صفحه و footer؛
- clipping، overlap و glyph خراب؛
- تراکم صفحه و فضای سفید؛
- خوانایی متن در صفحات پرمحتوا.

این صفحات جداگانه در اندازه کامل هم بررسی شدند:

- صفحه 2: فهرست مطالب؛
- صفحه 14: جدول مقایسه Process / Application Container / System Container / VM؛
- صفحه 24: شروع Lab و code blockها؛
- صفحه 34: شروع منابع و URLها؛
- صفحه 37: پایان منابع و Changelog.

## ریزدانگی درس

این سند 37 صفحه است و برای حدود 3 تا 6 ساعت مطالعه فعال طراحی شده. یک outcome اصلی دارد: ساخت مدل ذهنی درست از container و مرز آن با process، VM، system container و ecosystem. جزئیات namespace، cgroup و runtime internals عمداً به owner documentهای بعدی سپرده شده‌اند.

## وضعیت انتشار و یادگیری

- وضعیت سند: `published/canonical` بعد از promotion همین candidate.
- وضعیت learner: `not assessed`.

**Published ≠ Mastered.** learner فقط بعد از مطالعه، انجام Lab، teach-back و Mastery Checklist می‌تواند این درس را mastered علامت بزند.
