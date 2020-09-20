#!/bin/bash

sed -E 's/\[name=([a-zA-Z0-9]+)\]/\[\[name:\1|\1\]\]/g'
