# CMPE-258-Team3
# Text to SQL Conversion

## Application Area: Natural Language Processing

The primary objective of this project is to identify and finetune various existing approaches for Text-to-SQL conversion which accurately convert user-input natural language questions into corresponding SQL queries. This involves understanding the nuances of natural language, recognizing intent and context, and translating these into structured query language format. The project aims to make this translation as seamless and accurate as possible, catering to a wide range of queries from simple to complex. In order to determine which models work better, we intend to compare the performance of all the existing approaches.

## Datasets:
Various datasets are used for training/finetuning/inference. These datasets can be found below:
- WikiSQL: Available at https://github.com/salesforce/WikiSQL
- Spider: Available at https://github.com/taoyds/spider
- sql-create-context: Available at https://huggingface.co/datasets/b-mc2/sql-create-context

## Models
We experimented with the following models for out text-to-sql conversion project. Seq2SQl and SQLNet served as our baselines. All the models mentioned below use one of the datasets metioned above for the training purpose. The steps to run these models and the current implementation of these approaches can be found at their respective folders inside /models in this repo. <br>

- Baseline Models
  - Seq2SQL
  - SQLNet
- C3-SQL
- DIN-SQL
- DAIL-SQL
- Transformer-based models from Hugging face
  - gpt2Medium_text_to_sql
  - t5-small-awesome-text-to-sql
  - Mistral-7B-SQL
  - CodeLlama-7b-Instruct-SQL
  - CodeLlama-13b-Instruct-SQL
  - squeal
  - T5-LM-Large-text2sql-spider

## Results

The following tables compares the execution accuracy and the exact match for 3 different models which are currently among the state-of-the art methods in the area of text-to-sql conversion. <br>

| Model    | Execution Accuracy w/o plugging| Execution Accuracy w/ plugging | Exact Match Accuracy w/o plugging | Exact Match Accuracy w/ plugging |
|----------|--------------------------------|--------------------------------|-----------------------------------|----------------------------------|
| C3-SQL   | 89.0%                          | 90.0%                          | 40.0%                             | 40.0%                            |
| DIN-SQL  | 93.7%                          | 95.2%                          | 63.5%                             | 63.5%                            |
| DAIL-SQL | 76.6%                          | 82.6%                          | 58.7%                             | 58.7%                            |


![WhatsApp Image 2023-12-11 at 9 53 01 PM (1)](https://github.com/ankdeshm/CMPE-258-Team3/assets/101481678/75bda12e-f223-47a3-a05a-cc0318fad060)



## Comparison

## Conclusion


