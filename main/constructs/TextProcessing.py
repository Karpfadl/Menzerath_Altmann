import chardet


def get_text(path: str):
    def change_encoding(text_, from_encoding):
        return text_.decode(from_encoding)

    text = open(path, "rb").read()
    # TODO clean text
    estimate = chardet.detect(text)
    print(f"text encoding {estimate["encoding"]} detected with confidence {estimate["confidence"]}")
    return change_encoding(text, estimate["encoding"])
