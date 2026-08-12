# وضعیت فعلی Deep Study

**آخرین به‌روزرسانی:** 2026-08-12

## مسیر فعال

`DevOps -> Docker`

## سند مادر

- `DS-DKR-SYL` - Docker Mastery Syllabus v1.1.0
- Source: `curriculum/devops/docker/docker_mastery_syllabus_v1.1.0.md`
- PDF: `curriculum/devops/docker/artifacts/docker_mastery_syllabus_v1.1.0.pdf`

## اولین درس رسمی - آماده مطالعه

- Curriculum ID: `DKR.01`
- Document ID: `DS-DKR-01`
- عنوان: `تاریخچه و مدل ذهنی کانتینر`
- نسخه: `1.0.0`
- وضعیت سند: `published-canonical`
- وضعیت learner: `not assessed`
- Source: `subjects/docker/DKR.01/DKR.01.md`
- Manifest: `subjects/docker/DKR.01/document.yml`
- Artifact manifest: `subjects/docker/DKR.01/artifact-manifest.yml`
- QA report: `subjects/docker/DKR.01/QA_REPORT_v1.0.0.md`
- PDF: `subjects/docker/DKR.01/artifacts/DS-DKR-01_v1.0.0.pdf`
- PDF SHA256: `080aa14cfdc53cc08ccef66643b2bf9d798dfa6a384a6eaaa10423a1308c7b40`
- اندازه: 37 صفحه A4؛ حدود 3 تا 6 ساعت مطالعه فعال همراه با Lab و assessment.

## دو مسیر state که نباید قاطی شوند

قانون کامل: `meta/standards/PROGRESSION_AND_PREREQUISITES.md`.

### مسیر learner

1. `DKR.01` را مطالعه کند.
2. predictionهای Lab را قبل از مشاهده نتیجه ثبت کند.
3. Lab process/namespace را انجام دهد.
4. challenge/interview/teach-back را انجام دهد.
5. Mastery Checklist را با evidence واقعی پاس کند.
6. بعد از Mastery Gate، مطالعه رسمی `DKR.02` مجاز می‌شود.

وضعیت فعلی learner برای `DKR.01`: **not assessed**.

### مسیر authoring / آماده‌سازی محتوا

PDF downstream می‌تواند قبل از mastery learner آماده شود؛ publication سند downstream به معنی عبور learner از prerequisite نیست.

**Next authoring target:**

`DKR.02 - نصب، Editions، Platforms و Distribution`

- Document ID برنامه‌ریزی‌شده: `DS-DKR-02`
- Authoring state: `eligible / next-to-author`
- Publication state: `planned`
- Upstream canonical document: `DKR.01` موجود و published-canonical
- Operational prerequisite: `META.DKR.02`
- readiness evidence برای `META.DKR.02`: هنوز ثبت نشده و قبل از اجرای Lab عملی DKR.02 باید ثبت شود.

بنابراین ساخت کامل PDF `DKR.02` از نظر authoring مجاز و قدم بعدی پروژه است؛ اما شروع مطالعه رسمی آن توسط learner همچنان به Mastery Gate `DKR.01` و readiness عملی لازم وابسته است.

## وضعیت Git

- Repository: `M2002HR/Deep_Study`
- branch پیش‌فرض و canonical: `main`
- PR باز: ندارد؛ وضعیت واقعی در 2026-08-12 بررسی شد.
- روش پیش‌فرض تغییرات: **نوشتن مستقیم روی `main`، بدون ساخت branch جدا و بدون Pull Request.**
- branch/PR فقط با درخواست صریح user ساخته می‌شود.
- policy کامل: `meta/standards/GIT_WORKFLOW.md`

## قرارداد publication عمومی

- published Study PDFها باید در `DOCUMENT_REGISTRY.md` ثبت شوند.
- coverage matrix، progress، state، manifest و QA بعد از publication باید sync شوند.
- CI از `scripts/check_published_study_docs.sh` استفاده می‌کند تا همه‌ی `published-canonical` Study PDFها را از روی registry/manifest validate کند؛ contract فقط به DKR.01 محدود نیست.

## برای ادامه در یک چت تازه

1. از `START_HERE.md` شروع کن.
2. وضعیت واقعی GitHub، `main`، registry و آخرین artifact manifest را verify کن.
3. `meta/standards/PROGRESSION_AND_PREREQUISITES.md` را بخوان و authoring eligibility را با learner mastery قاطی نکن.
4. اگر هدف ادامه مطالعه learner است، mastery prerequisiteها و readiness عملی را بررسی کن.
5. اگر user می‌خواهد سند بعدی را آماده کند، syllabus و dependencyها را بخوان و `meta/prompts/CONTINUE_EXISTING_TRACK.md` را اجرا کن؛ next authoring target فعلی `DKR.02` است.
6. اگر موضوع جدیدی شروع می‌شود، `meta/prompts/NEW_TOPIC_SYLLABUS.md` را اجرا کن.
7. تغییرات عادی را مستقیم روی `main` ثبت کن؛ branch/PR نساز مگر user صریحاً بخواهد.
8. بعد از هر publication یا تغییر mastery/readiness، این فایل را به‌روزرسانی کن.
