import zipfile

from odfdo import Document
from argostranslatefiles.formats.abstract_xml import AbstractXml


class Odt(AbstractXml):
    supported_file_extensions = ['.odt']

    def translate(self, translation_request, file_path: str):
        output_path = self.get_output_path(file_path)

        document = Document(file_path)

        body = document.body

        for paragraph in body.get_paragraphs():
            #These can't be accurately placed in the translation, so remove them
            paragraph.remove_spans()
            paragraph.remove_links()
            paragraph.text = translation_request(paragraph.text)

 
        document.save(output_path, pretty=True)
        return output_path
