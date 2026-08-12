# AGENTS.md - Deep Study Operating Contract

این فایل قرارداد اجرایی برای ChatGPT، Codex و هر agent دیگری است که روی repository کار می‌کند.

## 0. بازیابی وضعیت در محیط تازه

اگر context قبلی را نداری، **اول** این دو فایل را بخوان:

1. `START_HERE.md`
2. `CURRENT_STATE.md`

بعد وضعیت واقعی GitHub، branch پیش‌فرض، آخرین commit، `DOCUMENT_REGISTRY.md` و manifestهای جدیدتر را verify کن. اگر state file قدیمی بود، آن را اصلاح کن.

branch اصلی پروژه `main` است. روش Git پروژه در `meta/standards/GIT_WORKFLOW.md` تعریف شده و برای همه agentها اجباری است.

## 1. قبل از هر کار محتوایی

به‌ترتیب بخوان:

1. `PROJECT.md`
2. `STUDY_METHOD.md`
3. `CONTENT_STANDARD.md`
4. `SOURCE_POLICY.md`
5. `RESEARCH_METHOD.md`
6. `MASTERY.md`
7. `meta/standards/GIT_WORKFLOW.md`
8. `meta/standards/PROGRESSION_AND_PREREQUISITES.md`
9. `meta/standards/MODULE_GRANULARITY.md` برای ساخت/تقسیم Study PDF
10. `meta/prompts/MASTER_PDF_PROMPT.md` و `meta/prompts/PDF_GENERATION.md` برای هر کار PDF
11. syllabus و Scope Contract مربوط به موضوع
12. upstream/downstream documents موجود

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

## 7. Publication، prerequisite readiness و Mastery سه چیز متفاوت‌اند

PDF `canonical/published` فقط یعنی سند آماده مطالعه است. learner را فقط بعد از انجام Lab، teach-back و Mastery Checklist همان module، mastered علامت بزن.

علاوه بر این، operational/environment prerequisiteها ممکن است readiness evidence جدا داشته باشند. publication یک PDF downstream، readiness محیط یا mastery learner را اثبات نمی‌کند.

وقتی user می‌گوید «PDF بعدی را بساز»، agent باید **authoring eligibility** را از dependency graph بررسی کند؛ pending بودن learner mastery به‌خودی‌خود authoring را block نمی‌کند. وقتی user می‌گوید «درس بعدی را شروع کنم»، mastery prerequisite و readiness عملی باید جدا بررسی شوند.

مرجع کامل: `meta/standards/PROGRESSION_AND_PREREQUISITES.md`.

## 8. Git discipline

- **حالت پیش‌فرض: تغییر مستقیم روی آخرین نسخه `main`.**
- به‌صورت پیش‌فرض branch جدا یا Pull Request نساز.
- branch/PR فقط وقتی ساخته شود که user در همان درخواست صریحاً بخواهد.
- اگر direct write روی `main` به دلیل protection/permission ممکن نبود، خطا را گزارش کن و خودکار branch/PR نساز.
- قبل از write آخرین نسخه و SHA فایل را از `main` بخوان تا تغییر جدیدی overwrite نشود.
- binary generated artifacts کنار canonical source با version matching نگهداری شوند.
- فایل font در repository commit نشود؛ font build dependency باید reproducible/pinned باشد.
- کتاب تجاری commit نشود.
- force push و rewrite تاریخچه `main` پیش‌فرض ممنوع است.

جزئیات کامل در `meta/standards/GIT_WORKFLOW.md` است.

## 9. Publication synchronization

بعد از publication هر Study PDF، حداقل این‌ها باید با هم sync شوند:

- `DOCUMENT_REGISTRY.md`
- coverage matrix همان track
- progress همان track
- `CURRENT_STATE.md`
- document/artifact manifest
- QA report

CI باید همه‌ی `published-canonical` Study PDFها را از registry/manifest validate کند؛ contract نباید فقط نام آخرین module را hard-code کند.

## 10. Stop conditions

اگر یک factual gap با sourceهای available قابل verify نیست، آن را `Unresolved` علامت بزن؛ حدس را به‌عنوان fact وارد سند نکن.
