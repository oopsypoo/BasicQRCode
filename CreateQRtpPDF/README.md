# QR Code Generator

This project provides a Python script to generate QR codes from various types of data such as URLs, email addresses, SMS messages, phone numbers, and plain text. The generated QR code can be saved in either PNG or PDF format.

## Dependencies

- `segno`
- `argparse`
- `sys`

You can install the `segno` library using pip:

```sh
pip install segno
```

## Usage

The script can be executed from the command line. Below are the available options and their usage:

```sh
python basic_qrcode.py [-h] [-t {url,email,sms,call,text}] [-d DATA] [-o OUTPUT] [-f {png,pdf}]
```

### Options

- `-t`, `--type` : The type of data to encode. Choices are `url`, `email`, `sms`, `call`, and `text`.
- `-d`, `--data` : The data to encode in the QR code.
- `-o`, `--output` : The output filename (without extension).
- `-f`, `--format` : The format/extension of the output file. Choices are `png`, `pdf`. The default is `png`.
- `-h`, `--help` : Show help message. Optionally, provide a data type for more specific help.

### Data Formatting

Each data type has specific formatting requirements:

1. **URL**:
   - Expects a valid URL.
   - Example: `-d 'http://example.com'`.
   
2. **Email**:
   - Expects data in the format `<email-address><subject><body>`.
   - Example: `-d '<someone@example.com><Subject><Body>'`.
   
3. **SMS**:
   - Expects data in the format `<phone-number><message>`.
   - Example: `-d '<1234567890><Hello, this is a message>'`.
   
4. **Call**:
   - Expects a phone number.
   - Example: `-d '1234567890'`.
   
5. **Text**:
   - Expects plain text.
   - Example: `-d 'This is a plain text message.'`.

### Examples

1. Create a QR code for a URL:
   
   ```sh
   python basic_qrcode.py -t url -d 'http://example.com' -o my_qr_code -f png
   ```
   This will create a QR code for `http://example.com` and save it as `my_qr_code.png`.

2. Create a QR code for an email:
   
   ```sh
   python basic_qrcode.py -t email -d '<someone@example.com><Hello><This is the body>' -o my_email_qr_code -f png
   ```
   This will create a QR code for the email and save it as `my_email_qr_code.png`.

3. Create a QR code for an SMS:
   
   ```sh
   python basic_qrcode.py -t sms -d '<1234567890><Hello there>' -o my_sms_qr_code -f pdf
   ```
   This will create a QR code for the SMS and save it as `my_sms_qr_code.pdf`.

## Error Handling

In case of invalid input, the script will display an appropriate error message and provide guidance on the expected format for the specified data type.

## Help

To get detailed help for a specific data type, you can use the `-h` or `--help` flag followed by the data type:

```sh
python basic_qrcode.py -h url
```

This will provide more specific information about the expected format for the URL data type.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Developed using the `segno` library for generating QR codes.