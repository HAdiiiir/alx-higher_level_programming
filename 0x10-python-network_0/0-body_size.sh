#!/bin/bash
# displays the size of the body of the response from the url
curl -sI "$1" | grep Content-Length | cut -d' ' -f2
