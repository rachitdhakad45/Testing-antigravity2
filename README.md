# Bajaj Finserv Health Qualifier Round - API & SQL Integration

This repository contains the automation script and configuration files for the API and SQL Integration task as part of the Bajaj Finserv Health Qualifier round.

## Candidate Details
- **Name:** Rachit Dhakad
- **Registration Number:** 0827CS231205 (Ends in 5 - Odd)
- **Email:** rachitdhakad230998@acropolis.in

## Project Structure
- `app.py`: Standalone Python script that automatically generates a webhook URL, prints the assignment link, pauses for the SQL input, and submits it to the webhook.
- `requirements.txt`: Python package requirements.
- `README.md`: Setup and execution documentation.

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rachitdhakad45/Testing-antigravity2.git
   cd Testing-antigravity2
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Execution

Run the script using:
```bash
python app.py
```

The script will:
1. Submit your details to generate a unique webhook and access token.
2. Output the assignment link for Question 1.
3. Pause in the terminal and prompt you to input the solved SQL query.
4. Submit the query to the dynamic webhook and output the response.
