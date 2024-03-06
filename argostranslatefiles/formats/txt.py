from argostranslatefiles.abstract_file import AbstractFile


class Txt(AbstractFile):
    supported_file_extensions = ['.txt']

    def translate(self, file_path: str):
        outfile_path = self.get_output_path(file_path)

        infile = open(file_path, "r")
        outfile = open(outfile_path, "w")

        translated_text = underlying_translation.translate(infile.read())
        outfile.write(translated_text)

        infile.close()
        outfile.close()

        return outfile_path
