import pytest
from os import path
from extract_images import extract_images


def describe_extract_images():
    def it_returns_an_array_the_length_of_the_pdf():
        file_path = path.relpath("tests/assets/6004_pdf_image.pdf")
        with open(file_path) as my_file:
            assert len(extract_images(file=file_path)) == 14
