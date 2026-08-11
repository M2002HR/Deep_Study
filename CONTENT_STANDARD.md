# Content Standard for Canonical Study Documents

هر PDF آموزشی باید یک سند عمیق و قابل اتکا باشد، نه یک خلاصه عمومی.

## زبان فارسی

- فارسی باید **ساده، روشن و طبیعی** باشد.
- جمله‌ها تا جای ممکن کوتاه، مستقیم و بدون پیچیدگی بی‌دلیل باشند.
- از لحن اداری، واژه‌های سنگین، ترجمه تحت‌اللفظی و جمله‌های طولانی پرهیز شود.
- عمق فنی کم نشود؛ موضوع سخت را با زبان ساده توضیح بده.
- انگلیسی را متعادل استفاده کن. نام ابزار، command، API، path، version و اصطلاح فنی جاافتاده می‌تواند انگلیسی بماند؛ ولی جمله فارسی را بی‌دلیل با کلمات انگلیسی پر نکن.
- اگر معادل فارسی ساده و طبیعی وجود دارد، در اولین استفاده شکل فارسی را بنویس و اصطلاح انگلیسی را داخل پرانتز بیاور؛ بعد از آن شکل ساده‌تر را ثابت نگه دار.
- اصطلاح فنی‌ای که ترجمه فارسی آن مصنوعی یا گیج‌کننده است، به شکل رایج انگلیسی نگه داشته شود و یک بار ساده توضیح داده شود.
- متن باید برای مطالعه طولانی راحت باشد و خواننده برای فهم ساختار جمله انرژی اضافه مصرف نکند.

## ریزدانگی

قبل از نوشتن Study PDF، `meta/standards/MODULE_GRANULARITY.md` را اجرا کن. هر سند باید یک mastery milestone روشن داشته باشد. page count به‌تنهایی معیار split/merge نیست.

## Metadata اجباری

- Document ID
- Title
- Curriculum / Track
- Version
- Status: draft / reviewed / canonical / deprecated
- Research cutoff
- Last reviewed
- Scope owner
- Prerequisites
- Upstream dependencies
- Downstream dependencies
- Source baseline (versions/tags/commits where relevant)

## Scope Contract اجباری

هر سند باید روشن کند:

- In Scope
- Out of Scope
- Prerequisites
- Assumed knowledge
- Version-sensitive areas
- Cross-document references
- What mastery of this document does **not** imply

## ساختار محتوایی پیش‌فرض

1. هدف و نمای کلی
2. چرا این موضوع وجود دارد
3. تاریخچه در حدی که کمک کند
4. اصطلاحات و قواعد ثابت
5. مدل ذهنی
6. معماری / مدل وضعیت
7. سازوکار دقیق
8. جزئیات داخلی
9. رابط‌ها / API / CLI / تنظیمات
10. ارتباط با سیستم‌های دیگر
11. نکات امنیتی
12. کارایی و مصرف منابع
13. نکات محیط واقعی و production
14. خطاها و حالت‌های شکست
15. مسیرهای عیب‌یابی
16. آزمایش‌های عملی
17. تمرین پیش‌بینی و مشاهده
18. خواندن source/spec
19. برداشت‌های اشتباه رایج
20. پاسخ مصاحبه در سه عمق 30s / 3m / 30m
21. سوال‌های teach-back
22. تمرین و challenge
23. چک‌لیست تسلط
24. سوال‌ها و موارد حل‌نشده
25. منابع و منشأ ادعاها
26. تاریخچه نسخه‌ها / changelog

ساختار می‌تواند برای موضوع خاص تغییر کند، اما حذف یک بخش مهم باید عمدی و در Scope Contract قابل توضیح باشد.

## قانون عمق

هر مفهوم مهم باید تا عمق مناسب این مسیر پیش برود:
`definition -> motivation -> model -> mechanism -> failure -> observation/debug -> implementation boundary -> source/spec evidence`.

## جلوگیری از تکرار

- توضیح کامل یک مفهوم پایه فقط در سند صاحب آن مفهوم می‌آید؛ سندهای بعدی خلاصه می‌کنند و لینک می‌دهند.
- اصطلاحات ثابت در `meta/standards/TERMINOLOGY.md` ثبت می‌شوند.
- اگر معلوم نیست یک مفهوم متعلق به کدام سند است، قبل از نوشتن PDF در coverage matrix مشخص شود.
