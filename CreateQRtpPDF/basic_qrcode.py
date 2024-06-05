
# basic_qrcode.py
import segno
import argparse
import sys

def create_qr_code(data, filename):
    qr = segno.make(data, error='H')  # Increase error-correction level for better reliability
    qr.save(filename)

def validate_and_prepare_data(data_type, data):
    if data_type == "url":
        if not data.lower().startswith(("http://", "https://")):
            data = "http://" + data
        return data
    elif data_type == "email":
        parts = data.split('><')
        if len(parts) != 3:
            raise ValueError("Email data must be in the format '<email-address><subject><body>'")
        email = parts[0].replace('<', '')
        subject = parts[1]
        body = parts[2].replace('>', '')
        return f"mailto:{email}?subject={subject}&body={body}"
    elif data_type == "sms":
        parts = data.split('><')
        if len(parts) != 2:
            raise ValueError("SMS data must be in the format '<phone-number><message>'")
        phone_number = parts[0].replace('<', '')
        message = parts[1].replace('>', '')
        return f"sms:{phone_number}?body={message}"
    elif data_type == "call":
        return f"tel:{data.strip()}"
    elif data_type == "text":
        return data
    else:
        raise ValueError("Invalid data type. Expected 'url', 'email', 'sms', 'call', or 'text'")

def print_extended_help(data_type):
    help_messages = {
        "url": "URL data type expects a valid URL. Example: -d 'http://example.com'.",
        "email": "Email data type expects data in the format '<email-address><subject><body>'. Example: -d '<someone@example.com><Subject><Body>'.",
        "sms": "SMS data type expects data in the format '<phone-number><message>'. Example: -d '<1234567890><Hello, this is a message>'",
        "call": "Call data type expects a phone number. Example: -d '1234567890'.",
        "text": "Text data type expects plain text. Example: -d 'This is a plain text message.'."
    }
    print(help_messages.get(data_type, "Unknown data type."))

def main():
    parser = argparse.ArgumentParser(description='Create QR codes for various types of data.', add_help=False)
    parser.add_argument('-t', '--type', choices=["url", "email", "sms", "call", "text"], help='Type of data: url, email, sms, call, text')
    parser.add_argument('-d', '--data', help='Data to encode in the QR code')
    parser.add_argument('-o', '--output', help='Output filename (without extension)')
    parser.add_argument('-f', '--format', choices=["png", "pdf"], default="png", help='Format/extension of the output file: png, pdf')
    parser.add_argument('-h', '--help', nargs='?', const=True, help='Show help message. Optionally, provide a data type for more specific help.')

    args = parser.parse_args()

    if args.help is not None:
        if args.help is True:
            parser.print_help()
        else:
            print_extended_help(args.help)
        sys.exit(0)

    if not args.type or not args.data or not args.output:
        parser.print_help()
        sys.exit(1)

    data_type = args.type
    data = args.data
    filename = f"{args.output}.{args.format}"

    try:
        prepared_data = validate_and_prepare_data(data_type, data)
        create_qr_code(prepared_data, filename)
        print(f"QR code created and saved as {filename}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()



