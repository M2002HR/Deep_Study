# AGENTS.md - Deep Study Operating Contract

این فایل قرارداد اجرایی برای ChatGPT، Codex و هر agent دیگری است که روی repository کار می‌کند.

## 0. بازیابی وضعیت در محیط تازه

اگر context قبلی را نداری، **اول** این دو فایل را بخوان:

1. `START_HERE.md`
2. `CURRENT_STATE.md`

بعد وضعیت واقعی GitHub، branch/PR، `DOCUMENT_REGISTRY.md` و manifestهای جدیدتر را verify کن. اگر state file قدیمی بود، آن را اصلاح کن.

## 1. قبل از هر کار محتوایی

به‌ترتیب بخوان:

1. `PROJECT.md`
2. `STUDY_METHOD.md`
3. `CONTENT_STANDARD.md`
4. `SOURCE_POLICY.md`
5. `RESEARCH_METHOD.md`
6. `MASTERY.md`
7. `meta/standards/MODULE_GRANULARITY.md` برای ساخت/تقسیم Study PDF
8. `meta/prompts/MASTER_PDF_PROMPT.md` و `meta/prompts/PDF_GENERATION.md` برای هر کار PDF
9. syllabus و Scope Contract مربوط به موضوع
10. upstream/downstream documents موجود

برای ادامه مسیر موجود، `meta/CONTINUATION_PROTOCOL.md` را اجرا کن. برای حوزه کاملاً جدید، `meta/prompts/NEW_TOPIC_SYLLABUS.md` را اجرا کن.

## 2. ممنوعیت memory-only

یک Study PDF نهایی را فقط از حافظه‌ی مدل نساز. برای بخش‌های فنی، source set را تعیین و claimهای version-sensitive را verify کن.

## 3. Source of Truth

Markdown/structured source canonical است. PDF artifact از روی آن ساخته می‌شود. اصلاح PDF مستقیم ممنوع مگر برای repair فنی که source آن نیز هم‌زمان اصلاح شود.

## 4. PDF Gate

هیچ PDF با status نهایی منتشر نشود مگر:

- Vazirmatn واقعاً استفاده/embedded شده باشد؛
- PDF preflight پاس شود؛
- فاصله content/page-frame طبق استاندارد فعلی پاس شود؛
- PDF به image render شود؛
- **همه صفحات** با vision بررسی شوند؛
- cover، TOC، RTL/LTR، tables، boxes، code، page breaks، borders، footer/page numbers، references و glyphها بررسی شوند؛
- TOC و صفحه‌های حساس در اندازه کامل spot-check شوند؛
- هر defect در source اصلاح و render/inspection کل سند تکرار شود.

## 5. زبان و اصطلاحات

- فارسی ساده، روشن و طبیعی باشد.
- انگلیسی نباید بی‌دلیل جای جمله فارسی را بگیرد.
- نام product/project، command، API، path، version و اصطلاح فنی جاافتاده می‌تواند Latin بماند.
- برای اصطلاحی که معادل فارسی ساده و طبیعی دارد، اول فارسی و در اولین استفاده انگلیسی داخل پرانتز بیاید.
- `meta/standards/TERMINOLOGY.md` معیار هماهنگی بین سندهاست.

## 6. Cross-document consistency

قبل از نوشتن سند جدید:

- owner document هر concept را پیدا کن؛
- terminology را یکسان نگه دار؛
- overlap را intentional کن؛
- ID و cross-reference را حفظ کن؛
- نسخه‌ها و research cutoff را sync کن؛
- اگر تغییر upstream downstream را affected می‌کند، impact list ثبت کن.

## 7. Publication با Mastery فرق دارد

PDF `canonical/published` فقط یعنی سند آماده مطالعه است. learner را فقط بعد از انجام Lab، teach-back و Mastery Checklist همان module، mastered علامت بزن.

## 8. Git discipline

- تغییرات ساختاری/محتوایی در branch کار انجام شوند.
- binary generated artifacts کنار canonical source با version matching نگهداری شوند.
- فایل font در repository commit نشود؛ font build dependency باید reproducible/pinned باشد.
- کتاب تجاری commit نشود.
- merge فقط با درخواست صریح user انجام شود.

## 9. Stop conditions

اگر یک factual gap با sourceهای available قابل verify نیست، آن را `Unresolved` علامت بزن؛ حدس را به‌عنوان fact وارد سند نکن.
