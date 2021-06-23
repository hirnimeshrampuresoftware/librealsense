#!/bin/bash

if [ -n "$(which apt-get)" ]; then
  apt-get install -y build-essential cmake libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev
elif [ -n "$(which yum)" ]; then
  yum install -y openssl-devel libusb1-devel gtk3-devel
fi
