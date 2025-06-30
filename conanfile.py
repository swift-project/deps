from conan import ConanFile
from conan.tools.cmake import cmake_layout


class SwiftDependencies(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("opus/1.3.1")
        self.requires("libsodium/1.0.18")
        self.requires("libevent/2.1.12")
        if self.settings.os != "Linux":
            self.requires("dbus/1.15.8")

    def configure(self):
        self.options["libevent"].with_openssl = False
        self.options["libevent"].shared = True
        self.options["libsodium"].shared = True
        self.options["opus"].shared = True
        if self.settings.os != "Linux":
            self.options["dbus"].message_bus = True

    def layout(self):
        cmake_layout(self)
