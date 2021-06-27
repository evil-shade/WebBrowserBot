#!/bin/bash

# shellcheck disable=SC2046
#kill -9 $(ps -x | grep firefox)
pkill -f firefox
