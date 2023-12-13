# CMPE-258-Team3 
### Ankita Arvind Deshmukh, Priyanka Birju Shah and Sanika Vijaykumar Karwa
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

This project's user interface (UI) is a Flask web application that converts natural language queries to SQL utilizing a variety of models. Users can enter their query, select from a variety of databases and models, and get the matching SQL conversion.

<img width="448" alt="UI" src="https://github.com/ankdeshm/CMPE-258-Team3/assets/101481678/803ca61e-054f-4d40-90fe-55ce191a220b">



## Comparison

The following table compares the execution accuracy and the exact match for 3 different models which are currently among the state-of-the art methods in the area of text-to-sql conversion. <br>

| Model    | Execution Accuracy w/o plugging| Execution Accuracy w/ plugging | Exact Match Accuracy w/o plugging | Exact Match Accuracy w/ plugging |
|----------|--------------------------------|--------------------------------|-----------------------------------|----------------------------------|
| C3-SQL   | 89.0%                          | 90.0%                          | 40.0%                             | 40.0%                            |
| DIN-SQL  | 93.7%                          | 95.2%                          | 63.5%                             | 63.5%                            |
| DAIL-SQL | 76.6%                          | 82.6%                          | 58.7%                             | 58.7%                            |


<p align="center">
  <img src="https://github.com/ankdeshm/CMPE-258-Team3/assets/101481678/75bda12e-f223-47a3-a05a-cc0318fad060" alt="First Image" width="500" style="margin-right: 10px;"/>
  <img src="https://github.com/ankdeshm/CMPE-258-Team3/assets/101481678/dfc97ac4-1902-4d24-b2cf-74837083b5c7" alt="Second Image" width="500"/>
</p>




## Conclusion
In this project, we conduct a comparative study of the different models for the task of text-to-SQL conversion. We started with baseline models like Seq2SQL and SQLNET and implemented those. Further, we implemented the top 3 models for the Spider dataset namely C3SQL, DINSQL, and DAILSQL. Additionally, we implemented some hugging-face models for this task which would perform the task of converting the models further. Although there were multiple challenges along the way, we powered through it all and attempted to perform the task of test-to-SQL conversion.  Lastly, we made a User Interface where all the models come together to provide the SQL query generation of the corresponding natural language query. 


