from flask import Flask, render_template, request
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModelForSeq2SeqLM


app = Flask(__name__)


def find_answer_for_question(input_question, filename):
    # Read questions file and store lines
    with open('questions.txt', 'r') as file:
        questions = [line.strip() for line in file.readlines()]

    # Try to find the question
    try:
        index = questions.index(input_question)
    except ValueError:
        return "Question not found"

    # Read answers file and store lines
    with open(filename, 'r') as file:
        answers = [line.strip() for line in file.readlines()]

    # Retrieve the answer using the found index
    if index < len(answers):
        answer = answers[index]
        return answer
    else:
        return "Answer not found"


def generate_c3(user_input):
    output = find_answer_for_question(user_input, "C3_predicted.txt")
    return output

def generate_DIN_SQL(user_input):
    output = find_answer_for_question(user_input, "DIN_predicted.txt")
    return output

def generate_DAIL_SQL(user_input):
    output = find_answer_for_question(user_input, "DAIL_predicted.txt")
    return output

def generate_T5_LM_spider(user_input):
    model_path = 'gaussalgo/T5-LM-Large-text2sql-spider'
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    # question = "What is the average, minimum, and maximum age for all French musicians?"

    # schema = """
    #    "stadium" "Stadium_ID" int , "Location" text , "Name" text , "Capacity" int , "Highest" int , "Lowest" int , "Average" int , foreign_key:  primary key: "Stadium_ID" [SEP] "singer" "Singer_ID" int , "Name" text , "Country" text , "Song_Name" text , "Song_release_year" text , "Age" int , "Is_male" bool , foreign_key:  primary key: "Singer_ID" [SEP] "concert" "concert_ID" int , "concert_Name" text , "Theme" text , "Year" text , foreign_key: "Stadium_ID" text from "stadium" "Stadium_ID" , primary key: "concert_ID" [SEP] "singer_in_concert"  foreign_key: "concert_ID" int from "concert" "concert_ID" , "Singer_ID" text from "singer" "Singer_ID" , primary key: "concert_ID" "Singer_ID"
    # """

    question = user_input
    schema = """
        "head" "age" int
    """

    input_text = " ".join(["Question: ",question, "Schema:", schema])

    model_inputs = tokenizer(input_text, return_tensors="pt")

    # Generate outputs
    outputs = model.generate(**model_inputs, max_length=512)

    # Check and flatten the outputs if necessary
    if isinstance(outputs, torch.Tensor):
        outputs = outputs.tolist()

    if any(isinstance(i, list) for i in outputs):
        # Flatten the list if it's a list of lists
        outputs = [item for sublist in outputs for item in sublist]

    # Decode the outputs
    output_text = tokenizer.decode(outputs, skip_special_tokens=True)
    output = output_text.replace("-", "SELECT")
    
    return output



def generate_gpt2Medium_text_to_sql(user_input):
    # Load your model and tokenizer
    finetunedGPT = GPT2LMHeadModel.from_pretrained("rakeshkiriyath/gpt2Medium_text_to_sql")
    finetunedTokenizer = GPT2Tokenizer.from_pretrained("rakeshkiriyath/gpt2Medium_text_to_sql")

    def generate_text_to_sql_gpt2Medium_text_to_sql(query, model, tokenizer, max_length=256):
        prompt = f"Translate the following English question to SQL: {query}"
        input_tensor = tokenizer.encode(prompt, return_tensors='pt')
        output = model.generate(input_tensor, max_length=max_length, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
        decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)
        sql_output = decoded_output[len(prompt):].strip()
        return sql_output
    return generate_text_to_sql_gpt2Medium_text_to_sql(user_input, finetunedGPT, finetunedTokenizer)

def generate_t5_small(user_input):
    # Initialize the tokenizer from Hugging Face Transformers library
    tokenizer = T5Tokenizer.from_pretrained('t5-small')

    # Load the model
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = T5ForConditionalGeneration.from_pretrained('cssupport/t5-small-awesome-text-to-sql')
    model = model.to(device)
    model.eval()

    def generate_sql(input_prompt):
        # Tokenize the input prompt
        inputs = tokenizer(input_prompt, padding=True, truncation=True, return_tensors="pt").to(device)

        # Forward pass
        with torch.no_grad():
            outputs = model.generate(**inputs, max_length=512)

        # Decode the output IDs to a string (SQL query in this case)
        generated_sql = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return generated_sql

    input_prompt = "tables:\n" + "CREATE TABLE head (age INTEGER)" + "\n" + "query for:" + user_input

    generated_sql = generate_sql(input_prompt)

    return generated_sql



def generate_toy_sql(user_input):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = AutoModelForCausalLM.from_pretrained("Artifact-io/toy-sql-28M").to(device)
    tokenizer = AutoTokenizer.from_pretrained("Artifact-io/toy-sql-28M")

    inputs = tokenizer([
        f"""CREATE TABLE head (age INTEGER)
        {user_input}
        """
      ],
      return_tensors="pt",
    ).to(device)
    outputs = model.generate(**inputs, max_new_tokens=200, do_sample=True, top_k=50, top_p=0.95)
    text = tokenizer.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)[0].split("---")[0]

    return text



@app.route('/', methods=['GET', 'POST'])
def index():
    database_options = ['Spider', 'Sql-create-context']
    model_options = {
        'Spider': ['C3-SQL', 'DIN-SQL', 'DAIL-SQL', 'T5-LM-Large-text2sql-spider'],
        'Sql-create-context': ['gpt2Medium_text_to_sql', 't5-small', 'toy-sql-28M']
    }
    model_details = {
    'C3-SQL': {'name': 'C3-SQL', 'architecture': 'C3 Model Architecture', 'accuracy': '80%'},
    'DIN-SQL': {'name': 'DIN-SQL', 'architecture': 'DIN SQL Architecture', 'accuracy': '93%'},
    'DAIL-SQL': {'name': 'DAIL-SQL', 'architecture': 'DAIL SQL Architecture', 'accuracy': '76%'},
    'T5-LM-Large-text2sql-spider': {'name': 'T5-LM-Large-text2sql-spider', 'architecture': 'T5 Large Model', 'accuracy': '60%'},
    'gpt2Medium_text_to_sql': {'name': 'gpt2Medium_text_to_sql', 'architecture': 'GPT-2 Medium', 'accuracy': '67%'},
    't5-small': {'name': 't5-small', 'architecture': 'T5 Small', 'accuracy': '40%'},
    'toy-sql-28M': {'name': 'toy-sql-28M', 'architecture': 'Toy SQL 28M', 'accuracy': '20%'},
    # Add other models as needed
}

    
    selected_database = request.form.get('database') if request.method == 'POST' else 'Spider'
    models_to_display = model_options[selected_database]
    
    model_output = ""
    user_input = ""
    model_detail = ""
    selected_model = ""
    if request.method == 'POST':
        user_input = request.form['text']
        selected_model = request.form.get('model')
        # Only run the model if the selected one is 'gpt2Medium_text_to_sql'

        if 'generate_button' in request.form:
            if selected_model == 'toy-sql-28M':
                model_output = generate_toy_sql(user_input)
            if selected_model == 'gpt2Medium_text_to_sql':
                model_output = generate_gpt2Medium_text_to_sql(user_input)
            if selected_model == 't5-small':
                model_output = generate_t5_small(user_input)
            if selected_model == 'T5-LM-Large-text2sql-spider':
                model_output = generate_T5_LM_spider(user_input)
            if selected_model == 'C3-SQL':
                model_output = generate_c3(user_input)
            if selected_model == 'DIN-SQL':
                model_output = generate_DIN_SQL(user_input)
            if selected_model == 'DAIL-SQL':
                model_output = generate_DAIL_SQL(user_input)
    
    model_detail = model_details.get(selected_model, {'architecture': 'N/A', 'accuracy': 'N/A'})
    return render_template('index.html',
                           database_options=database_options,
                           selected_database=selected_database,
                           models_to_display=models_to_display,
                           user_input=user_input,
                           model_output=model_output,
                          model_detail=model_detail
                           )



if __name__ == '__main__':
    app.run(debug=True)

