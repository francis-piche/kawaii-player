#!/bin/bash

#get highest tag number
VERSION=`git describe --abbrev=0 --tags`
#FILES=("kawaii_player.py/kawaii-player.py" "setup.py" "kawaii_player.py/version.txt" "kawaii-player/ubuntu/DEBIAN/control") 


#replace . with space so can split into an array
VERSION_BITS=(${VERSION//./ })

#get number parts and increase last one by 1
VNUM1=${VERSION_BITS[0]}
VNUM2=${VERSION_BITS[1]}
VNUM3=${VERSION_BITS[2]}
#VNUM3=$((VNUM3+1))

#create new tag
#NEW_TAG="$VNUM1.$VNUM2.$VNUM3"

FILE="kawaii_player.py/kawaii-player.py"
echo "Updating $VERSION to file $FILE"
sed -i  's/address=.*/address='$addr'/' $FILE

#kawaii_player.py/kawaii-player.py sed 's/foo/bar/'


#get current hash and see if it already has a tag
GIT_COMMIT=`git rev-parse HEAD`
NEEDS_TAG=`git describe --contains $GIT_COMMIT 2>/dev/null`

#only tag if no tag already
if [ -z "$NEEDS_TAG" ]; then
    #git tag $NEW_TAG
    #echo "Tagged with $NEW_TAG"
    #git push --tags
    echo "test"
else
    echo "Already a tag on this commit"
fi
