from mtuoctranslatefiles.formats.opendocument.odt import Odt
from mtuoctranslatefiles.formats.openxml.docx import Docx
from mtuoctranslatefiles.formats.txt import Txt

def get_supported_formats():
    return [
        Txt(),
        Odt(),
        #Odp(),
        Docx(),
        #Pptx()
        #Epub(),
        #Html()
    ]


def translate_file(translation_request, file_path: str):
    """Translate a file.

    Args:
        file_path (str): file path

    Returns:
        file_path: Translated file
    """

    for supported_format in get_supported_formats():
        if supported_format.support(file_path):
            return supported_format.translate(translation_request, file_path)

    return False
