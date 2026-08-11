# Prompt - ساخت syllabus برای یک موضوع جدید

وقتی کاربر یک حوزه جدید مثل Networking، PostgreSQL، Kubernetes، Git یا Operating Systems را شروع می‌کند، قبل از ساخت اولین درس این روند را اجرا کن.

## A. هدف را تعریف کن

- سطح نهایی موردنظر user را مشخص کن: usage / production / troubleshooting / internals / implementation / contribution.
- مرز موضوع و ارتباطش با trackهای دیگر را روشن کن.
- «کامل بودن» را به coverage قابل audit تبدیل کن، نه ادعای مبهم.

## B. Source inventory بساز

حداقل این سطح‌ها را بررسی کن:

1. navigation کامل official docs؛
2. reference indexهای CLI/API/config/file format؛
3. specification/standard TOC اگر وجود دارد؛
4. release/deprecation/security surface؛
5. source tree و subsystemهای مهم؛
6. TOC چند کتاب قوی برای ترتیب آموزشی و gap detection؛
7. papers/design docs/maintainer docs در صورت relevance.

برای اطلاعات current، خود canonical page را باز و verify کن؛ search snippet کافی نیست.

## C. Union و gap analysis

- همه topicها را union کن.
- synonymها را normalize کن ولی provenance را نگه دار.
- current/legacy/deprecated/experimental را جدا کن.
- هر topic را foundational/user/production/internals/implementation/contributor طبقه‌بندی کن.
- اگر topic در source tree/spec/reference هست ولی در کتاب نیست، آن را gap احتمالی بدان و بررسی کن.

## D. Dependency DAG

Dependency را بر concept بنا کن، نه برند. بعد از DAG، spiral study order بساز؛ prerequisite paralysis ایجاد نکن.

## E. ID و ownership

- IDهای پایدار تعریف کن.
- برای هر concept یک owner module مشخص کن.
- overlap بین سندها فقط summary + cross-reference باشد.

## F. Granularity

برای هر node `MODULE_GRANULARITY.md` را اجرا کن. هر PDF باید یک mastery milestone مشخص داشته باشد.

## G. هر module چه اطلاعاتی داشته باشد؟

- ID / title / depth / prerequisites
- In Scope / Out of Scope
- mandatory coverage
- labs/experiments
- failure scenarios/debugging
- source/spec/source-code reading
- interview objectives
- Definition of Done
- canonical sources

## H. Coverage audit

حداقل matrix زیر را بساز:

`ID | Topic | Owner | Docs | Spec | Source | Book | Lab | Failure | Interview | Status`

## I. PDF syllabus

Syllabus را با Master PDF Prompt بساز، version/research cutoff/source baseline را ثبت کن و همه صفحات را visual-QA کن.

## J. Repository bootstrap

قبل از اولین درس:

- syllabus source/PDF را ثبت کن؛
- document registry/state/progress بساز؛
- source registry و coverage/dependency map را ذخیره کن؛
- prompt/workflow لازم برای تولید درس‌ها را آماده کن؛
- next module را صریح ثبت کن.

**قاعده:** کتاب ترتیب آموزشی می‌دهد؛ docs دامنه و رفتار فعلی را؛ spec دقت normative را؛ source implementation واقعی را. هیچ‌کدام به‌تنهایی syllabus expert-level کامل نیست.
