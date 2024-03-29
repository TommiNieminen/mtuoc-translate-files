import abc
import os.path


class AbstractFile():
    supported_file_extensions = []

    def support(self, file_path: str):
        file_ext = os.path.splitext(file_path)[1]

        return file_ext in self.supported_file_extensions

    def get_output_path(self, file_path: str):
        dir_path = os.path.dirname(file_path)
        file_name, file_ext = os.path.splitext(os.path.basename(file_path))

        return dir_path + "/" + file_name + "_translated" + file_ext

    @abc.abstractmethod
    def translate(self, translation_request, file_path: str): raise NotImplementedError
