## Setup

Ensure you have Python 3 installed. I tested the script using Python3.8

Optional: Setup a virtual environment
`python3.8 -m venv ./venv`

Install packages with virtual environment:
`./venv/bin/python3 -m pip install -r requirements.txt`

Without virtual environtment:
`python3.8 -m pip install -r requirements.txt`

## Running code

To remove padding:
`python remove_padding.py input_padded_image output_unpadded_image`

To add padding:
`python scale_image.py input_image output_image`