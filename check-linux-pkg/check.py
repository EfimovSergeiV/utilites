#!/usr/bin/env python3
import colorama
from colorama import Fore

colorama.init()
personal_packages = 0
general_packages = 0

with open('./inst-later.txt', 'r') as file:
    packages = file.readlines()

with open('./work-installed.txt') as file:
    work_packages = file.readlines()
    for pkg in work_packages:
        if pkg in packages:
            general_packages += 1
            print(Fore.GREEN, f'GENERAL:\t{general_packages}. {pkg[:-1]}')

        else:
            personal_packages += 1
            print(Fore.RED, f'PERSONAL:\t{personal_packages}. {pkg[:-1]}')


print(
    f"\n\nGENERAL PKG:\t{general_packages}",
    f"\nPERSONAL PKG:\t{personal_packages}",
)