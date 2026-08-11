# Source Policy

## Source hierarchy

برای claimهای فنی، اولویت پیش‌فرض:

1. Normative specifications / standards
2. Official product/project documentation
3. Primary source code + tests + release notes + design docs
4. Maintainer-authored material / project proposals
5. High-quality books and papers
6. Secondary technical articles
7. Community discussions - فقط برای signals/edge cases، با verification

## Currentness

هر claim که به نسخه، رفتار فعلی، default، deprecation، security، API یا product feature وابسته است باید در زمان تولید/به‌روزرسانی document دوباره verify شود.

## Provenance

- ادعای normative به spec section وصل شود.
- implementation-specific claim در صورت اهمیت با repository + tag/commit/path ثبت شود.
- source baseline در metadata سند pin شود.
- اگر sourceها اختلاف دارند، اختلاف و scope هر کدام نوشته شود؛ synthesis نباید disagreement را پنهان کند.

## Books

کتاب برای pedagogical ordering و coherence استفاده می‌شود، نه به‌عنوان تنها Source of Truth برای ابزار version-sensitive.

## Copyright

- کتاب تجاری یا PDF دارای copyright در Git نگهداری نمی‌شود مگر license/اجازه صریح وجود داشته باشد.
- catalog فقط metadata و location قانونی را ثبت می‌کند.
- quoteهای کوتاه در حد ضرورت؛ اصل کار synthesis و paraphrase است.
- specifications/documentation با license مناسب فقط در صورت نیاز mirror می‌شوند؛ در غیر این صورت link + version pin ترجیح دارد.
