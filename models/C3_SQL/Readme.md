# C3-SQL
C3-SQL model is a ChatGPT-based zero-shot Text-to-SQL method. It is tested on the Spider dataset and is the state-of-the-art zero-shot Text-to-SQL method. Zero-shot learning means that the model can learn and understand the task the first time it is asked without giving any prior examples or fine-tuning it. C3 consists of three key components, Clear Prompting(CP), Calibration with Hints(CH), and Consistent Output(CO) which corresponds to the model input, model bias, and model output respectively. Because this is a zero-shot method, it uses approximately 1000 tokens per query. Clear Prompting corresponds to clean and effective input with precise instructions given to the model with two main parts: clear layout and clear context. Calibration with Hints provides some hints for the model biases to be resolved. Consistent Output overcomes the randomness and uncertainty of the output using a self-consistency method which is finding the unique right answer for multiple different paths, which would improve the reliability of the outputs produced. Overall, C3SQL provides a systematic approach for GPT-based Text-to-SQL search from the perspective of model input, bias, and output. The code to implement C3-SQL is taken from [1] and further modified to update dependencies. 

# Steps to run C3-SQL model:
- Download spider data from the website and the database and then unzip them and place it in folder called "data"
- Add your respective OpenAI API keys in _generate_sqls_by_gpt3.5.py, column_recall.py, table_recall.py files.
- Run the inference of the file with the command "bash run_c3sql.sh" and the "predicted_sql.txt" file will be ready.
- Other steps to run this model are given in C3_SQL.ipynb file.
- For more information on C3-SQL implementation, refer to [1].


# Reference
[1] bigbigwatermalon, “C3SQL,” GitHub repository, [Online]. Available: https://github.com/bigbigwatermalon/C3SQL/tree/master. [Accessed: Dec 12, 2023].

### Contributor: Sanika Vijaykumar Karwa


