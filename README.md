# The Turing Test Revisited - Arabic NLP

**Machine Learning's Ability to Identify AI-Generated Text**

مشروع تخرج جماعي في علوم الحاسب بجامعة الملك سعود. كان دوري تنظيف البيانات العربية التي جمعها الزملاء وتدريب النماذج العربية. يعرض هذا المستودع كود التجارب العربية على المقالات والمراجعات والتغريدات، مع أداة تنظيف من نسخة بحثية لاحقة.

My contribution was the Arabic-language component: cleaning Arabic data collected by teammates and training Arabic models. This source release covers article, review, and tweet experiments with AraBERT, PyTorch, and Transformers.

## Small offline example

Try the later cleaning helper without downloading a model or supplying research data:

```sh
python examples/cleaning_demo.py
```

| Synthetic input | Actual cleaned output |
| --- | --- |
| `أهلا #مثال @demo https://example.invalid/demo` | `اهلا مثال` |
| `إبداع في آفاق اللغة العربية` | `ابداع في افاق اللغة العربية` |
| `جميييييل` | `جمييل` |
| `مِثال` | `مِثال` |

[Runnable example](examples/cleaning_demo.py) · [Captured plain-text output](examples/output.txt)

This example was added for the portfolio in November 2026. It illustrates preprocessing only: repeated characters are limited to two and Arabic diacritics can remain. It does not execute the 2024 training experiments, classify text, or demonstrate model quality.

## Course and original project dates

- **Course / المادة:** Computer Science Graduation Project, King Saud University. The surviving team report is labeled **CSC 496**.
- **Original research / التاريخ الأصلي:** **March-May 2024**, supported by the local experiment files and the team report saved in May 2024.
- **Later cleaning variant:** the extracted cleaning helper comes from a local notebook last saved on **17 December 2025** and is documented separately from the 2024 experiments.
- **Publication review:** 9 November 2026. GitHub commit dates describe publication, not when the original research was completed.

The team report lists Nasser AlGasabi, Abdullah AlJabri, Salman AlEisa, Nawaf AlMazyad, and Mohammed AlDamegh. Team context is credited; the repository presents my Arabic work. Other members collected data and worked on other components, including English.

## Source contents

| File | Purpose | Original source version |
| --- | --- | --- |
| [arabert-articles.ipynb](notebooks/arabert-articles.ipynb) | Arabic article experiment, including balancing and model training | 11 May 2024 |
| [arabert-reviews.ipynb](notebooks/arabert-reviews.ipynb) | Arabic review experiment | 12 May 2024 |
| [arabert-arabic.ipynb](notebooks/arabert-arabic.ipynb) | Arabic tweet experiment; retains the existing public notebook path | 20 May 2024 |
| [arabic_cleaning.py](preprocessing/arabic_cleaning.py) | Extracted text-cleaning function and a new streaming CSV wrapper | Later variant saved 17 December 2025 |
| [PUBLICATION.md](PUBLICATION.md) | Provenance, sanitization, validation, and release scope | Publication documentation |

These are selected final source variants rather than every duplicate experiment. Data collection, original corpora, trained models, checkpoints, shared reports, and English components are separate from this source release.

## Inspect and run

Read the notebooks on GitHub without executing them. The cleaning helper and its tests use Python's standard library:

```sh
python -m unittest discover -s tests -v
python preprocessing/arabic_cleaning.py --input data/input.csv --output artifacts/cleaned.csv
```

The cleaner expects `text,label` CSV columns and labels `0` or `1`. It removes links/mentions and non-Arabic-block characters, normalizes alef variants, limits repeated characters to two, and collapses whitespace. Arabic-block digits, punctuation, diacritics, and tatweel can remain. It does not implement every normalization mentioned in the historical comments. Review suitability for your own data before reuse.

To inspect training in an isolated environment:

```sh
python -m venv .venv
# Activate the environment for your operating system.
python -m pip install -r requirements.txt
python -m jupyterlab
```

Open a notebook from `notebooks/`. Supply authorized `data/train.csv` and `data/test.csv` files containing `text` and numeric `label` columns; the code maps `0 = AI` and `1 = Human`. Select a checkpoint you trained before setting `model_path` in final inference. The `artifacts/model` value is a placeholder. Notebook execution downloads upstream model/tokenizer and evaluation resources.

## Validation and research limitations

All published notebook code cells pass Python syntax parsing. The cleaning function and CSV wrapper pass synthetic regression checks. Training, model download, end-to-end inference, and historical model scores were not rerun. Requirements are inferred from imports and are not a tested environment lock.

Historical training and evaluation logic is preserved: random splits lack fixed seeds/explicit stratification, some balancing assumes enough examples in one class, sections use different preprocessing/tokenization lengths, and the final evaluation averages per-batch metrics while restricting labels to predictions in each batch. Those metrics can differ from global evaluation. The article notebook's historical evaluation input originally carried a tweet-oriented filename; the correct evaluation corpus must be verified before reuse.

The first inference example loads an upstream base model. A separately fine-tuned checkpoint is required for task inference. No accuracy or F1 result is asserted by this release, and experimental predictions must not be used as evidence that a person used AI.

## Upstream components and scope

The experiments reference [AraBERT](https://github.com/aub-mind/arabert), [Transformers](https://github.com/huggingface/transformers), [PyTorch](https://github.com/pytorch/pytorch), and the [AraBERT Twitter checkpoint](https://huggingface.co/aubmindlab/bert-base-arabertv02-twitter). Their respective terms apply; those components are referenced rather than bundled.

Publication covers selected Arabic code and the extracted helper. It grants no additional rights to teammates' datasets, shared reports, or upstream assets. No blanket open-source license is applied. Student identifiers, faculty names, original outputs, embedded data, credentials, and machine-specific paths are excluded.

[Portfolio](https://maldamegh.sa/)
