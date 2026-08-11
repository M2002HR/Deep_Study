# Research Method

## مرحله ۱ - Scope inventory

قبل از طراحی ترتیب مطالعه، union موضوعات را بساز:

- documentation navigation tree
- کتاب‌های منتخب و TOC آن‌ها
- specification TOC
- CLI/API/config/file-format reference indexes
- major source-tree subsystems
- release/deprecation surface

هیچ topic فقط به این دلیل که در یک منبع نیامده حذف نمی‌شود.

## مرحله ۲ - Normalize

- synonymها را merge کن، ولی provenance را نگه دار.
- deprecated/legacy/current را برچسب بزن.
- product-specific و fundamental را جدا کن.
- topic را به foundational / user / production / internals / implementation / contributor طبقه‌بندی کن.

## مرحله ۳ - Dependency DAG

برای هر node prerequisites مفهومی را استخراج کن. dependency روی **concept** باشد، نه صرفاً brand/tool.

## مرحله ۴ - Coverage Audit

برای هر topic این ستون‌ها حداقل ثبت شوند:

`ID | topic | owner doc | book | docs | spec | source | lab | failure | interview | status`

## مرحله ۵ - Study order

از DAG یک spiral order بساز؛ prerequisiteها را فقط به اندازه‌ی gate موردنیاز جلو بیاور.

## مرحله ۶ - Module research

برای یک module:

1. research questionها را بنویس؛
2. source baseline را pin کن؛
3. docs/spec/source را بخوان؛
4. claims و evidence را ثبت کن؛
5. unresolved questions را جدا نگه دار؛
6. labs و failure scenarios را طراحی کن؛
7. module source را بنویس؛
8. source-verification pass؛
9. consistency pass با upstream/downstream؛
10. PDF generation + visual QA.

## مرحله ۷ - Update protocol

release/change monitor -> impact classification -> affected IDs -> source update -> regression research -> PDF rebuild -> visual QA -> changelog.
