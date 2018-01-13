#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class GreatestConan(ConanFile):
    name = "greatest"
    version = "1.3.1"
    url = "https://github.com/bincrafters/conan-greatest"
    description = "A C testing library in 1 file. No dependencies, no dynamic allocation. ISC licensed."
    
    # Indicates License type of the packaged library
    license = "ISC"
    
    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]
    
    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    
    def source(self):
        source_url = "https://github.com/silentbicycle/greatest"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)


    def package(self):
        include_folder = self.source_subfolder
        self.copy(pattern="LICENSE")
        self.copy(pattern="greatest.h", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
