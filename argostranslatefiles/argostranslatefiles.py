#from argostranslatefiles.formats.html import Html
#from argostranslatefiles.formats.opendocument.odp import Odp
from argostranslatefiles.formats.opendocument.odt import Odt
from argostranslatefiles.formats.openxml.docx import Docx
#from argostranslatefiles.formats.openxml.pptx import Pptx
from argostranslatefiles.formats.txt import Txt
#from argostranslatefiles.formats.epub import Epub

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
