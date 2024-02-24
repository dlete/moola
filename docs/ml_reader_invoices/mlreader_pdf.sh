#!/bin/sh

test_url='35.232.51.61:5000/extract'
pdf_file=./invoice_clean.pdf

(echo  '{';
 echo ' "pdf": "';
  base64 $pdf_file;
  echo '", '
  echo ' "features": [{ "donate": "1"}] ';
  echo ' }') | curl -H "Content-Type: application/json" -d @-  $test_url
