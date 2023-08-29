import fitz


def extract_images(file):
    doc = fitz.Document(file)
    return doc
