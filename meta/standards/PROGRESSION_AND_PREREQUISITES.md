# Progression and Prerequisite State - Deep Study

این استاندارد مشخص می‌کند «ساخت سند»، «انتشار سند»، «آمادگی prerequisite» و «تسلط learner» چگونه از هم جدا نگه داشته شوند.

## اصل اصلی

چهار state مستقل وجود دارد و agent حق ندارد آن‌ها را به جای هم استفاده کند:

1. **Authoring eligibility** - آیا از نظر syllabus/dependency می‌توان سند بعدی را تحقیق و آماده کرد؟
2. **Publication state** - آیا source + PDF + manifest + QA آن سند canonical و منتشر شده است؟
3. **Prerequisite readiness** - آیا پیش‌نیازهای محیطی/عملی لازم برای اجرای Lab و مطالعه واقعی آماده‌اند؟
4. **Learner mastery** - آیا learner با evidence واقعی Mastery Gate prerequisite را پاس کرده است؟

## Authoring eligibility با learner progression فرق دارد

می‌توان PDF یک module downstream را **پیشاپیش آماده و منتشر** کرد حتی اگر learner هنوز prerequisite قبلی را mastered نکرده باشد، مشروط به این‌که:

- dependency و Scope Contract آن module درست استخراج شده باشد؛
- upstream canonical documents موجود و consistency-audit شده باشند؛
- سند downstream صریحاً prerequisiteهای مطالعه/اجرای Lab را حفظ کند؛
- publication هیچ‌وقت به‌عنوان mastery learner ثبت نشود.

بنابراین «PDF بعدی آماده است» به معنی «learner مجاز است prerequisite را رد کند» نیست.

## انواع prerequisite

### 1. Knowledge / mastery prerequisite

مثل `DKR.01 -> DKR.02`.

برای **مطالعه رسمی و عبور learner**، prerequisite باید طبق `MASTERY.md` با evidence پاس شود. اما authoring سند downstream می‌تواند زودتر انجام شود.

### 2. Operational / environment prerequisite

مثل `META.DKR.02` برای `DKR.02`.

این prerequisite ممکن است قبل از اینکه Study PDF مستقل آن منتشر شود، با یک **readiness evidence** معتبر satisfy شود؛ برای مثال:

- Linux VM disposable آماده؛
- baseline kernel/cgroup/filesystem/firewall ثبت شده؛
- ابزارهای مورد نیاز نصب/قابل دسترس؛
- snapshot/restore یا محیط امن برای آزمایش‌های destructive آماده.

اگر syllabus صریحاً mastery محتوایی همان META module را برای فهم module downstream لازم بداند، readiness عملی به‌تنهایی کافی نیست و باید mastery آن نیز ثبت شود.

### 3. Document / source prerequisite

اگر سند downstream برای terminology، model یا contract به یک owner document canonical وابسته است، آن upstream document باید قبل از publication downstream موجود و consistency-audit شده باشد.

## وضعیت پیشنهادی برای progress files

برای هر module مهم تا جای ممکن این stateها جدا ثبت شوند:

- `authoring`: blocked / eligible / in-progress / candidate / complete
- `publication`: planned / draft / reviewed / published-canonical / deprecated
- `prerequisite_readiness`: not-applicable / pending / ready / evidence-required
- `learner_mastery`: not-started / in-progress / not-assessed / mastered / needs-review

نام دقیق می‌تواند در track متفاوت باشد، اما معنا نباید مخلوط شود.

## قانون انتخاب next ID

وقتی user می‌گوید «PDF بعدی را بساز»:

1. next curriculum ID را از syllabus/dependency graph پیدا کن.
2. prerequisiteها را classify کن: knowledge/mastery، operational/environment، document/source.
3. مشخص کن کدام prerequisite برای **authoring** لازم است و کدام برای **مطالعه learner**.
4. اگر authoring dependency حل است، می‌توان سند را ساخت حتی اگر learner mastery هنوز pending باشد.
5. Scope Contract سند downstream باید تمام prerequisiteهای مطالعه را صریح نگه دارد.

وقتی user می‌گوید «می‌خواهم درس بعدی را شروع کنم/بخوانم»:

- mastery prerequisiteهای learner را بررسی کن؛
- readiness محیطی Lab را بررسی کن؛
- صرف وجود PDF اجازه عبور نیست.

## DKR.02 - تصمیم فعلی

برای مسیر Docker فعلی:

- `DKR.02` از نظر **authoring** next eligible document است.
- `DKR.01` canonical upstream document موجود است، پس authoring dependency آن حل است.
- learner mastery `DKR.01` هنوز `not assessed` است؛ بنابراین progression مطالعاتی learner همچنان gated است.
- `META.DKR.02` یک operational/environment prerequisite برای Lab و مطالعه عملی `DKR.02` است. readiness evidence آن باید قبل از اجرای Lab ثبت شود؛ publication یک PDF مستقل برای `META.DKR.02` شرط authoring `DKR.02` نیست.

اگر بعداً syllabus یا scope روشن کند که بخشی از `META.DKR.02` یک knowledge mastery prerequisite مستقل است، این تصمیم باید update و در progress ثبت شود.

## Publication rule

پس از publication هر Study PDF:

- `DOCUMENT_REGISTRY.md`، coverage matrix، track progress، `CURRENT_STATE.md`، artifact manifest و QA report باید همگی sync شوند.
- CI باید تمام `published-canonical` Study PDFها را از روی registry/manifest validate کند؛ validation نباید فقط نام یک module خاص را hard-code کند.
