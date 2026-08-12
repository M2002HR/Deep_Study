# Continuation Protocol

این قرارداد برای زمانی است که پروژه در یک ChatGPT/Codex/agent یا چت کاملاً تازه ادامه پیدا می‌کند.

## 1. State recovery

قبل از هر تصمیم:

- `START_HERE.md` و `CURRENT_STATE.md` را بخوان؛
- وضعیت واقعی GitHub، branch پیش‌فرض `main` و آخرین commit را بررسی کن؛
- `meta/standards/GIT_WORKFLOW.md` را بخوان؛
- `DOCUMENT_REGISTRY.md` را بخوان؛
- syllabus مسیر فعال و آخرین artifact manifest/QA report را بخوان؛
- اگر `CURRENT_STATE.md` با GitHub اختلاف داشت، GitHub و manifestهای جدیدتر را مبنا بگیر و state file را اصلاح کن.

## 2. انتخاب قدم بعدی

قدم بعدی را از syllabus انتخاب کن، نه از حافظه مدل. برای همان ID:

- owner scope؛
- prerequisiteها؛
- upstream/downstream؛
- Depth؛
- labs/failures؛
- canonical source list؛
- Definition of Done

را استخراج کن.

## 3. Granularity gate

قبل از تحقیق، `meta/standards/MODULE_GRANULARITY.md` را اجرا کن. اگر syllabus item برای یک Study PDF بیش از حد بزرگ یا کوچک است، آن را به subdocumentهای دارای ID پایدار تقسیم یا با بخش هم‌مالک ادغام کن؛ syllabus/coverage باید این تصمیم را ثبت کند.

## 4. Research gate

- منابع فعلی و رسمی را دوباره verify کن.
- claimهای current/version-sensitive را در همان روز ساخت سند بررسی کن.
- spec/docs/source/book roles را جدا نگه دار.
- unresolvedها را پنهان نکن.

## 5. Authoring gate

- `MASTER_PDF_PROMPT.md` + `PDF_GENERATION.md` + `CONTENT_STANDARD.md` را اجرا کن.
- متن فارسی ساده باشد.
- اصطلاحات repo را از `TERMINOLOGY.md` رعایت کن.
- overlap با owner documentهای قبلی intentional و کوتاه باشد.

## 6. Build and QA

- Markdown canonical را بساز.
- PDF candidate را از source تولید کن.
- font/clearance/integrity checks را اجرا کن.
- همه صفحه‌ها را 180 تا 220 DPI render کن.
- همه صفحه‌ها را ببین؛ TOC/table/code/lab/referenceها را جداگانه full-size بررسی کن.
- defect را در source اصلاح کن و کل QA را تکرار کن.

## 7. Publication gate

در publication:

- `DOCUMENT_REGISTRY.md` را به‌روزرسانی کن؛
- artifact manifest و QA report ثبت کن؛
- `CURRENT_STATE.md` و progress مسیر را به‌روزرسانی کن؛
- PDF artifact و source دقیقاً version-matched باشند؛
- publication status را با learner mastery قاطی نکن.

### روش Git در publication

- پیش‌فرض: همه تغییرات تأییدشده را مستقیم روی آخرین `main` ثبت کن.
- branch جدا و Pull Request نساز مگر user صریحاً درخواست کند.
- اگر GitHub direct write روی `main` را نپذیرفت، توقف کن و خطا را گزارش بده؛ خودکار مسیر PR را جایگزین نکن.

## 8. Handoff

در پایان هر کار، repository باید آن‌قدر state داشته باشد که agent بعدی بدون context چت بتواند بگوید:

- چه چیزهایی canonical هستند؟
- چه چیزی فقط draft/candidate است؟
- آخرین درس منتشرشده چیست؟
- learner از کجا باید شروع/ادامه دهد؟
- درس بعدی چیست؟
- چه source baseline و QA contractی باید حفظ شود؟
- تغییر بعدی باید روی کدام branch ثبت شود؟ پاسخ پیش‌فرض: `main`.
