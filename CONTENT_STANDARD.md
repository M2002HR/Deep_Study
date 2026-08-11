# Content Standard for Canonical Study Documents

هر Study PDF یک **Mastery Document** است، نه خلاصه‌ی عمومی.

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

هر سند باید صریحاً شامل موارد زیر باشد:

- In Scope
- Out of Scope
- Prerequisites
- Assumed knowledge
- Version-sensitive areas
- Cross-document references
- What mastery of this document does **not** imply

## ساختار محتوایی پیش‌فرض

1. Executive orientation / هدف
2. Why this exists
3. Historical context در حد مفید
4. Terminology and invariants
5. Mental model
6. Architecture / state model
7. Detailed mechanics
8. Internals
9. Interfaces / API / CLI / config surface
10. Connections to other systems
11. Security implications
12. Performance/resource implications
13. Production considerations
14. Failure modes
15. Troubleshooting decision trees
16. Hands-on labs
17. Experiments / prediction tasks
18. Source/spec reading
19. Common misconceptions
20. Interview ladder (30s / 3m / 30m)
21. Teach-back questions
22. Exercises / challenge tasks
23. Mastery checklist
24. Open questions / unresolved items
25. References and provenance
26. Version history / changelog

ساختار می‌تواند برای موضوع خاص تغییر کند، اما حذف یک بخش relevant باید intentional و در Scope Contract قابل توضیح باشد.

## قانون depth

هر مفهوم مهم باید در مناسب‌ترین عمق از این زنجیره قرار گیرد:
`definition -> motivation -> model -> mechanism -> failure -> observation/debug -> implementation boundary -> source/spec evidence`.

## جلوگیری از duplication

- foundational explanation فقط در owner document کامل می‌آید؛ اسناد downstream خلاصه و cross-reference می‌دهند.
- terminology canonical در `meta/standards/TERMINOLOGY.md` ثبت می‌شود.
- اگر ownership یک مفهوم مبهم است، قبل از نوشتن PDF در coverage matrix مشخص شود.
