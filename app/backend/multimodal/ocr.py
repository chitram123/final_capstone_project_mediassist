import easyocr

# Load model only once when the application starts
reader = easyocr.Reader(
    ['en'],
    gpu=False
)


def extract_text(image_path):

    result = reader.readtext(
        image_path,
        detail=0
    )

    text = "\n".join(result)

    return text

