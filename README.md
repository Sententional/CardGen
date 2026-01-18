# 💳 CardGen - Fake Credit Card Generator

**A powerful Python CLI tool for generating valid test credit card numbers for development and testing purposes.**

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: Clean](https://img.shields.io/badge/code%20style-clean-brightgreen.svg)](https://github.com/Sententional/fake-card-generator)

## ⚠️ Legal Disclaimer

**FOR TESTING AND DEVELOPMENT PURPOSES ONLY**

This tool generates mathematically valid but completely fictitious credit card numbers using the Luhn algorithm. These cards:

- ❌ Will **NOT** work for actual purchases or transactions
- ❌ Cannot be used to make real payments
- ✅ Are designed for form validation, UI testing, and development
- ⚖️ Using these for fraud is **illegal** and can be prosecuted

---

## 🚀 Features

- 🎯 **6 Card Types** - Visa, Mastercard, Amex, Discover, JCB, Diners Club
- ✅ **Valid Luhn Checksums** - All generated cards pass validation
- 📊 **Multiple Output Formats** - Text, JSON, CSV, Table
- 🔍 **Card Validator** - Check if a card number is valid
- 🎲 **Batch Generation** - Generate hundreds of cards at once
- 👤 **Realistic Data** - Random cardholder names and expiry dates
- 💻 **Zero Dependencies** - Pure Python standard library
- 🎨 **Clean CLI** - Intuitive command-line interface

---

## Requirements
- Python 3.6 or higher
- No external dependencies required!

---

## 📖 Usage

### Basic Commands

```bash
# Generate a random card
python card_generator.py

# Generate a specific card type
python card_generator.py -t visa

# Generate multiple cards
python card_generator.py -n 10

# Generate with specific format
python card_generator.py -f json

# Validate a card number
python card_generator.py --validate 4532015112345678

# List all available card types
python card_generator.py --list-types
```

### Command-Line Options

```
Options:
  -h, --help            Show help message and exit
  -t, --type TYPE       Card type: visa, mastercard, amex, discover, jcb, diners
  -n, --number N        Number of cards to generate (default: 1)
  -f, --format FORMAT   Output format: text, json, csv, table (default: text)
  --validate NUMBER     Validate a card number using Luhn algorithm
  --list-types          List all available card types
```

---

## 💡 Examples

### Generate Different Card Types

```bash
# Visa card
$ python card_generator.py -t visa
Visa
Number:     4532 0151 1234 5678
Cardholder: JOHN SMITH
Expiry:     08/27
CVV:        123

# American Express
$ python card_generator.py -t amex
American Express
Number:     3714 496353 98431
Cardholder: SARAH JOHNSON
Expiry:     03/28
CVV:        4567

# Mastercard
$ python card_generator.py -t mastercard
Mastercard
Number:     5425 2334 3010 9903
Cardholder: MICHAEL GARCIA
Expiry:     11/26
CVV:        837
```

### Batch Generation

```bash
# Generate 5 random cards
python card_generator.py -n 5

# Generate 10 Visa cards
python card_generator.py -t visa -n 10

# Generate 100 cards of mixed types
python card_generator.py -n 100
```

### JSON Output

Perfect for automated testing and API mocking:

```bash
$ python card_generator.py -t mastercard -f json
[
  {
    "card_type": "Mastercard",
    "card_number": "5425233430109903",
    "card_number_formatted": "5425 2334 3010 9903",
    "cvv": "837",
    "expiry_month": "11",
    "expiry_year": "28",
    "expiry_year_full": "2028",
    "expiry_date": "11/28",
    "cardholder_name": "SARAH JOHNSON"
  }
]
```

### CSV Export

Great for importing into spreadsheets or databases:

```bash
# Export to CSV file
python card_generator.py -n 100 -f csv > test_cards.csv

# Generate specific card types
python card_generator.py -t visa -n 50 -f csv > visa_cards.csv
```

### Table Format

Clean, readable output for documentation:

```bash
$ python card_generator.py -n 2 -f table
==================================================
Card Type:    Visa
Card Number:  4532 0151 1234 5678
Cardholder:   JOHN SMITH
Expiry Date:  08/27
CVV:          123
==================================================
==================================================
Card Type:    Mastercard
Card Number:  5425 2334 3010 9903
Cardholder:   SARAH JOHNSON
Expiry Date:  11/28
CVV:          837
==================================================
```

### Card Validation

Verify if a card number has a valid checksum:

```bash
$ python card_generator.py --validate 4532015112345678
Card number: 4532015112345678
Valid: ✓ YES

$ python card_generator.py --validate 1234567890123456
Card number: 1234567890123456
Valid: ✗ NO
```

---

## 🎯 Use Cases

### 1. Form Validation Testing

Test credit card input fields without using real data:

```bash
python card_generator.py -n 20 -f json > test_data.json
```

### 2. Payment UI Development

Preview how different card types display in your interface:

```bash
# Test all card types
for type in visa mastercard amex discover jcb diners; do
    python card_generator.py -t $type
done
```

### 3. Automated Testing & CI/CD

Generate test fixtures for your test suite:

```bash
# Create test fixtures
python card_generator.py -n 100 -f csv > tests/fixtures/cards.csv
```

### 4. Database Seeding

Populate development databases with test data:

```python
import subprocess
import json

# Generate cards
result = subprocess.run(
    ['python', 'card_generator.py', '-n', '1000', '-f', 'json'],
    capture_output=True,
    text=True
)

cards = json.loads(result.stdout)
# Insert into your database
```

### 5. API Mocking

Create realistic test data for payment API mocks:

```bash
python card_generator.py -n 50 -f json > mock_data/cards.json
```

---

## 📋 Supported Card Types

| Card Type            | Length | CVV | Prefix    | Example               |
|----------------------|--------|-----|-----------|-----------------------|
| **Visa**             | 16     | 3   | 4         | `4532 0151 1234 5678` |
| **Mastercard**       | 16     | 3   | 51-55     | `5425 2334 3010 9903` |
| **American Express** | 15     | 4   | 34, 37    | `3714 496353 98431`   |
| **Discover**         | 16     | 3   | 6011      | `6011 1111 1111 1117` |
| **JCB**              | 16     | 3   | 3528-3589 | `3528 0000 0000 0000` |
| **Diners Club**      | 14     | 3   | 36, 38    | `3600 666633 3344`    |

---

## 🧮 How It Works

### The Luhn Algorithm

This generator uses the **Luhn algorithm** (also known as "modulus 10" or "mod 10"), invented by IBM scientist Hans Peter Luhn in 1954. It's the industry-standard checksum formula for validating credit card numbers.

#### Algorithm Steps:

1. **Start from the right** - Begin with the rightmost digit (excluding the check digit)
2. **Double every second digit** - Moving left, double every second digit
3. **Subtract 9 if needed** - If doubling results in a number > 9, subtract 9
4. **Sum all digits** - Add up all the digits
5. **Check digit** - The check digit is whatever makes the total sum divisible by 10

#### Example:

```
Card number: 4532 0151 1234 5678
                              ↑
                         check digit

Steps:
1. Take digits: 4 5 3 2 0 1 5 1 1 2 3 4 5 6 7
2. Double alternating: 8 5 6 2 0 1 10 1 2 2 6 4 10 6 14
3. Subtract 9 if > 9: 8 5 6 2 0 1 1 1 2 2 6 4 1 6 5
4. Sum: 8+5+6+2+0+1+1+1+2+2+6+4+1+6+5 = 50
5. Check digit: 8 (makes total 58, divisible by 10)
```

### Why Use Luhn?

- ✅ Industry standard since 1954
- ✅ Used by all major credit card networks
- ✅ Catches common typing errors
- ✅ Public domain (patent expired)
- ✅ Simple to implement and verify


---

## ❓ FAQ

### Q: Will these cards work for real purchases?
**A:** No. These are mathematically valid but fictitious. They will fail at payment processing.

### Q: Can I use these for testing payment integrations?
**A:** For UI/form testing, yes. For actual payment processor testing, use their official test cards.

### Q: How are these different from official test cards?
**A:** Official test cards from payment processors trigger specific scenarios (success, decline, etc.). These are just for form validation.

### Q: Is this legal?
**A:** Yes, generating test data for development is completely legal. Using them fraudulently is not.

### Q: Why do some cards fail validation?
**A:** If you're using an external validator, ensure it supports all card types (especially JCB, Diners).

### Q: Can I specify custom cardholder names?
**A:** Currently random names are generated. You can modify the code and use Faker for more!

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Important Legal Notice

This software is provided "as is" for **testing and development purposes only**. 

⚠️ **WARNING:** Fraudulent use of credit card information is illegal under:
- 18 U.S.C. § 1029 (Access Device Fraud) - United States
- Computer Fraud and Abuse Act - United States
- Various international cybercrime laws

**The authors are not responsible for any misuse of this software.**

---

## 📚 Resources

### Learn More

- [Luhn Algorithm on Wikipedia](https://en.wikipedia.org/wiki/Luhn_algorithm)
- [PCI Security Standards](https://www.pcisecuritystandards.org/)
- [Payment Card Industry Data Security Standard](https://www.pcisecuritystandards.org/document_library)


---

<div align="center">

**Made with ❤️ for developers**

⭐ **Star this repo** if you find it useful!

</div>