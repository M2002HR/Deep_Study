# Docker Track Progress

این فایل stateهای مختلف مسیر را از هم جدا نگه می‌دارد. تعریف رسمی در `meta/standards/PROGRESSION_AND_PREREQUISITES.md` است.

| ID | Document | Authoring | Publication | Prerequisite readiness | Learner mastery | Next dependency |
|---|---|---|---|---|---|---|
| DKR.01 | DS-DKR-01 - تاریخچه و مدل ذهنی کانتینر | complete | published-canonical / v1.0.0 / 37 pages | not-applicable | not assessed | learner: DKR.02 after DKR.01 mastery gate |
| DKR.02 | DS-DKR-02 - نصب، Editions، Platforms و Distribution | complete | published-canonical / v1.0.0 / 42 pages | `META.DKR.02`: evidence-required before practical Lab | not-started | learner: DKR.03 after required mastery gates |
| DKR.03 | DS-DKR-03 - معماری Docker Engine: CLI -> API -> dockerd -> runtime stack | eligible / next-to-author | planned | to-be-derived-from-syllabus-at-authoring | not-started | downstream follows dependency graph |

## وضعیت فعلی learner

مطالعه واقعی learner از `DKR.01` شروع شده است. PDFهای `DKR.01` و `DKR.02` هر دو canonical و آماده مطالعه‌اند، اما publication سند دوم **هیچ Mastery Gateی را دور نمی‌زند**.

وضعیت فعلی evidence:

- `DKR.01`: learner mastery = `not assessed`.
- `DKR.02`: learner mastery = `not-started`.
- `META.DKR.02` readiness برای Lab عملی DKR.02 = `pending / not yet recorded`.

برای mastered شدن `DKR.01` حداقل این evidence لازم است:

- مطالعه کامل درس؛
- انجام Lab process/namespace و ثبت observationها؛
- پاسخ به challengeها بدون نگاه به جواب آماده؛
- teach-back برای partner بدون note؛
- پاسخ interview در سطح 30 ثانیه، حدود 3 دقیقه و deep dive؛
- پاس‌کردن Mastery Checklist خود سند.

## وضعیت authoring بعدی

`DKR.02` اکنون کامل و `published-canonical` است. از نظر authoring، سند بعدی curriculum برابر `DKR.03` است؛ prerequisiteهای محتوایی آن (`DKR.01` و `DKR.02`) هر دو به‌صورت canonical موجودند. قبل از ساخت DKR.03 همچنان continuation protocol، granularity gate و research gate باید از نو اجرا شوند.

## Readiness عملی META.DKR.02

Prerequisite دوم syllabus برای `DKR.02` یک prerequisite عملی/محیطی مهم است. publication مستقل `META.DKR.02` شرط authoring DKR.02 نبود، اما readiness آن باید قبل از اجرای Lab واقعی DKR.02 evidence داشته باشد.

### Evidence حداقلی readiness

قبل از Lab عملی DKR.02 ثبت شود:

- حداقل یک Linux VM disposable یا محیط آزمایش امن؛
- امکان snapshot/restore یا rebuild سریع؛
- ثبت `uname`، kernel، cgroup mode، filesystem و firewall backend؛
- ثبت نسخه‌های واقعی Docker Engine/CLI و در صورت وجود BuildKit/containerd/runc؛
- دسترسی به ابزارهای پایه مورد نیاز module مانند `docker`, `curl`, `jq`, `systemctl` و ابزارهای inspection مرتبط؛
- privileged/network experiments فقط در محیط disposable.

## قانون وضعیت

- `authoring`: وضعیت تحقیق/ساخت سند است؛ به learner mastery وابسته نیست مگر dependency محتوایی authoring حل نشده باشد.
- `published-canonical`: source، PDF، manifest و QA آماده‌اند.
- `prerequisite readiness`: آمادگی محیطی/عملی برای اجرای صحیح Lab است.
- `learner mastery`: فقط وقتی Lab + teach-back + mastery checklist با evidence انجام شده باشد ثبت می‌شود.
- agent نباید صرف ساخته‌شدن یا منتشرشدن PDF، learner را mastered علامت بزند.
- agent نباید pending بودن mastery learner را با blocked بودن authoring سند بعدی یکی بداند.
- برای **شروع مطالعه رسمی DKR.02 توسط learner**، Mastery Gate `DKR.01` و readiness لازم `META.DKR.02` باید بررسی شوند.
