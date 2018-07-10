#!/usr/bin/env bash
pylint --errors-only --score y .
nosetests -v
