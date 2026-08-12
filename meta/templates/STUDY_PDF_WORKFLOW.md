# Template - CI برای Study PDF جدید

برای Study PDFهای جدید، workflowهای DKR.01 را کورکورانه copy نکن. آن‌ها artifact تاریخی اولین module هستند.

زیرساخت عمومی پروژه:

- `.github/workflows/reusable-build-study-pdf.yml` برای build candidate؛
- `.github/workflows/reusable-promote-study-pdf.yml` برای promotion exact candidate بعد از Visual QA؛
- `meta/templates/APPROVED_STUDY_CANDIDATE.example.yml` برای approval contract؛
- `scripts/check_published_study_docs.sh` برای validation عمومی همه‌ی Study PDFهای `published-canonical`.

## Build

برای module جدید، caller کوچک module-specific بساز یا reusable workflow را با `workflow_dispatch` اجرا کن. ورودی‌های build:

- path منبع Markdown canonical؛
- path فایل `document.yml`؛
- artifact name یکتا.

نام PDF از `document_id` و `version` داخل manifest به شکل زیر ساخته می‌شود:

`<Document-ID>_v<version>.pdf`

همیشه این gateها را نگه دار:

1. Vazirmatn pinned + fontconfig registration؛
2. build با `scripts/build_study_pdf.py`؛
3. `check_pdf_fonts.sh`؛
4. `check_pdf_clearance.py --min-mm 20 --frame-inset-mm 5 --min-frame-gap-mm 14`؛
5. text extraction و replacement-glyph check؛
6. candidate artifact فقط برای visual QA؛
7. canonical artifact فقط بعد از exact-candidate visual approval.

## Visual approval contract

بعد از render و بررسی **تمام صفحات**، `APPROVED_CANDIDATE.yml` همان module باید حداقل این فیلدها را داشته باشد:

- `run_id`
- `artifact_name`
- `pdf_filename`
- `sha256`
- `page_count`
- `visual_qa: PASS`
- `visual_qa_date`
- `review_basis`

هیچ approvalی فقط با موفقیت build معتبر نیست.

## Promotion

reusable promotion workflow:

- exact artifact همان `run_id` را دانلود می‌کند؛
- exact SHA256 را verify می‌کند؛
- page count را verify می‌کند؛
- font/clearance/text checks را دوباره اجرا می‌کند؛
- فقط همان PDF تأییدشده را زیر `artifacts/` module قرار می‌دهد و روی `main` commit می‌کند.

## Publication synchronization

بعد از promotion نهایی، publication هنوز کامل نیست تا این‌ها sync شوند:

- `DOCUMENT_REGISTRY.md`
- coverage matrix
- progress track
- `CURRENT_STATE.md`
- `artifact-manifest.yml`
- QA report

`Deep Study document contract` سپس همه‌ی registry entryهای `published-canonical` را به‌صورت عمومی validate می‌کند؛ برای هر module جدید validation hard-code جدا نساز مگر contract خاصی واقعاً لازم باشد.
