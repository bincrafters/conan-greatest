#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class GreatestConan(ConanFile):
    name = "greatest"
    version = "1.3.1"
    url = "https://github.com/bincrafters/conan-greatest"
    homepage = "https://github.com/silentbicycle/greatest"
    author = "Bincrafters <bincrafters@gmail.com>"
    description = "A C testing library in 1 file. No dependencies, no dynamic allocation. "
    license = "ISC"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"
    no_copy_source = True

    def source(self):
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        self.copy(pattern="greatest.h", dst="include", src=self.source_subfolder)

    def package_id(self):
        self.info.header_only()
