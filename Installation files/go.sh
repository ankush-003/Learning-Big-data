#!/bin/bash

start_dir=$(pwd)
cd

echo "======================"
echo " Installing GO "
echo "======================"

sudo apt-get update -y
sudo apt-get upgrade -y

wget https://go.dev/dl/go1.21.3.linux-amd64.tar.gz

tar -xvf go1.21.3.linux-amd64.tar.gz

if [ -d "/usr/local/go" ]; then
	echo "Deleting previous installation"
	sudo rm -rf /usr/local/go
fi

sudo mv go /usr/local

echo "export GOROOT=/usr/local/go" >> ~/.bashrc
echo "export GOPATH=\$HOME/go" >> ~/.bashrc
echo "export PATH=\$PATH:\$GOPATH/bin:\$GOROOT/bin" >> ~/.bashrc
source ~/.bashrc

go version
