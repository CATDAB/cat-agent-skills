# Knowledge Readiness Rubric

Use this rubric to score knowledge sources for Copilot Studio readiness.

## Weighted score

| Category | Weight | What to assess |
|---|---:|---|
| Coverage | 25 | The source answers the top user intents completely and directly. |
| Accuracy and conflict risk | 20 | Content is authoritative, non-duplicative, and does not conflict with other sources. |
| Structure and chunkability | 20 | Headings, sections, page length, tables, and FAQ structure support reliable retrieval. |
| Freshness | 15 | Content has recent review dates, owners, effective dates, and no stale instructions. |
| Permissions and sensitivity | 10 | Users can only retrieve content they are allowed to see. Weight is intentionally low because this category acts as a hard gate (see below), not a contributing score. |
| Metadata completeness | 10 | Content has owner, audience, product, region, category, and lifecycle metadata. |

## Category scoring

Score each category from 0 to 5, then multiply by the category weight.

| Score | Meaning |
|---:|---|
| 5 | Strong. Ready with minor or no changes. |
| 4 | Good. Some cleanup recommended but not blocking. |
| 3 | Usable for pilot. Known gaps or risks require tracking. |
| 2 | Weak. Significant remediation needed before broad use. |
| 1 | Poor. High risk of wrong, stale, or incomplete answers. |
| 0 | Missing, inaccessible, or unsafe. |

Formula:

```text
weighted category score = (category score / 5) * category weight
total score = sum(weighted category scores)
```

## Recommendation bands

| Total | Recommendation |
|---:|---|
| 85-100 | Production-ready with monitoring. |
| 70-84 | Pilot-ready with targeted remediation. |
| 50-69 | Limited pilot only; high-severity findings must be fixed before production. |
| 0-49 | Not ready; remediate source quality and governance first. |

## Hard gates

Do not recommend production if any of these are true:

- Sensitive or restricted content is available to the wrong audience.
- Two authoritative sources give conflicting answers for a high-volume or high-risk question.
- The source lacks enough coverage for the agent's primary purpose.
- The source requires live status, approvals, transactions, or writes but no action/tool is available.
- There is no owner or remediation path for high-severity findings.

## Severity definitions

| Severity | Definition |
|---|---|
| High | Likely to cause wrong answers, data exposure, failed workflows, or production-blocking user harm. |
| Medium | Likely to reduce answer quality, create confusion, or increase support burden. |
| Low | Cleanup or polish that improves maintainability but does not block pilot. |
