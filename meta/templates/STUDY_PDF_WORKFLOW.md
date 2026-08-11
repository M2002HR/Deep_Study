# Template - CI برای Study PDF جدید

برای PDF جدید، workflow `build-dkr01.yml` را کورکورانه copy نکن. اول این چیزها را عوض کن:

- pathهای source/manifest؛
- Document ID و output filename؛
- trigger pathها؛
- artifact name.

همیشه این gateها را نگه دار:

1. Vazirmatn pinned + fontconfig registration؛
2. build با `scripts/build_study_pdf.py`؛
3. `check_pdf_fonts.sh`؛
4. `check_pdf_clearance.py --min-mm 20 --frame-inset-mm 5 --min-frame-gap-mm 14`؛
5. text extraction و replacement-glyph check؛
6. candidate artifact فقط برای visual QA؛
7. canonical artifact فقط بعد از exact-candidate visual approval.

در آینده اگر تعداد اسناد زیاد شد، این workflowها را به reusable workflow تبدیل کن؛ اما validation gateها را کم نکن.
