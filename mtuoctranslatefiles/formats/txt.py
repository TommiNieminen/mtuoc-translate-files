from mtuoctranslatefiles.abstract_file import AbstractFile


class Txt(AbstractFile):
    supported_file_extensions = ['.txt']

    def translate(self, translation_request, file_path: str):
        outfile_path = self.get_output_path(file_path)

        infile = open(file_path, "r")
        outfile = open(outfile_path, "w")
        text = infile.read()
        translated_text = translation_request(text)
        outfile.write(translated_text)

        infile.close()
        outfile.close()

        return outfile_path
