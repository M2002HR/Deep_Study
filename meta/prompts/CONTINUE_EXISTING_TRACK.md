# Prompt - ادامه مسیر موجود

این prompt را وقتی اجرا کن که repository قبلاً syllabus و چند سند دارد و باید مسیر ادامه پیدا کند.

1. `START_HERE.md`, `CURRENT_STATE.md`, `AGENTS.md` و تمام اسناد مادر را بخوان.
2. وضعیت واقعی GitHub و branch پیش‌فرض `main` را verify کن و اختلاف state را اصلاح کن.
3. `meta/standards/GIT_WORKFLOW.md` را بخوان؛ پیش‌فرض این پروژه نوشتن مستقیم روی `main` بدون branch و PR است.
4. `meta/standards/PROGRESSION_AND_PREREQUISITES.md` را بخوان و authoring/publication/readiness/mastery را از هم جدا نگه دار.
5. syllabus مسیر فعال را بخوان و next eligible ID را از dependencyها پیدا کن.
6. prerequisiteهای همان ID را classify کن: knowledge/mastery، operational/environment، document/source.
7. اگر user **PDF بعدی را می‌خواهد**، authoring eligibility را بررسی کن؛ pending بودن learner mastery به‌تنهایی authoring downstream را block نمی‌کند. اگر user **می‌خواهد درس بعدی را شروع کند**، mastery prerequisite و readiness عملی را جدا gate کن.
8. Scope همان ID را استخراج کن؛ چیزی را از حافظه خودت به scope اضافه نکن مگر با gap analysis و ثبت در syllabus.
9. `MODULE_GRANULARITY.md` را اجرا کن و تصمیم split/merge را قبل از research ثبت کن.
10. upstream owner documents را بخوان تا terminology و مدل ذهنی با اسناد قبلی هماهنگ بماند.
11. source set فعلی را از spec/docs/source/release notes/books تعیین و version-sensitive claims را دوباره verify کن.
12. research questions -> evidence -> unresolved -> draft را بساز.
13. فارسی را ساده و طبیعی بنویس؛ انگلیسی را فقط برای نام‌ها، commandها و اصطلاحات رایج فنی نگه دار.
14. Lab، failure، interview 30s/3m/30m، teach-back و Mastery Checklist را متناسب با scope بساز.
15. PDF را فقط با Master PDF Prompt تولید کن.
16. mechanical preflight + full-page visual QA را کامل اجرا کن.
17. registry + coverage + state + progress + manifest + QA را با هم به‌روزرسانی کن.
18. CI عمومی published Study PDFها را طوری نگه دار که سند جدید از روی registry/manifest validate شود؛ validation جدید را فقط برای یک Document ID hard-code نکن مگر دلیل نسخه‌ای روشن داشته باشی.
19. تغییرات تأییدشده را مستقیم روی آخرین `main` ثبت کن. branch یا Pull Request فقط با درخواست صریح user ساخته شود.
20. در پایان دقیقاً بنویس learner بعد از این سند چه milestoneی دارد، چه prerequisite readiness/mastery هنوز pending است و next ID چیست.

**ممنوع:** شروع درس بعدی فقط چون «منطقی به نظر می‌رسد»، قاطی‌کردن authoring eligibility با learner mastery، تولید memory-only، تغییر بی‌دلیل اصطلاحات، انتشار PDF بدون full visual QA، عقب‌ماندن coverage/progress از registry، یا ساخت خودکار branch/PR بدون درخواست صریح user.
