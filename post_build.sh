#!/usr/bin/env bash
report_file=$(pwd)/tests/test_results/xunit_results.html
coverage_folder=$(pwd)/tests/test_results
rm -rf $report_file, $coverage_folder/*
mkdir -m 777 $coverage_folder
pylint --errors-only --score y .
nosetests ./tests
coverage erase
coverage run --source=src .
coverage report -m
coverage html -d $coverage_folder

#without AWS S3 support, we only want to generate the html locally
if [ "$OS" == 'Windows_NT' ]; then
  junit2html nosetests.xml $report_file
  "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --args $report_file
  "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --args $coverage_folder/index.html
fi
