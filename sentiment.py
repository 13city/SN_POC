import os
import glob
import logging
import re
from transformers import pipeline

# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Setup logging
logging_directory = "logs"
if not os.path.exists(logging_directory):
    os.makedirs(logging_directory)
logging.basicConfig(filename=f'{logging_directory}/analysis.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_model():
    """
    Loads the sentiment analysis model.
    Uses the 'distilbert-base-uncased-finetuned-sst-2-english' model for sentiment analysis.
    """
    try:
        model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        logging.info("Sentiment analysis model loaded successfully.")
        return model
    except Exception as e:
        logging.error(f"Error loading model: {e}", exc_info=True)
        raise

def normalize_text(text):
    """
    Normalizes the text by removing or standardizing special characters, URLs, and email addresses.
    Also, removes common email signatures and disclaimers.
    """
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'\S*@\S*\s?', '', text)
    text = re.sub(r'[^A-Za-z0-9]+', ' ', text)
    common_signatures = ["regards", "cheers", "sincerely", "thanks", "thank you"]
    for signature in common_signatures:
        text = re.split(signature, text, flags=re.IGNORECASE)[0]
    return text.strip()

def heuristic_check(content):
    """
    Checks for specific phrases that strongly indicate interest, disinterest, or neutrality.
    Skips sentiment analysis if a strong indicator is found.
    """
    not_interested_phrases = ["not interested", "unsubscribe", "stop emailing", "no thanks", "no"]
    interested_phrases = ["sounds great", "tell me more", "very interested", "let's meet", "interested"]
    neutral_phrases = [
        "I'll think about it", "I'll review", "maybe later", 
        "currently reviewing", "will consider", "will look into it",
        "need more time", "undecided", "not sure", "possibly"
    ]

    for phrase in not_interested_phrases:
        if phrase in content.lower():
            return "not interested"
    for phrase in interested_phrases:
        if phrase in content.lower():
            return "interested"
    for phrase in neutral_phrases:
        if phrase in content.lower():
            return "neutral"
    return None

def process_emails(directory, model):
    """
    Processes each email in the given directory.
    Applies text normalization and heuristic checks before sentiment analysis.
    """
    try:
        email_files = glob.glob(os.path.join(directory, '*.txt'))
        logging.info(f"Found {len(email_files)} email files in {directory}")

        # Adjust these thresholds as needed
        interested_threshold = 0.7
        not_interested_threshold = 0.3

        for filepath in email_files:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                logging.info(f"Processing file {filepath} with content: {content[:100]}")

                normalized_content = normalize_text(content)
                heuristic_result = heuristic_check(normalized_content)
                if heuristic_result:
                    logging.info(f"Heuristic applied for {filepath}: {heuristic_result}")
                    color = RED if heuristic_result == "not interested" else GREEN if heuristic_result == "interested" else BLUE
                    print(f"{color}{filepath}: {heuristic_result} (Heuristic){RESET}")
                    continue

                try:
                    result = model(normalized_content)[0]
                    score = result['score']
                    label = "interested" if score > interested_threshold else "not interested" if score < not_interested_threshold else "neutral"
                    color = GREEN if label == "interested" else RED if label == "not interested" else BLUE
                    logging.info(f"Processed {filepath}: {label} ({score})")
                    print(f"{color}{filepath}: {label} ({score}){RESET}")

                    # Debugging: log the score and content for review
                    logging.debug(f"Email: {filepath}, Score: {score}, Content: {normalized_content[:100]}")

                except Exception as e:
                    logging.error(f"Error in sentiment analysis for {filepath}: {e}", exc_info=True)

    except Exception as e:
        logging.error(f"Error processing emails: {e}", exc_info=True)
        raise

def main():
    model = load_model()
    email_directory = "test_emails"
    process_emails(email_directory, model)

if __name__ == "__main__":
    main()
