# Project Charter - Deep Study

## مأموریت

ساخت یک knowledge system شخصی و قابل‌تداوم برای یادگیری بسیار عمیق software systems، به‌نحوی که برای هر حوزه بتوان از سطح user به power user، production operator، troubleshooter/architect، internals expert و contributor رسید.

## تعریف موفقیت

هدف «حفظ کردن commandها» یا «تمام کردن courseها» نیست. موفقیت یعنی:

- فهم دقیق مسئله‌ای که هر abstraction حل می‌کند؛
- توانایی توضیح mechanics و architecture از سطح high-level تا پایین‌ترین لایه‌ی مرتبط؛
- توانایی تشخیص failure domain و debugging سیستماتیک؛
- توانایی کار با docs/spec/source code و پیدا کردن پاسخ ناشناخته؛
- توانایی ساخت یا بازسازی اجزای کوچک برای اثبات فهم؛
- آمادگی interview در سه عمق ۳۰ ثانیه، ۳ دقیقه و ۳۰ دقیقه؛
- توانایی بررسی issue/PR واقعی و در نهایت contribution.

## معماری دانش

`Canonical sources -> research/synthesis -> Markdown source -> PDF study artifact -> labs/failures/assessment -> mastery evidence`

PDF سند مصرفی اصلی است، اما هیچ PDF به‌تنهایی منبع قابل‌ویرایش پروژه نیست. هر PDF باید از source versioned بازتولیدپذیر باشد.

## قواعد غیرقابل مذاکره

1. ادعای version-sensitive بدون verification فعلی ممنوع است.
2. مدل نباید از حافظه‌ی خود به‌تنهایی یک module نهایی بسازد.
3. منابع اولیه و رسمی بر blog/tutorial مقدم‌اند.
4. اختلاف منابع پنهان نمی‌شود.
5. Scope هر سند باید explicit باشد.
6. هر اصلاح روی آخرین نسخه‌ی پذیرفته‌شده انجام می‌شود، نه نسخه‌ی قدیمی.
7. PDF نهایی بدون visual QA همه‌ی صفحات «Done» نیست.
8. فونت اصلی پروژه برای اسناد فارسی Vazirmatn است.
9. محتوای copyrighted تجاری بدون مجوز در repository ذخیره نمی‌شود.
10. تغییر foundational document باید downstream impact را مشخص کند.
