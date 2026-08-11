# AGENTS.md - Deep Study Operating Contract

این فایل قرارداد اجرایی برای ChatGPT، Codex و هر agent دیگری است که روی repository کار می‌کند.

## 1. قبل از هر کار محتوایی

به‌ترتیب بخوان:

1. `PROJECT.md`
2. `STUDY_METHOD.md`
3. `CONTENT_STANDARD.md`
4. `SOURCE_POLICY.md`
5. `RESEARCH_METHOD.md`
6. `MASTERY.md`
7. `meta/prompts/MASTER_PDF_PROMPT.md` برای هر کار PDF
8. syllabus و Scope Contract مربوط به موضوع
9. upstream/downstream documents موجود

## 2. ممنوعیت memory-only

یک Study PDF نهایی را فقط از حافظه‌ی مدل نساز. برای بخش‌های فنی، source set را تعیین و claimهای version-sensitive را verify کن.

## 3. Source of Truth

Markdown/structured source canonical است. PDF artifact از روی آن ساخته می‌شود. اصلاح PDF مستقیم ممنوع مگر برای repair فنی که source آن نیز هم‌زمان اصلاح شود.

## 4. PDF Gate

هیچ PDF با status نهایی منتشر نشود مگر:

- Vazirmatn واقعاً استفاده/embedded شده باشد؛
- PDF preflight پاس شود؛
- PDF به image render شود؛
- **همه صفحات** با vision بررسی شوند؛
- cover، TOC، RTL/LTR، tables، boxes، code، page breaks، borders، footer/page numbers، references و glyphها بررسی شوند؛
- هر defect در source اصلاح و render/inspection تکرار شود.

## 5. Cross-document consistency

قبل از نوشتن سند جدید:

- owner document هر concept را پیدا کن؛
- terminology را یکسان نگه دار؛
- overlap را intentional کن؛
- ID و cross-reference را حفظ کن؛
- نسخه‌ها و research cutoff را sync کن؛
- اگر تغییر upstream downstream را affected می‌کند، impact list ثبت کن.

## 6. Git discipline

- تغییرات ساختاری/محتوایی در branch کار انجام شوند.
- binary generated artifacts کنار canonical source با version matching نگهداری شوند.
- فایل font در repository commit نشود؛ font build dependency باید reproducible/pinned باشد.
- کتاب تجاری commit نشود.

## 7. Stop conditions

اگر یک factual gap با sourceهای available قابل verify نیست، آن را `Unresolved` علامت بزن؛ حدس را به‌عنوان fact وارد سند نکن.
