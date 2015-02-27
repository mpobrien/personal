#!/bin/sh
set -e
if [ -z "$0" ]; then 
	echo "Usage: $0 <path to s3cfg file>"
	exit 1
fi

echo "generating site"
python ./blog.py
cd out
echo "syncing"
s3cmd -c $1 sync . s3://www.mpobrien.sexy
echo "setting permissions"
s3cmd -c $1 setacl --acl-public --recursive s3://www.mpobrien.sexy/blog
echo "done."
