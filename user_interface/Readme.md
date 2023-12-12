# UI

This project's user interface (UI) is a Flask web application that converts natural language queries to SQL utilizing a variety of models. Users can enter their query, select from a variety of databases and models, and get the matching SQL conversion as shown in Fig. 10 below. Hugging Face's Transformers library is integrated into the backend for model implementations, and it manages query processing and model selection. The application offers comprehensive model information, including architecture and correctness, and is both interactive and user-friendly. Flask's rendering system handles the front-end design with the help of HTML templates.This user interface can be accessed via http://127.0.0.1:5000/ or on a local server, localhost. This approach ensures data privacy and quick response times, as processing happens on the local machine.

In the UI for the GPT-based models like C3, DIN-SQL, and DAIL-SQL, the application does not dynamically generate SQL queries in real-time. Instead, it displays pre-generated predictions from a predetermined text file. When a user inputs a query, the system searches these files for a corresponding answer rather than using the models to generate a new response on the fly. This approach simplifies the backend processing but limits the output to pre-existing examples covered in the text files

<img width="874" alt="Screenshot 2023-12-12 at 11 38 11 AM" src="https://github.com/ankdeshm/Text-to-SQL/assets/145494439/24317d46-c383-44ea-b5c1-fa359092f645">



# Steps to run the UI:
1. Environment set up:

  ```python -m venv ui_env```
  
  ```source ./ui_env/bin/activate```

  ```pip install flask```
  
  ```pip install transformer```
  
  ```pip install sentencepiece```



2. Run app.py.py

  ```python app.py```


  
3. Open http://127.0.0.1:5000/ in a browser 




### Contributor: Priyanka Birju Shah
