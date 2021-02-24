#!/bin/bash
## loop around and issue 201 gets to /fast ##
for ((i=1;i<=201;i++));
do
    curl "http://0.0.0.0:2224/fast";
done
