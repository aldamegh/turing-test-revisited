# The Turing Test Revisited — Arabic NLP

**Machine Learning's Ability to Identify AI-Generated Text**

## دوري في المشروع

أنا محمد الدامغ. شاركت في هذا المشروع الجماعي للتخرج في علوم الحاسب بجامعة الملك سعود، وكان دوري العمل على الجزء العربي: تنظيف البيانات العربية التي جمعها الزملاء وتدريب النموذج. تولّى أعضاء آخرون جمع البيانات والعمل على الجزء الإنجليزي.

يعرض هذا المستودع نسخة منقحة من كود تجربة عربية كتبتها، باستخدام AraBERT وPyTorch وTransformers.

## My contribution

I am Mohammed AlDamegh. My role in this team graduation project was the Arabic-language component: cleaning Arabic data collected by teammates and training the Arabic model. Other team members collected data and worked on the English-language components.

This repository contains one selected Arabic tweet-classification experiment from my research notebooks. It demonstrates text preprocessing, tokenization, a PyTorch training loop, checkpoint saving, inference, and evaluation. It is not the complete research archive or every data-cleaning step used during the project.

## Contents

- [`notebooks/arabert-arabic.ipynb`](notebooks/arabert-arabic.ipynb): sanitized historical Arabic experiment; no saved outputs or embedded data.
- [`requirements.txt`](requirements.txt): dependencies inferred from the notebook imports; not a tested environment lock.
- [`PUBLICATION.md`](PUBLICATION.md): authorship, publication boundaries, sanitization, and validation.

## Inspect or run

You can read the notebook directly on GitHub without executing it. To run it, use an isolated Python/Jupyter environment and review dependency compatibility first:

```sh
python -m venv .venv
# Activate the environment using the command for your operating system.
python -m pip install -r requirements.txt
python -m jupyterlab
```

Open the notebook from `notebooks/` so its relative paths resolve. Supply your own authorized `data/train.csv` and `data/test.csv` files with `text` and numeric `label` columns. The notebook names labels `0 = AI` and `1 = Human`; verify your labels before training. Do not use the original project data unless you have independently established permission.

The training code writes to `artifacts/trained/`; choose a generated checkpoint and update `model_path` before the final inference section. The generic `artifacts/model` path is a placeholder, not an included trained model. The `artifacts/` directory is ignored by Git.

Running downloads upstream model/tokenizer assets and evaluation resources. No dataset, shared report, trained weight, checkpoint, log, or original Git history is distributed in this repository.

## Research limitations

This is an archival source release. Training and end-to-end inference were not rerun when preparing it, and dependency versions are not locked. No accuracy or F1 result is claimed for this release.

The original experiment uses random train/test splitting without a fixed seed or explicit stratification. Its final evaluation helper averages per-batch metrics and restricts labels to those predicted in each batch; those figures are not equivalent to a single global metric calculation and can be misleading. The preprocessing setup and tokenization lengths also differ between sections and require review before reuse. These historical choices remain visible rather than being silently rewritten.

The first inference example uses an upstream pretrained model before task training, so its outputs must not be treated as a trained AI-text detector. A prediction from this experimental code is not evidence that a person used AI.

## Upstream components and project scope

The notebook imports [AraBERT preprocessing](https://github.com/aub-mind/arabert), [Transformers](https://github.com/huggingface/transformers), and [PyTorch](https://github.com/pytorch/pytorch), and references the upstream [AraBERT Twitter checkpoint](https://huggingface.co/aubmindlab/bert-base-arabertv02-twitter). These upstream components are not authored by me; their respective terms apply. They are referenced, not bundled here.

Publication of my selected code does not grant rights to the shared research report, teammates' data or code, or any third-party datasets and weights. No additional open-source license is granted by this release.

[Portfolio / موقعي](https://maldamegh.sa/)
