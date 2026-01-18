import random
import argparse
import json
import sys
from datetime import datetime, timedelta


class CardGenerator:
    CARD_CONFIGS = {
        "visa": {
            "name": "Visa",
            "prefixes": [[4]],
            "length": 16,
            "cvv_length": 3
        },
        "mastercard": {
            "name": "Mastercard",
            "prefixes": [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5]],
            "length": 16,
            "cvv_length": 3
        },
        "amex": {
            "name": "American Express",
            "prefixes": [[3, 4], [3, 7]],
            "length": 15,
            "cvv_length": 4
        },
        "discover": {
            "name": "Discover",
            "prefixes": [[6, 0, 1, 1]],
            "length": 16,
            "cvv_length": 3
        },
        "jcb": {
            "name": "JCB",
            "prefixes": [[3, 5, 2, 8], [3, 5, 2, 9]],
            "length": 16,
            "cvv_length": 3
        },
        "diners": {
            "name": "Diners Club",
            "prefixes": [[3, 6], [3, 8]],
            "length": 14,
            "cvv_length": 3
        }
    }

    @staticmethod
    def luhn_checksum(card_digits):
        check_sum = 0
        check_offset = (len(card_digits) + 1) % 2

        for i, digit in enumerate(card_digits):
            if (i + check_offset) % 2 == 0:
                doubled = digit * 2
                check_sum += doubled - 9 if doubled > 9 else doubled
            else:
                check_sum += digit

        return (10 - (check_sum % 10)) % 10

    @staticmethod
    def validate_luhn(card_number):
        try:
            digits = [int(d) for d in card_number.replace(" ", "").replace("-", "")]
            check_digit = digits.pop()
            return CardGenerator.luhn_checksum(digits) == check_digit
        except (ValueError, IndexError):
            return False

    @classmethod
    def generate(cls, card_type, expiry_years_ahead=2):
        if card_type is None:
            card_type = random.choice(list(cls.CARD_CONFIGS.keys()))
        elif card_type.lower() not in cls.CARD_CONFIGS:
            raise ValueError(f"Unknown card type: {card_type}. Valid types: {', '.join(cls.CARD_CONFIGS.keys())}")

        card_type = card_type.lower()
        config = cls.CARD_CONFIGS[card_type]

        prefix = random.choice(config["prefixes"]).copy()
        remaining_length = config["length"] - len(prefix) - 1

        card_digits = prefix + [random.randint(0, 9) for _ in range(remaining_length)]
        checksum = cls.luhn_checksum(card_digits)
        card_digits.append(checksum)

        card_number = "".join(map(str, card_digits))

        if card_type == "amex":
            formatted_number = f"{card_number[:4]} {card_number[4:10]} {card_number[10:]}"
        elif card_type == "diners":
            formatted_number = f"{card_number[:4]} {card_number[4:10]} {card_number[10:]}"
        else:
            formatted_number = " ".join([card_number[i:i + 4] for i in range(0, len(card_number), 4)])

        cvv_length = config["cvv_length"]
        cvv = "".join([str(random.randint(0, 9)) for _ in range(cvv_length)])

        today = datetime.now()
        months_ahead = random.randint(1, expiry_years_ahead * 12)
        expiry_date = today + timedelta(days=months_ahead * 30)

        month = f"{expiry_date.month:02d}"
        year_2digit = f"{expiry_date.year % 100:02d}"
        year_4digit = str(expiry_date.year)

        first_names = [
            "John", "Jane", "Michael", "Sarah", "David", "Emily", "James", "Emma",
            "Robert", "Lisa", "Daniel", "Olivia", "Matthew", "Sophia", "Andrew",
            "Isabella", "Joseph", "Mia", "William", "Charlotte", "Alexander",
            "Amelia", "Christopher", "Harper", "Joshua", "Evelyn", "Ryan", "Abigail",
            "Nicholas", "Ella", "Anthony", "Avery", "Samuel", "Scarlett", "Benjamin",
            "Grace", "Jonathan", "Chloe", "Henry", "Victoria", "Justin", "Riley",
            "Aaron", "Aria", "Kevin", "Lily", "Brian", "Zoey", "Thomas", "Hannah",
            "Steven", "Nora", "Mark", "Addison", "Paul", "Ellie", "Jason", "Layla",
            "Timothy", "Brooklyn", "Charles", "Penelope", "Jeffrey", "Lillian",
            "Patrick", "Audrey", "Scott", "Claire", "Brandon", "Lucy", "Adam",
            "Paisley", "Zachary", "Everly", "Sean", "Anna", "Kyle", "Caroline",
            "Ethan", "Nova", "Jeremy", "Genesis", "Christian", "Emilia", "Nathan",
            "Samantha", "Jordan", "Maya"
        ]
        last_names = [
            "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
            "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez",
            "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
            "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark",
            "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen", "King",
            "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green",
            "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
            "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz",
            "Parker", "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris",
            "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan",
            "Cooper", "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos",
            "Kim", "Cox", "Ward", "Richardson", "Watson", "Brooks", "Chavez",
            "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes",
            "Price", "Alvarez", "Castillo", "Sanders"
        ]
        cardholder = f"{random.choice(first_names)} {random.choice(last_names)}".upper()

        return {
            "card_type": config["name"],
            "card_number": card_number,
            "card_number_formatted": formatted_number,
            "cvv": cvv,
            "expiry_month": month,
            "expiry_year": year_2digit,
            "expiry_year_full": year_4digit,
            "expiry_date": f"{month}/{year_2digit}",
            "cardholder_name": cardholder
        }

    @classmethod
    def generate_batch(cls, count, card_type):
        return [cls.generate(card_type) for _ in range(count)]


def format_output(cards, output_format):
    if output_format == "json":
        return json.dumps(cards, indent=2)

    elif output_format == "csv":
        if not cards:
            return ""

        headers = list(cards[0].keys())
        lines = [",".join(headers)]
        for card in cards:
            lines.append(",".join(str(card[h]) for h in headers))
        return "\n".join(lines)

    elif output_format == "table":
        output = []
        for card in cards:
            output.append("=" * 50)
            output.append(f"Card Type:    {card['card_type']}")
            output.append(f"Card Number:  {card['card_number_formatted']}")
            output.append(f"Cardholder:   {card['cardholder_name']}")
            output.append(f"Expiry Date:  {card['expiry_date']}")
            output.append(f"CVV:          {card['cvv']}")
            output.append("=" * 50)
        return "\n".join(output)

    else:
        output = []
        for i, card in enumerate(cards, 1):
            if len(cards) > 1:
                output.append(f"\n{'=' * 50}")
                output.append(f"CARD #{i}")
                output.append('=' * 50)
            output.append(f"{card['card_type']}")
            output.append(f"Number:     {card['card_number_formatted']}")
            output.append(f"Cardholder: {card['cardholder_name']}")
            output.append(f"Expiry:     {card['expiry_date']}")
            output.append(f"CVV:        {card['cvv']}")
        return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description="Generate fake credit cards for testing purposes",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog="""
Examples:
  %(prog)s                          Generate one random card
  %(prog)s -t visa                  Generate a Visa card
  %(prog)s -n 5                     Generate 5 random cards
  %(prog)s -t mastercard -n 3       Generate 3 Mastercard cards
  %(prog)s -f json > cards.json     Output in JSON format
  %(prog)s -t amex -f csv           Generate Amex card in CSV format
  %(prog)s --validate 4532015112345678  Validate a card number

Available card types: visa, mastercard, amex, discover, jcb, diners
        """
                                     )

    parser.add_argument("-t", "--type", choices=list(CardGenerator.CARD_CONFIGS.keys()), help="Card type to generate")

    parser.add_argument("-n", "--number", type=int, default=1, metavar="N", help="Number of cards to generate (default: 1)")

    parser.add_argument("-f", "--format", choices=["text", "json", "csv", "table"], default="text", help="Output format (default: text)")

    parser.add_argument("--validate", metavar="CARD_NUMBER", help="Validate a card number using Luhn algorithm")

    parser.add_argument("--list-types", action="store_true", help="List all available card types")

    args = parser.parse_args()

    if args.list_types:
        print("Available card types:")
        for key, config in CardGenerator.CARD_CONFIGS.items():
            print(f"  {key:12} - {config['name']}")
        return 0

    if args.validate:
        is_valid = CardGenerator.validate_luhn(args.validate)
        print(f"Card number: {args.validate}")
        print(f"Valid: {'✓ YES' if is_valid else '✗ NO'}")
        return 0 if is_valid else 1

    try:
        cards = CardGenerator.generate_batch(args.number, args.type)
        output = format_output(cards, args.format)
        print(output)
        return 0
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
