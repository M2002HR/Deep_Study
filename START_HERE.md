# از اینجا شروع کن - Deep Study

اگر این repository را در یک چت یا محیط تازه باز کرده‌ای، **قبل از ساختن درس یا syllabus جدید از این فایل شروع کن.**

## ترتیب خواندن

1. `CURRENT_STATE.md` - الان پروژه دقیقاً کجاست و قدم بعدی چیست؟
2. `PROJECT.md` - هدف کل پروژه چیست؟
3. `AGENTS.md` - قرارداد اجرایی برای ChatGPT/Codex/agentها.
4. `meta/standards/GIT_WORKFLOW.md` - تغییرات Git به‌طور پیش‌فرض چگونه ثبت شوند؟
5. `STUDY_METHOD.md` - روش یادگیری پروژه.
6. `CONTENT_STANDARD.md` - هر سند درسی چه کیفیت و ساختاری باید داشته باشد؟
7. `SOURCE_POLICY.md` - از چه منبعی برای چه نوع ادعایی استفاده شود؟
8. `RESEARCH_METHOD.md` - روش تحقیق syllabus و module.
9. `MASTERY.md` - چه زمانی یک درس واقعاً تمام شده است؟
10. `meta/prompts/MASTER_PDF_PROMPT.md` و `meta/prompts/PDF_GENERATION.md` - برای هر PDF اجباری‌اند.
11. syllabus مسیر فعال و سندهای upstream/downstream همان موضوع.

## اگر می‌خواهی مسیر فعلی را ادامه بدهی

`meta/CONTINUATION_PROTOCOL.md` و `meta/prompts/CONTINUE_EXISTING_TRACK.md` را اجرا کن.

## اگر می‌خواهی یک موضوع کاملاً جدید شروع کنی

`meta/prompts/NEW_TOPIC_SYLLABUS.md` را اجرا کن. قبل از نوشتن درس‌ها باید syllabus، coverage، dependencyها و ریزدانگی آن موضوع ساخته و audit شود.

## چند قانون خیلی مهم

- branch اصلی پروژه `main` است.
- تغییرات معمول را مستقیم روی آخرین نسخه `main` ثبت کن.
- به‌صورت پیش‌فرض branch جدا یا Pull Request نساز؛ فقط با درخواست صریح user.
- اگر direct write روی `main` ممکن نبود، خطا را گزارش کن و خودکار PR نساز.
- از حافظه مدل به‌تنهایی سند نهایی نساز.
- Markdown/structured source منبع اصلی است؛ PDF خروجی مطالعه است.
- متن فارسی تا جای ممکن ساده، روشن و طبیعی باشد.
- از انگلیسی فقط جایی استفاده کن که اصطلاح فنی رایج یا نام دقیق لازم است.
- هیچ PDF نهایی نیست تا همه صفحه‌هایش render و بررسی دیداری نشده باشند.
- ساخته‌شدن PDF به معنی mastered شدن درس توسط learner نیست؛ وضعیت مطالعه جدا ثبت می‌شود.
- همیشه روی آخرین نسخه درست ادامه بده و fixهای قبلی را برنگردان.
