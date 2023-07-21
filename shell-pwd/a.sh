#!/bin/bash
echo $0

TEST_DIR="$(dirname $0)"

echo $PWD
$TEST_DIR/temp/b.sh

"$1"/d.sh
"$1/d.sh"
