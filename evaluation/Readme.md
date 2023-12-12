# Evaluation for the LLM Models trained on Spider Dataset

The generative LLM models trained on the Spider dataset are evaluated using the official Spider evaluation tool provided in [7] and [12]. The models are evaluated based on (1) SQL Difficulty Level, (2) Matching with/without values plugged, (3) Partial and exact matching.  

1. SQL Difficulty Level: 
      First, the following SQL components are defined:
      1. SQL components 1: WHERE, GROUP BY, ORDER BY, LIMIT, JOIN, etc 
      
      2. SQL components 2: EXCEPT, UNION, INTERSECT, NESTED
      
      3. Others
2. Then, the SQL difficulty level is determined by the following criteria: 
      1. Easy : 
      If SQL keywords have less than or equal to one component from [SQL components 1] and none from SQL components 2 and Others
      
      2. Medium : 
      If the SQL satisfies no more than two rules in Others, up to one component from SQL components 1, and none in SQL components 2
      
      3. Hard : 
      If the SQL satisfies more than two rules in Others, up to two components from SQL components 1, and up to 1 component in SQL components 2
      
      4.. Extra Hard : 
      All the SQLs left 
3. Value String:
      1. Not Provided- The model is expected to generate a value prediction for the value string and is evaluated on the accuracy of the predicted value string as well as the SQL query accuracy.
      
      2. Provided- The model is not expected to generate a value prediction for the value string and instead a list of gold values for each question is provided. This evaluates the accuracy of just the SQL query structure as opposed to the generated value string.
4. Matching Accuracy:
    1. Exact Match Accuracy - The exact-set match accuracy measures the matched SQL keywords between the ground truth and its corresponding predicted SQL query. This would give less accuracy even if one of the parts of the SQL query is wrong/missing as it measures the exactness of the ground truth. 
    
    2. Execution Accuracy - The execution accuracy compares the execution output of the predicted SQL query with the ground truth SQL query on some database instances. This is a more precise metric to measure the performance because there could be multiple possible SQL queries for a single natural language question. 



# Steps to run eval:
1. Run evaluation.py
``` python evaluation.py --gold gold.txt --pred [predicted_file] --etype all --db [path to spider database] --table tables.json  --progress_bar_for_each_datapoint ```

For example:
To run the DAIL evaluation, use: 

```python evaluation.py --gold gold.txt --pred dail_predicted.txt --etype all --db [path to spider database] --table tables.json  --progress_bar_for_each_datapoint```

To provide value strings, use --plug_value 

```python evaluation.py --gold gold.txt --pred dail_predicted.txt --etype all --db [path to spider database] --table tables.json  --progress_bar_for_each_datapoint --plug_value```


# References
[1]T. Yu, “Semantic Evaluation for Text-to-SQL with Test Suites,” GitHub, Dec. 12, 2023. https://github.com/taoyds/test-suite-sql-eval/tree/master (accessed Dec. 12, 2023).
‌

### Contributor: Priyanka Birju Shah

