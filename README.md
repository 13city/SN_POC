# 📧 EmailSentiment: B2B Email Sentiment Analysis

## Overview 🌟
Welcome to **EmailSentiment**, a POC sentiment analysis tool designed specifically for B2B email communication. At the heart of EmailSentiment, we utilize the power of deep learning with PyTorch and the Hugging Face transformers library to decode the nuances of business correspondence.

The POC goes beyond mere word counting. It dives into the contextual understanding of email responses, accurately classifying them into sentiments that truly resonate with the human emotional spectrum: _Interested_, _Neutral_, or _Not Interested_.

## Features 🛠️
- **Deep Learning Powered**: Built on the robust PyTorch framework with the finesse of Hugging Face's transformer models.
- **Sentiment Detection**: Uses sophisticated NLP techniques to discern and categorize sentiments in emails.
- **Customized Responses**: Tailored to understand the subtleties of B2B interactions.
- **Logging and Monitoring**: Every action is logged meticulously for easy tracking and auditing.
- **Error Resilience**: Crafted with fault tolerance in mind, ensuring smooth operation amidst anomalies.
- **Test Email Generation**: Create your test dataset with realistic B2B email scenarios for model validation.

## Getting Started 🚀
### Prerequisites
- Python 3.x
- PyTorch, TorchVision, and Transformers

### Setting Up Your Environment 🌐
Clone the repository:
```sh
git clone https://github.com/your-github-username/emailsentiment.git
cd emailsentiment
```

Create and activate the virtual environment:
```sh
# Create virtual environment
python3 -m venv emailsentiment

# Activate Venv on macOS/Linux
source emailsentiment/bin/activate

# Activate Venv on Windows
.\emailsentiment\Scripts\activate
```

Install dependencies:
```sh
# With PyTorch, ensure you have the right CUDA version if needed
pip install transformers torch torchvision
```
_**Note:** PyTorch was chosen for its developer-friendly interface and dynamic computational graph. For those looking toward production-scale deployment, TensorFlow may offer additional benefits in terms of scalability and deployment options._

## Repository Structure 📁
- `sentiment.py`: The main script harnessing PyTorch and Hugging Face's transformers to perform sentiment analysis on provided email texts.
- `poc_data.py`: Generates a diverse set of test email content in predefined categories to facilitate thorough testing of the sentiment model.
- `unit_test_sentiment.py` & `unit_test_poc_data.py`: Rigorous unit tests to validate each functionality within the core scripts, ensuring reliability and stability.

## Scripts and Functions 📜
### `sentiment.py`
- `load_model()`: Initializes the sentiment analysis model from Hugging Face's transformers, setting the stage for the AI-powered sentiment classification.
- `normalize_text(text)`: Preprocesses email content, stripping it of URLs, email addresses, and special characters, preparing the text for analysis.
- `heuristic_check(content)`: Applies a set of heuristic rules to quickly identify clear indicators of sentiment without the need for deep analysis.
- `process_emails(directory, model)`: Orchestrates the reading of email files, text normalization, heuristic checks, and sentiment analysis, logging each step and outcome.

### `poc_data.py`
- `generate_email_content(category)`: Creatively crafts email bodies that mirror real-world B2B communication, enriching your dataset for each sentiment category.
- `handle_existing_directory()`: Empowers users with the choice to keep, add to, or replace existing test email datasets, ensuring flexibility and control.
- `create_test_emails()`: Generates and populates the test email directory with rich, diverse content that rigorously challenges the sentiment analysis model.

## Running the Tests 🧪
Execute the unit tests to validate the system's integrity:
```sh
python -m unittest unit_test_sentiment.py
python -m unittest unit_test_poc_data.py
```

## Contributing 👥
Your insights and code contributions are what make this community vibrant and remarkable. If you wish to contribute, feel free to fork the repository, make your changes, and submit a pull request!

## License 📄
This POC project is liberally licensed under the Biff Jam License. Feel free to use it as you see fit. Sharing is caring. 

## Questions or Feedback 📬
Have a question or feedback? Reach out to me through the support chat.

