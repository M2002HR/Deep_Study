# Docker Track Progress

این فایل stateهای مختلف مسیر را از هم جدا نگه می‌دارد. تعریف رسمی در `meta/standards/PROGRESSION_AND_PREREQUISITES.md` است.

| ID | Document | Authoring | Publication | Prerequisite readiness | Learner mastery | Next dependency |
|---|---|---|---|---|---|---|
| DKR.01 | DS-DKR-01 - تاریخچه و مدل ذهنی کانتینر | complete | published-canonical / v1.0.0 / 37 pages | not-applicable | not assessed | learner: DKR.02 after DKR.01 mastery gate |
| DKR.02 | DS-DKR-02 - نصب، Editions، Platforms و Distribution | **eligible / next-to-author** | planned | `META.DKR.02`: evidence-required before practical Lab | not-started | DKR.03 after required mastery gates |

## وضعیت فعلی learner

مطالعه واقعی پروژه از `DKR.01` شروع شده است. PDF آن آماده است، اما هنوز evidence تسلط learner ثبت نشده است.

برای mastered شدن `DKR.01` حداقل این evidence لازم است:

- مطالعه کامل درس؛
- انجام Lab process/namespace و ثبت observationها؛
- پاسخ به challengeها بدون نگاه به جواب آماده؛
- teach-back برای partner بدون note؛
- پاسخ interview در سطح 30 ثانیه، حدود 3 دقیقه و deep dive؛
- پاس‌کردن Mastery Checklist خود سند.

## وضعیت authoring بعدی

`DKR.02` از نظر **authoring** next eligible document است و می‌تواند قبل از mastered شدن `DKR.01` آماده و حتی منتشر شود. این کار فقط محتوا را برای آینده آماده می‌کند و learner mastery را تغییر نمی‌دهد.

Upstream canonical لازم برای authoring موجود است:

- `DKR.01` / `DS-DKR-01` = `published-canonical`.

Prerequisite دوم syllabus یعنی `META.DKR.02` برای `DKR.02` یک prerequisite عملی/محیطی مهم است. publication یک PDF مستقل برای `META.DKR.02` شرط authoring `DKR.02` نیست، اما readiness آن باید قبل از اجرای Lab واقعی `DKR.02` evidence داشته باشد.

### Evidence حداقلی readiness برای META.DKR.02

قبل از Lab عملی DKR.02 ثبت شود:

- حداقل یک Linux VM disposable یا محیط آزمایش امن؛
- امکان snapshot/restore یا rebuild سریع؛
- ثبت `uname`، kernel، cgroup mode، filesystem و firewall backend؛
- ثبت نسخه‌های واقعی Docker Engine/CLI و در صورت وجود BuildKit/containerd/runc؛
- دسترسی به ابزارهای پایه مورد نیاز module مانند `docker`, `curl`, `jq`, `systemctl` و ابزارهای inspection مرتبط؛
- privileged/network experiments فقط در محیط disposable.

وضعیت فعلی این evidence: **pending / not yet recorded**.

## قانون وضعیت

- `authoring`: وضعیت تحقیق/ساخت سند است؛ به learner mastery وابسته نیست مگر dependency محتوایی authoring حل نشده باشد.
- `published-canonical`: source، PDF، manifest و QA آماده‌اند.
- `prerequisite readiness`: آمادگی محیطی/عملی برای اجرای صحیح Lab است.
- `learner mastery`: فقط وقتی Lab + teach-back + mastery checklist با evidence انجام شده باشد ثبت می‌شود.
- agent نباید صرف ساخته‌شدن یا منتشرشدن PDF، learner را mastered علامت بزند.
- agent نباید pending بودن mastery learner را با blocked بودن authoring سند بعدی یکی بداند.
- برای **شروع مطالعه رسمی DKR.02 توسط learner**، Mastery Gate `DKR.01` و readiness لازم `META.DKR.02` باید بررسی شوند.
