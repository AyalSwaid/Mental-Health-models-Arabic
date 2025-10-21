# 📊 Model Performance Comparison

This report summarizes the evaluation results of multiple Arabic-language models: **DK (domain knowledge) AraBERTv0.2-large**, **Gemma-3-4B**, and **Famar-9B** - across four  prediction tasks: GSR, depression, self-hurt, sexual-hurt
Metrics include **Accuracy**, **Precision**, **Recall**, **F1**, and **F2** scores.

---

## GSR Results Summary

| Model          | Accuracy | Precision | Recall | F1  | F2 | AUC-ROC  |
|----------------|-----------|------------|--------|-----|----------|-----|
| **AraBERTv0.2 large**         | x | 0.69 | 0.74 | 0.73 | 0.77 | x |
| **DK AraBERTv0.2 large**      | x | 0.68 | 0.8 | 0.73 | 0.77 | x |
| **DK Gemma-3-4B**                | x | 0.66 | 0.59 | 0.62 | 0.60 | x |
| **DK Fanar-9B**                  | x | 0.68 | 0.68 | 0.68 | 0.68 | x |
---

## Observations

- **DK AraBERT** achives the highest overall performance.  
- Arabic models (**AraBERT** and **Fanar-9b**) outperformed multilingual (**Gemma-3-4b**).  
- **Gemma-3-4B** is the most unstable .

---

## Subject Classification Results

| Category | Support | Model | Accuracy | Precision | Recall | F1  | F2  | ROC-AUC |
|----------|---------|--------|-----------|------------|--------|-----|----------|-----|
| Depression  | 102  | AraBERTv0.2 large | x | 0.42 | 0.25 | 0.311 | 0.26 | x |
|             |      | DK AraBERTv0.2 large     | x | 0.50 | 0.44 | 0.46 | 0.45 | x |
|             |      | Fanar-9B     | x | 0.43 | 0.52 | 0.47 | 0.50 | x |
| Self Hurt   |  10  | DK AraBERTv0.2 | x | 0.18 | 0.2 | 0.19 | 0.19 | x |
|             |      | Fanar-9B     | x | 0.50 | 0.2 | 0.28 | 0.22 | x |
| Sexual Hurt |  15  | DK AraBERTv0.2 large | x | 0.59 | 0.73 | 0.65 | 0.94 | x |
|             |      | Fanar-9B     | x | 0.66 | 0.93 | 0.77 | 0.86 | x |

### Insights
- **Fanar** consistently surpasses **DK AraBERTv0.2** in both Recall and F1 across all subject prediction tasks.
- in sexual-hurt **Fanar** showed great recall score even though it is only 2% of the data.
- All models had trouble with depression prediction. 


---

*All results were computed using identical dataset splits and preprocessing pipelines, except sexual-hurt used different split duo to target distribution in train and test sets.  
Metrics represent binary-averaged values unless otherwise stated.*



