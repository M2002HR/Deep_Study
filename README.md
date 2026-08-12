# Deep Study

Deep Study یک برنامه‌ی بلندمدت، source-grounded و versioned برای رسیدن از «استفاده از ابزار» به **فهم معماری، internals، debugging، source reading و contribution** در دنیای نرم‌افزار و سیستم‌هاست.

## اصول اصلی

- PDF محیط اصلی مطالعه است؛ Markdown/structured source، **Source of Truth** قابل version-control است.
- هیچ PDF درسی بدون Scope Contract، منابع canonical، research cutoff، citations، labs، failure scenarios و Definition of Done ساخته نمی‌شود.
- کیفیت سند فقط با تولید PDF تمام نمی‌شود: PDF باید به تصویر render شود و **همه‌ی صفحات** به‌صورت بصری بررسی شوند؛ ایرادها باید در source اصلاح و چرخه تا قبولی کامل تکرار شود.
- فونت canonical اسناد فارسی پروژه **Vazirmatn** است.
- authoring، publication، prerequisite readiness و learner mastery stateهای جدا هستند؛ مرجع: `meta/standards/PROGRESSION_AND_PREREQUISITES.md`.
- اولین curriculum عمیق پروژه: **DevOps -> Docker Mastery**.

## از کجا شروع کنم؟

1. `START_HERE.md`
2. `CURRENT_STATE.md`
3. `PROJECT.md`
4. `STUDY_METHOD.md`
5. `AGENTS.md`
6. `meta/prompts/MASTER_PDF_PROMPT.md`
7. `curriculum/devops/docker/docker_mastery_syllabus_v1.1.0.md`

> کتاب‌های تجاری در repository کپی نمی‌شوند مگر license آن‌ها صریحاً اجازه دهد. `library/` فقط catalog، metadata و منابع قانونی را نگه می‌دارد.

## Canonical registry and artifacts

- Document registry: `DOCUMENT_REGISTRY.md`
- Docker curriculum: `curriculum/devops/docker/`
- Canonical syllabus source: `curriculum/devops/docker/docker_mastery_syllabus_v1.1.0.md`
- Canonical syllabus PDF: `curriculum/devops/docker/artifacts/docker_mastery_syllabus_v1.1.0.pdf`
- Syllabus QA evidence: `curriculum/devops/docker/QA_REPORT_v1.1.0.md`
- Syllabus artifact manifest: `curriculum/devops/docker/artifact-manifest.yml`
- First canonical Study source: `subjects/docker/DKR.01/DKR.01.md`
- First canonical Study PDF: `subjects/docker/DKR.01/artifacts/DS-DKR-01_v1.0.0.pdf`
- DKR.01 QA: `subjects/docker/DKR.01/QA_REPORT_v1.0.0.md`
- Docker track progress / next authoring target: `curriculum/devops/docker/PROGRESS.md`

## Study PDF infrastructure

- Generic builder: `scripts/build_study_pdf.py`
- Reusable candidate workflow: `.github/workflows/reusable-build-study-pdf.yml`
- Reusable promotion workflow: `.github/workflows/reusable-promote-study-pdf.yml`
- Generic published-document validation: `scripts/check_published_study_docs.sh`
- Workflow template/contract: `meta/templates/STUDY_PDF_WORKFLOW.md`

در وضعیت فعلی، `DKR.01` published-canonical است و `DKR.02` next eligible authoring target است؛ learner mastery `DKR.01` جداگانه track می‌شود.
