#!/bin/bash

eguna=`date +"%F"`
rsync -a --link-dest=/home/gortxut/Segurtasuna/BabesKopiak . /var/tmp/Backups/$eguna