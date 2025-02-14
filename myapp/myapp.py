# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2021 Tobias Fella <fella@posteo.de>

import info
from Blueprints.CraftPackageObject import CraftPackageObject
from CraftCore import CraftCore
from Package.CMakePackageBase import CMakePackageBase


class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues(gitUrl="https://github.com/I-dont-need-name/StoneEX.git")
        self.displayName = "StoneEX"
        self.description = "Stone exhibition management"
        self.svnTargets["master"] = "https://github.com/I-dont-need-name/StoneEX.git"
        self.defaultTarget = "main"

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = None
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt/qtbase"] = None
        #self.runtimeDependencies["libs/qt/qtsql"] = None
        self.runtimeDependencies["libs/qt/qtdeclarative"] = None
        #self.runtimeDependencies["libs/qt/qtcharts"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kirigami"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kquickcharts"] = None
        self.runtimeDependencies["kde/frameworks/tier3/knotifications"] = None
        self.runtimeDependencies["kde/libs/kweathercore"] = None
        self.runtimeDependencies["kde/unreleased/kirigami-addons"] = None
        if not CraftCore.compiler.isAndroid:
            self.runtimeDependencies["kde/frameworks/tier1/breeze-icons"] = None
            self.runtimeDependencies["kde/frameworks/tier3/qqc2-desktop-style"] = None
            self.runtimeDependencies["kde/plasma/breeze"] = None
        else:
            self.runtimeDependencies["kde/plasma/qqc2-breeze-style"] = None
            self.runtimeDependencies["kde/frameworks/tier1/breeze-icons"] = None


class Package(CMakePackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.subinfo.options.configure.args += ["-DBUILD_PLASMOID=OFF"]
        #self.blacklist_file.append(self.blueprintDir() / "blacklist.txt")

    def createPackage(self):
        self.defines["executable"] = r"bin\stoneex"
        #self.addExecutableFilter(r"(bin|libexec)/(?!(kweather|update-mime-database)).*")
        #self.ignoredPackages.append("binary/mysql")
        if not CraftCore.compiler.isLinux:
            self.ignoredPackages.append("libs/dbus")
        return super().createPackage()
