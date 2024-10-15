# Text Summarization using Machine Learning #
 
This project aims to create a simple text summarization tool using machine learning techniques and popular Python libraries such as spaCy, heapq, and string. The project also includes a web interface built with the Flask framework, allowing users to easily input text and get summarized content.

## Features ##

- **Text Summarization:** Extractive summarization technique is used to pick the most important sentences from the original text.
- **Web Interface:** A user-friendly web interface is provided using the Flask framework for easy interaction with the summarization tool.
- **Customizable Settings:** The summarization ratio can be adjusted based on user preferences.

## Libraries and Frameworks Used ##
- **spaCy:** For natural language processing tasks such as tokenization, lemmatization, and sentence parsing.
- **heapq:** Used to extract the most important sentences based on the computed sentence scores.
- **string:** To handle text pre-processing tasks such as punctuation removal.
- **STOP_WORDS:** To remove common stop words from the text for better summarization.
- **Flask:** A lightweight web framework used to create the web interface for the summarization tool.

## Installation ##
1. Clone the repository:
   ```bash
    git clone https://github.com/prathmesh193/text-summarization-using-ml.git
3. Navigate to the project directory:
   ```bash
    cd text-summarization-using-ml
4. Install the required dependencies:
   ```bash
    pip install -r requirements.txt
   
The requirements.txt file should contain:
```
    - spacy
    - flask
    - stop_words
```
Additionally, make sure to download the necessary spaCy language model:
```python -m spacy download en_core_web_sm```

## Usage ##
1. Run the Flask web application:
2.     python app.py
3. Open your web browser and go to http://127.0.0.1:5000/ to access the text summarization tool.
4. Input your text into the provided text box and specify the summarization ratio.
5. Click the 'Summarize' button to get the summarized text.

## Project Structure  ##
- **app.py:** The main Flask application file.
- **summarizer.py:** Contains the logic for text summarization, including functions for text processing, scoring sentences, and generating the summary.
- **templates/:** Contains HTML templates for the web interface.
- **static/:** Contains any static files such as CSS for the web interface.
- **requirements.txt:** List of dependencies for the project.

## How it Works ##
1) **Text Preprocessing:** The input text is processed using spaCy to remove stop words, punctuation, and perform tokenization.
2) **Sentence Scoring:** Sentences are scored based on the occurrence of important words.
3) **Sentence Selection:** The most important sentences are selected using heapq to form the final summary.
4) **Display Result:** The summarized text is displayed on the web interface.

## Customization ##
You can adjust the summarization ratio in the web interface to control the length of the generated summary. Additionally, you can modify the summarizer.py file to implement different summarization algorithms or incorporate advanced techniques such as TF-IDF weighting.

## Contributing ##
Feel free to contribute to this project by submitting issues, feature requests, or pull requests. Any contributions are highly appreciated!

License
    This project is licensed under the MIT License.
