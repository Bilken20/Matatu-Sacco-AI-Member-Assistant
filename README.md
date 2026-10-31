# Matatu SACCO AI Member Assistant

An AI-powered Python application that helps members of a Matatu SACCO in Thika, Kenya, get answers to common questions about membership, registration fees, outstanding balances and meetings.

The application uses the **Anthropic Python SDK** and Claude Haiku to generate responses.

## Features
- Answers common SACCO enquiries.
- Validates user input.
- Handles API errors.
- Uses environment variables to protect API credentials.

## Technologies
- Python
- Anthropic Claude API
- python-dotenv

## Setup and Installation

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Matatu_Sacco_Assistant
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install anthropic python-dotenv
```

**4. Configure your API key**

Create a `.env` file in the project directory:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

**5. Run the application**

```bash
python main.py
```

## Sample Questions
- What is the outstanding balance?
- How much is the registration fee?
- When is the next SACCO meeting?
- How can I verify my account balance?

## Important Note
The SACCO information currently used is demonstration data, not verified records. Individual member balances must be confirmed by the SACCO secretary.

## Future Improvements
- Database integration.
- Individual member account tracking.
- Payment history management.
- Graphical user interface.

