# DAIL-SQL
Currently, DAIL-SQL stands as one of the most advanced methods in the field of translating text to SQL. It thoroughly evaluates and tests various existing techniques of prompt engineering and determines the most effective method for question representation, as well as the selection and arrangement of examples. The approach to representing questions is zero-shot, whereas the strategies for selecting and organizing examples are few-shot. For the representation of questions, it identifies examples by considering information from both the question and its corresponding query, arranging them in a way that maintains the association between the question and its SQL translation. In the process of selecting examples, the method involves picking the best 𝑘 examples, showcasing their questions and queries within a Code Representation Prompt. This prompt is then input into a large-scale language model to forecast the SQL query. Subsequently, the Jaccard similarity index is employed to evaluate the resemblance between the example candidates and the predicted query based on their query similarity. Furthermore, DAIL-SQL introduces a refined solution to the issue of token efficiency, a common challenge in other large language model-based approaches. The code to implement DAIL-SQL is taken from [1] and modified to update the dependecies and paths.

# Steps to run the DAIL-SQL model:
- Create a folders named "dataset" and "third_party" where the folder DAIL-SQL_Main is present
- Download core NLP package and place it inside third_party folder
- Download and place the Spider dataset inside dataset_folder
- Other steps to run DAIL-SQL are given in DAIL_SQL.ipynb
- Refer to [1] for more information on DAIL-SQL implementation


# References
[1] BeachWang, “Beachwang/Dail-SQL: A efficient and effective few-shot NL2SQL method on GPT-4.,” GitHub, https://github.com/BeachWang/DAIL-SQL (accessed Dec. 11, 2023). 

### Contributor: Ankita Arvind Deshmukh
