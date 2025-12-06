# 📊 Model Performance Comparison

This report summarizes the evaluation results of **Gemma-3-12B** LLM for the generation task, each experiement involved different approach of teaching the model to talk more the "Sahar" style. 

Metrics include **BERTScore**, **Perplexity**.

## Experiements

|#| Model                    | Description |
|-|--------------------------|-------|
|1|**Gemma-3-12B basic model**    |standard [Gemma-3-12B](https://huggingface.co/google/gemma-3-12b-it) without finetuning|
|2|**Gemma-3-12B 500 steps** | [Gemma-3-12B](https://huggingface.co/google/gemma-3-12b-it) but finetuned (causal LM) on the Sahar data for 500 steps|
|3|**Gemma-3-12B 2000 steps**        | [Gemma-3-12B](https://huggingface.co/google/gemma-3-12b-it) but finetuned (causal LM) on the Sahar data for 2000 steps|
|4|**Gemma-3-12B lexiocon as text**          | same as **Gemma-3-12B 2000 steps** but added 5 most relevant categories of the last user message (categories from lexicon) as a text in the prompt during training time|
|5|**Gemma-3-12B lexiocon as tokens**          | same as **Gemma-3-12B lexiocon as text** but expanded the vocabulary to include the categories in the lexicon.|
---

## Results Summary


| Model | BERTScore | Perplexity |
| :--- | :--- | :--- |
| **Gemma-3-12B basic model** | 0.6356 | 15571294.791 |
| **Finetuned Gemma3 (500 steps)** | 0.744 | 1191.629 |
| **Finetuned Gemma3 (2000 steps)** | 0.7534 | 1254.392 |
| **Gemma-3-12B lexiocon as text**  | 0.7523 | 1822.310 |
| **Gemma-3-12B lexiocon as tokens** | X | X |
---
