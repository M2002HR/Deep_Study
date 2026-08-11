# Terminology Registry

هدف این فایل جلوگیری از drift اصطلاحات بین PDFهاست. هر curriculum می‌تواند extension خود را داشته باشد.

## قانون کلی فارسی/انگلیسی

- هدف اول **فهم راحت خواننده فارسی‌زبان** است، نه نمایش واژه‌های انگلیسی.
- نام product/project، command، API، path، flag، hash و version به شکل اصلی Latin بماند.
- برای اصطلاح فنی رایج، اولین استفاده می‌تواند `فارسی ساده (English term)` باشد و بعد شکل کوتاه‌تر و ثابت استفاده شود.
- اگر ترجمه یک اصطلاح مصنوعی، مبهم یا کم‌استفاده است، خود اصطلاح انگلیسی را نگه دار و یک بار نقش آن را ساده توضیح بده.
- در یک جمله، تعداد واژه‌های انگلیسی را بی‌دلیل زیاد نکن. اگر می‌شود جمله را ساده فارسی نوشت، فارسی بنویس.

## General conventions

| Canonical term | Persian usage | Notes |
|---|---|---|
| container | کانتینر (container) -> سپس «کانتینر» | بعد از تعریف اولیه، در متن فارسی معمولاً «کانتینر» ترجیح دارد. |
| image | ایمیج (image) -> سپس «ایمیج» | با کانتینر اشتباه نشود؛ در command/API شکل `image` حفظ می‌شود. |
| runtime | runtime | ترجمه اجباری نکن؛ scope high-level و OCI runtime را روشن کن. |
| namespace | namespace | نام primitive فنی است؛ اولین بار با توضیح ساده «نمای جداشده از resource» معرفی شود. |
| cgroup | cgroup | نام primitive فنی؛ نقش سازمان‌دهی/کنترل منابع ساده توضیح داده شود. |
| portability | قابلیت جابه‌جایی (portability) | از ادعای مطلق «هرجا اجرا می‌شود» پرهیز شود. |
| isolation | جداسازی (isolation) | isolation را binary/absolute فرض نکن. |
| security boundary | مرز امنیتی (security boundary) | با «کانتینر امن است» جایگزین نشود. |
| Source of Truth | Source of Truth | canonical editable source؛ PDF artifact است. |
| Scope Contract | Scope Contract | In/Out/Prerequisites/Dependencies/version sensitivity. |
| failure mode | حالت خرابی (failure mode) | نوع خرابی، نه صرفاً error message. |
| research cutoff | research cutoff | آخرین تاریخ verification سند. |

Technical proper nouns, API names, flags, paths, hashes and version strings should remain Latin.
