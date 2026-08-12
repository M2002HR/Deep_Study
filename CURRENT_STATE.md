# وضعیت فعلی Deep Study

**آخرین به‌روزرسانی:** 2026-08-12

## مسیر فعال

`DevOps -> Docker`

## سند مادر

- `DS-DKR-SYL` - Docker Mastery Syllabus v1.1.0
- Source: `curriculum/devops/docker/docker_mastery_syllabus_v1.1.0.md`
- PDF: `curriculum/devops/docker/artifacts/docker_mastery_syllabus_v1.1.0.pdf`

## اسناد درسی canonical

### DKR.01

- Curriculum ID: `DKR.01`
- Document ID: `DS-DKR-01`
- عنوان: `تاریخچه و مدل ذهنی کانتینر`
- نسخه: `1.0.0`
- وضعیت سند: `published-canonical`
- وضعیت learner: `not assessed`
- Source: `subjects/docker/DKR.01/DKR.01.md`
- Artifact manifest: `subjects/docker/DKR.01/artifact-manifest.yml`
- QA report: `subjects/docker/DKR.01/QA_REPORT_v1.0.0.md`
- PDF: `subjects/docker/DKR.01/artifacts/DS-DKR-01_v1.0.0.pdf`
- PDF SHA256: `080aa14cfdc53cc08ccef66643b2bf9d798dfa6a384a6eaaa10423a1308c7b40`
- اندازه: 37 صفحه A4؛ حدود 3 تا 6 ساعت مطالعه فعال.

### DKR.02 - آخرین PDF منتشرشده

- Curriculum ID: `DKR.02`
- Document ID: `DS-DKR-02`
- عنوان: `نصب، Editions، Platforms و Distribution`
- نسخه: `1.0.0`
- وضعیت سند: `published-canonical`
- وضعیت learner: `not-started`
- Research cutoff: `2026-08-12`
- Source: `subjects/docker/DKR.02/DKR.02.md`
- Metadata: `subjects/docker/DKR.02/document.yml`
- Sources: `subjects/docker/DKR.02/SOURCES.md`
- Research log: `subjects/docker/DKR.02/RESEARCH_LOG_v1.0.0.md`
- Artifact manifest: `subjects/docker/DKR.02/artifact-manifest.yml`
- QA report: `subjects/docker/DKR.02/QA_REPORT_v1.0.0.md`
- Approval: `subjects/docker/DKR.02/APPROVED_CANDIDATE.yml`
- PDF: `subjects/docker/DKR.02/artifacts/DS-DKR-02_v1.0.0.pdf`
- PDF SHA256: `109e9d47c69cdecc33ab5e70be8e13baf7a224edc8a172b88fe33a69cadb0ab6`
- اندازه: 42 صفحه A4؛ حدود 4 تا 7 ساعت مطالعه فعال همراه با Lab و assessment.
- Visual QA: PASS؛ 42/42 صفحه در 180 DPI بررسی شده‌اند.
- فونت نهایی: فقط Vazirmatn Regular/Medium/Bold، embedded.

## مسیر learner با مسیر authoring فرق دارد

قانون کامل: `meta/standards/PROGRESSION_AND_PREREQUISITES.md`.

### مسیر learner

انتشار `DKR.02` به معنی mastered شدن `DKR.01` نیست. وضعیت learner برای `DKR.01` همچنان **not assessed** است.

برای شروع رسمی مطالعه `DKR.02`:

1. Mastery Gate `DKR.01` با evidence واقعی پاس شود.
2. readiness عملی `META.DKR.02` برای Lab ثبت شود؛ وضعیت فعلی آن `pending` است.
3. سپس DKR.02 مطالعه، Lab، failure drills، interview، teach-back و Mastery Checklist انجام شود.

### مسیر authoring / آماده‌سازی محتوا

`DKR.02` کامل و canonical شده است. **Next authoring target** اکنون:

`DKR.03 - معماری Docker Engine: CLI -> API -> dockerd -> runtime stack`

- Document ID برنامه‌ریزی‌شده: `DS-DKR-03`
- Authoring state: `eligible / next-to-author`
- Publication state: `planned`
- prerequisiteهای محتوایی `DKR.01` و `DKR.02` هر دو canonical موجودند.
- قبل از authoring باید continuation protocol، granularity gate و research/currentness gate دوباره اجرا شوند.

## وضعیت Git

- Repository: `M2002HR/Deep_Study`
- branch پیش‌فرض و canonical: `main`
- روش پیش‌فرض تغییرات: **نوشتن مستقیم روی `main`، بدون ساخت branch جدا و بدون Pull Request.**
- branch/PR فقط با درخواست صریح user ساخته می‌شود.
- policy کامل: `meta/standards/GIT_WORKFLOW.md`

## قرارداد publication عمومی

- published Study PDFها باید در `DOCUMENT_REGISTRY.md` ثبت شوند.
- coverage matrix، progress، state، manifest و QA بعد از publication باید sync شوند.
- CI از `scripts/check_published_study_docs.sh` استفاده می‌کند تا همه‌ی `published-canonical` Study PDFها را از روی registry/manifest validate کند؛ contract فقط به یک module محدود نیست.
- PDF بدون Visual QA کامل canonical نمی‌شود.

## برای ادامه در یک چت تازه

1. از `START_HERE.md` شروع کن.
2. وضعیت واقعی GitHub، `main`، registry و آخرین artifact manifest/QA را verify کن.
3. `meta/standards/PROGRESSION_AND_PREREQUISITES.md` را بخوان و authoring eligibility را با learner mastery قاطی نکن.
4. اگر هدف ادامه مطالعه learner است، mastery prerequisiteها و readiness عملی را بررسی کن.
5. اگر هدف ساخت سند بعدی است، syllabus/dependencyها را verify و `meta/prompts/CONTINUE_EXISTING_TRACK.md` را اجرا کن؛ next authoring target فعلی `DKR.03` است.
6. تغییرات عادی را مستقیم روی `main` ثبت کن؛ branch/PR نساز مگر user صریحاً بخواهد.
7. بعد از هر publication یا تغییر mastery/readiness، این فایل را به‌روزرسانی کن.
