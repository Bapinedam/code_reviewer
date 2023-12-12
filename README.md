# code_reviewer 

By: Brayam Pineda.

Version: 0.1.0

This is an attempt of creation a code reviewer based on GPT-4

## Create environment

```bash
conda env create -f environment.yml
activate code_reviewer
```

or 

```bash
mamba env create -f environment.yml
activate code_reviewer
```

## Project organization

    code_reviewer
        ├── data
        │   ├── processed      <- The final, canonical data sets for modeling.
        │   └── raw            <- The original, immutable data dump.
        │
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                         the creator's initials, and a short `-` delimited description, e.g.
        │                         `1.0-initial-data-exploration`.
        │
        ├── .gitignore         <- Files to ignore by `git`.
        │
        ├── environment.yml    <- The requirements file for reproducing the analysis environment.
        │
        └── README.md          <- The top-level README for developers using this project.

---
