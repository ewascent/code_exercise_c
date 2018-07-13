#!/usr/bin/env bash
coverage_folder=$(pwd)/tests/test_results
report_file=$coverage_folder/xunit_results.html
rm -rf $report_file, $coverage_folder
mkdir -m 777 $coverage_folder

coverage erase
coverage run --source=src .
nosetests
coverage report -m
pylint --errors-only --score y .

coverage html -d $coverage_folder

#without AWS S3 support, we only want to generate the html locally
if [ "$OS" == 'Windows_NT' ]; then
  junit2html nosetests.xml $report_file
  "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --args $report_file
  "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --args $coverage_folder/index.html
fi
