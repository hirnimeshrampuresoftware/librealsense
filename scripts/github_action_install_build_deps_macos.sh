#!/bin/bash

brew uninstall xctool;
brew install xctool --HEAD;
brew install homebrew/core/glfw3;
brew list libusb || brew install libusb;
