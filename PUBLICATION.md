# Provenance and publication review

## Team and source scope

The owner identified Arabic data cleaning and model training as his contribution to the team graduation project. The local May 2024 report confirms the project title and CSC 496 course label. This release presents three selected Arabic experiment variants; duplicate notebooks, unrelated medical coursework, and a report about a different 2020 sentiment-analysis project were excluded.

The 2024 experiment version dates are preserved source modification dates: articles 11 May, reviews 12 May, tweets 20 May. They are not claimed submission timestamps. The cleaning function comes from a later notebook saved on 17 December 2025; the CSV wrapper and tests were added for publication on 9 November 2026. The release does not infer that this later helper was used in every historical experiment.

## Sanitization

All notebook outputs, execution counts, original metadata, cell metadata, and attachments were removed. Raw previews were replaced with comments, the example quotation with synthetic text, and original data/checkpoint/log paths with generic local paths. Shared reports and source archives remain private.

No raw datasets, collected tweets, reviews, emails, medical records, screenshots, original reports, student identifiers, faculty names, credentials, model weights, or training logs are included. The file allowlist contains text source, documentation, and synthetic tests only. Original local files remain unchanged.

## Validation

Notebook JSON structure and all code-cell syntax were checked without execution. Cleaning behavior and the CSV command were checked with synthetic examples. The source tree and notebook JSON were scanned for identifiers, faculty names, contact details, credentials, embedded payloads, local paths, and saved outputs. Automated checks supplement inspection and cannot prove that every possible sensitive string is absent.

No training, dataset loading, model download, full inference, or performance reproduction was attempted. Historical algorithmic and evaluation limitations are recorded in the README. No historical score is republished as a verified result.

## Reuse

The Arabic source release preserves team context and upstream references. It does not relicense datasets, shared reports, other team components, third-party software, or model weights. No blanket license is added.
