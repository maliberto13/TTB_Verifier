# TTB Label Verifier
Link: (ttb-verifier.fly.dev)

This repository contains a Django-based web application designed to verify text on alcohol labels against user-provided data. The system uses Optical Character Recognition (OCR) to extract text from an uploaded label image and compares it to the submitted form data, providing a detailed breakdown of matches and mismatches. It is styled after the requirements for TTB (Alcohol and Tobacco Tax and Trade Bureau) label verification.

## Key Features

*   **Web-Based Interface:** A simple web form to input label data and upload an image. (ttb-verifier.fly.dev)
*   **OCR Text Extraction:** Uses `Pytesseract` to read and extract text from the label image.
*   **Intelligent Text Comparison:** Employs `fuzzywuzzy` and `nltk` for fuzzy string matching to robustly compare the expected text with the OCR output, accounting for minor OCR errors.
*   **Field-Specific Verification:** Performs individual checks for:
    *   Brand Name
    *   Class/Type
    *   Alcohol by Volume (ABV) with a tolerance
    *   Net Contents
    *   Presence of the Government Warning
*   **Detailed Results:** Displays a clear pass/fail summary, a field-by-field comparison, the raw OCR text, and a preview of the uploaded image.

## How It Works

1.  **User Input:** The user fills out a form with required label information (Brand Name, ABV, etc.) and uploads an image of the product label.
2.  **Image Processing:** The uploaded image is preprocessed using the Pillow library (converted to grayscale and autocontrasted) to improve OCR accuracy.
3.  **OCR Extraction:** `pytesseract` scans the processed image and extracts all readable text.
4.  **Comparison Logic:** The core comparison logic in `compare_utils.py` is executed:
    *   For text fields like Brand Name, it uses `fuzzywuzzy.token_sort_ratio` on n-grams of the OCR text to find the best match for the user's input.
    *   For ABV, it uses regular expressions to find percentage values in the OCR text and checks if any fall within a defined tolerance (`0.3%`) of the expected value.
5.  **Result Display:** The application renders a results page that clearly indicates which fields match, which do not, and what text (if any) was found on the label for each field.

## Getting Started

### Prerequisites

*   Python 3.x
*   pip
*   **Tesseract OCR Engine:** This is a system dependency, not a Python package. You must install it on your operating system and ensure the `tesseract` command is available in your system's PATH.
    *   **macOS (via Homebrew):** `brew install tesseract`
    *   **Ubuntu/Debian:** `sudo apt-get install tesseract-ocr`
    *   **Windows:** Download and run the installer from the [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) page.

### Installation on MacOS

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/maliberto13/ttb_verifier.git
    cd ttb_verifier
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```

3.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6.  Open your web browser and navigate to `http://127.0.0.1:8000/` to use the application.

## Usage

1.  Navigate to the application's home page.
2.  Fill in the form fields with the _exact_ data you expect to find on the label.
3.  Click "Choose File" to select and upload a clear image of the label.
4.  Press the "Verify Label" button.
5.  The next page will display the verification results, including an overall pass/fail status and a detailed breakdown for each field. Tips for improving accuracy and a quick report of discrepancies are also provided.
6.  To quickly go back to the previous form, use the Back Button in your browser.
7.  To start a new form, use the "Verify Another Label" button.

## Project Structure

```
├── labelverifier/        # Django project settings and configuration
├── verifier/             # Main Django application for verification logic
│   ├── compare_utils.py  # Fuzzy matching and comparison functions
│   ├── forms.py          # The label submission form definition
│   ├── models.py         # Database model for a Verification record
│   ├── ocr_utils.py      # Image preprocessing and OCR text extraction
│   ├── views.py          # Main view handling form submission, OCR, and results
│   ├── templates/        # HTML templates for the UI
│   │   ├── verifier/
│   │       ├── base.html
│   │       ├── result.html
│   │       └── upload_form.html
│   └── urls.py           # URL routing for the verifier app
├── manage.py             # Django's command-line utility
└── requirements.txt      # Python dependencies
