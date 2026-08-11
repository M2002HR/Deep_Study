# Study Method

## چرخه‌ی اصلی هر موضوع

1. **Why / problem statement** - چرا این مفهوم یا ابزار وجود دارد؟
2. **Mental model** - abstractionها و state model را بساز.
3. **Mechanics** - happy path را دقیق دنبال کن.
4. **Internals** - abstraction را تا لایه‌های پایین‌تر بشکن.
5. **Operations** - operation taxonomy و ابزارهای inspect/modify/recover را بشناس.
6. **Failure engineering** - عمداً سیستم را خراب کن.
7. **Debugging** - symptom را به hypothesis و evidence تبدیل کن.
8. **Connections** - dependency و boundary با ابزارها/مفاهیم دیگر را رسم کن.
9. **Build** - بخشی از mechanism را بازسازی یا instrument کن.
10. **Teach-back** - بدون note توضیح بده.
11. **Interview ladder** - پاسخ ۳۰ ثانیه، ۳ دقیقه، ۳۰ دقیقه.
12. **Revisit** - در spiral بعدی با عمق بیشتر برگرد.

## Spiral Learning

Prerequisiteها قرار نیست قبل از شروع یک ابزار «کامل» شوند. وقتی Docker ما را به namespace، cgroup، OverlayFS یا routing می‌رساند، prerequisite به اندازه‌ی لازم باز می‌شود؛ بعداً به‌صورت module مستقل عمیق می‌شود و دوباره به Docker برمی‌گردیم.

## نقش منابع

- Books: coherence و fundamentals پایدار.
- Official docs: رفتار فعلی و surface واقعی ابزار.
- Specifications: semantics دقیق و interoperability contract.
- Source/tests/issues/PRs: implementation reality و edge cases.
- YouTube/visual media: intuition و visualization، نه Source of Truth.
- ChatGPT: tutor، adversarial examiner، synthesis و gap analysis؛ نه جایگزین source.
- NotebookLM: synthesis روی corpus curated.
- Codex: implementation/review/test/source tracing؛ ابتدا فهم و تلاش خود learner حفظ شود.

## مطالعه‌ی دونفره

### Teach Without Notes
هر نفر یک مفهوم را بدون note روی تخته توضیح و diagram می‌کند؛ نفر دوم boundary question می‌پرسد.

### Attack / Defend
یک claim فنی مطرح می‌شود و طرف مقابل باید assumptions، exceptions و counterexampleها را پیدا کند.

### Mutual Interview
هفته‌ای یک جلسه interviewer/candidate با role rotation، شامل conceptual + debugging + architecture + source-reading question.

### Incident Pairing
یک نفر incident را طراحی و evidence را مرحله‌ای آشکار می‌کند؛ نفر دیگر باید hypothesis-driven debug کند.

## قانون AI

AI باید اصطکاک مفید یادگیری را حذف نکند. برای assessment، پیش‌فرض این است که ابتدا سؤال/سناریو بدهد و جواب را تا وقتی learner تلاش نکرده آشکار نکند.
