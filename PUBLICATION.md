# Authorship, privacy, and validation

## Authorship and team context

Mohammed AlDamegh confirmed that the Arabic code is his work, and that he handled Arabic data cleaning and model training. Teammates collected the data and worked on other components, including English. This release contains only one selected Arabic notebook, not the full team's work. No claim of sole authorship of the graduation research is made.

## Sanitization

- Removed all 33 saved output objects, execution counters, original notebook metadata, and cell metadata.
- Replaced six raw-data preview cells with comments to avoid displaying teammates' text on later runs.
- Replaced a sample quotation with a newly authored synthetic sentence.
- Replaced original dataset filenames and experiment-specific checkpoint paths with generic local input/output paths.
- Included no attachments, embedded images, dataset rows, original reports, student identifiers, personal contact details, archives, model weights, or checkpoint files.
- Retained the historical training and metric logic; described its limitations in the README instead of claiming it was revalidated.
- Created a fresh publication history. No source archive history is imported.

## Validation performed

All notebook code cells passed Python syntax parsing. The complete notebook JSON, cell sources, metadata, and documentation were reviewed for personal data, secrets, embedded payloads, and raw examples. The final file allowlist contains UTF-8 text only. Automated pattern checks supplement manual inspection; they do not prove the absence of every possible secret.

No training, model download, dataset loading, installation, or end-to-end inference was performed. Runtime compatibility and model quality remain unverified. The previous experiment's metrics are not included as results.

## Reuse boundaries

The user's authorship clarification applies to this Arabic code. It does not authorize publication of teammates' collected data, shared reports, English code, model weights, or Syaq source. Those remain excluded. Referenced upstream software and models retain their own rights. No broad license for these materials is inferred.
