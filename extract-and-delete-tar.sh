#!/bin/bash
for file in *.tar.gz; do tar xvf "${file}" && rm "${file}"; done
