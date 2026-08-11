# Prompt - ادامه مسیر موجود

این prompt را وقتی اجرا کن که repository قبلاً syllabus و چند سند دارد و باید مسیر ادامه پیدا کند.

1. `START_HERE.md`, `CURRENT_STATE.md`, `AGENTS.md` و تمام اسناد مادر را بخوان.
2. وضعیت واقعی GitHub را verify کن و اختلاف state را اصلاح کن.
3. syllabus مسیر فعال را بخوان و next eligible ID را از dependencyها پیدا کن.
4. Scope همان ID را استخراج کن؛ چیزی را از حافظه خودت به scope اضافه نکن مگر با gap analysis و ثبت در syllabus.
5. `MODULE_GRANULARITY.md` را اجرا کن و تصمیم split/merge را قبل از research ثبت کن.
6. upstream owner documents را بخوان تا terminology و مدل ذهنی با اسناد قبلی هماهنگ بماند.
7. source set فعلی را از spec/docs/source/release notes/books تعیین و version-sensitive claims را دوباره verify کن.
8. research questions -> evidence -> unresolved -> draft را بساز.
9. فارسی را ساده و طبیعی بنویس؛ انگلیسی را فقط برای نام‌ها، commandها و اصطلاحات رایج فنی نگه دار.
10. Lab، failure، interview 30s/3m/30m، teach-back و Mastery Checklist را متناسب با scope بساز.
11. PDF را فقط با Master PDF Prompt تولید کن.
12. mechanical preflight + full-page visual QA را کامل اجرا کن.
13. registry/state/progress/manifest/QA را به‌روزرسانی کن.
14. در پایان دقیقاً بنویس learner بعد از این سند چه milestoneی دارد و next ID چیست.

**ممنوع:** شروع درس بعدی فقط چون «منطقی به نظر می‌رسد»، تولید memory-only، تغییر بی‌دلیل اصطلاحات، یا انتشار PDF بدون full visual QA.
