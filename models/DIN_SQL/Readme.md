# DIN-SQL

The paper "DIN-SQL: Decomposed In-Context Learning of Text-to-SQL with Self-Correction" [5] presents a technique to enhance the capacity of Large Language Models (LLMs) to produce SQL queries from natural language. With this method, difficult Text-to-SQL jobs are broken down into easier subtasks, and the final query is built using the solutions to those subtasks. This method demonstrated state-of-the-art performance on the Spider dataset when evaluated with GPT-4. It consists of four modules that improve the robustness and accuracy of the created SQL queries: self-correction, SQL generation, query categorization and decomposition, and schema linkage.

1. Schema Linking: The first module in the DIN-SQL model, schema linking, is essential for connecting certain sections of a database schema to natural language queries. It significantly simplifies creating complex queries and adjusting to various domains. The Large Language Model's (LLM) highest error rate is seen in this module. Ten arbitrary samples from the Spider dataset are used in a prompt-based, chain-of-thought technique for schema linking. In addition to collecting potential entities and values from the query, this method includes identifying column names and matching tables.

2. Classification and Decomposition: Complex queries and join operations are addressed in DIN-SQL's second module, Classification & Decomposition. It divides queries into three categories: non-nested complex (needs joins but no sub-queries), nested complex (needs joins, sub-queries, and set operations), and easy (single-table, no joins or nesting). Additionally, the module finds sub-queries for nested queries and determines which tables need to be combined. Each query class has a different set of prompts, which helps with precise query formulation. The paper provides an example of the input and output of the module.

3. SQL Generation: DIN-SQL's SQL Generation Module handles the challenge of translating natural language queries into SQL. For the three query classes—easy, non-nested complex, and nested complex—it employs several strategies. It uses simple prompting for simple requests. In non-nested complicated queries, join operations are handled using an intermediate representation such as NatSQL. The most complex inquiries are nested complex queries, which involve solving sub-queries prior to the final SQL generation. To close the gap between natural language and SQL, each class makes use of particular formats and prompts.

4. Self-Correction: Lastly, the self-correction module is designed to fix little mistakes in SQL queries that are produced by LLMs, such as duplicate or missing terms. Errors are corrected by the model in a zero-shot scenario, which eliminates the need for further examples. The model is asked to find and fix faults using two different kinds of prompts: a generic question that asks the model directly, and a soft prompt that gently advises looking for possible problems without assuming the query is flawed.



# Steps to run the DIN-SQL model:
1. Download the Spider Dataset from here: https://drive.google.com/u/0/uc?id=1iRDVHLr4mX2wQKSgA9J8Pire73Jahh0m&export=download and place it in /data/.
2. Copy dev.json and tables.json into /data/ as well.
3. Add your OPENAI API key in DIN-SQL.py
4. Environment set up:

  ```python -m venv din_env```
  
  ```source ./din_env/bin/activate```

  ```pip install -r requirements.txt```

5. Run DIN-SQL.py

  ```python DIN-SQL.py --dataset ./data/ --output predicted_sql.txt```


# References
[1]M. Pourreza, “Few-shot-NL2SQL-with-prompting,” GitHub, Dec. 11, 2023. https://github.com/MohammadrezaPourreza/Few-shot-NL2SQL-with-prompting/tree/main (accessed Dec. 12, 2023).
‌

### Contributor: Priyanka Birju Shah

