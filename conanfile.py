from conans import ConanFile, tools
import os


class GreatestConan(ConanFile):
    name = "greatest"
    version = "1.4.1"
    url = "https://github.com/bincrafters/conan-greatest"
    homepage = "https://github.com/silentbicycle/greatest"
    description = "A C testing library in 1 file. No dependencies, no dynamic allocation. "
    license = "ISC"
    _source_subfolder = "source_subfolder"
    no_copy_source = True

    def source(self):
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="greatest.h", dst="include", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
