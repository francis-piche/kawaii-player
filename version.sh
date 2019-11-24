#!/bin/bash

#get highest tag number
#VERSION=`git describe --abbrev=0 --tags`

case $TRAVIS_TAG in v*)
    VERSION=$(echo "$TRAVIS_TAG" | sed -r 's/v//g')
    V=$(echo "$VERSION" | sed -r 's/-/./g')
        
    #replace . with space so can split into an array
    VERSION_BITS=(${V//./ })

    #get number parts and increase last one by 1
    #VNUM1=${VERSION_BITS[0]}
    #VNUM2=${VERSION_BITS[1]}
    #VNUM3=${VERSION_BITS[2]}
    #VNUM4=${VERSION_BITS[3]}
 
    FILE="kawaii_player/version.txt"
    echo "Updating $VERSION to file $FILE"
    echo $VERSION > $FILE

    FILE="ubuntu/DEBIAN/control"
    echo "Updating $VERSION to file ${FILE}"
    cp ${FILE}_template $FILE    
    sed -i "s/{VERSION}/$VERSION/" ${FILE}
esac
