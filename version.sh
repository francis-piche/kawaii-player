#!/bin/bash

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_website_files() {
    
    VERSION=$(echo "$TRAVIS_TAG" | sed -r 's/v//g')
    V=$(echo "$VERSION" | sed -r 's/-/./g')
         
    FILE="kawaii_player/version.txt"
    echo "Updating $VERSION to file $FILE"
    echo $VERSION > $FILE

    FILE="ubuntu/DEBIAN/control"
    echo "Updating $VERSION to file ${FILE}"
    cp ${FILE}_template $FILE    
    sed -i "s/{VERSION}/$VERSION/" ${FILE}
    
    git add "kawaii_player/version.txt" "ubuntu/DEBIAN/control"
    git commit -m "Automated version change"

    python3 ubuntu/create_deb.py
    cd ubuntu
    ls
}

upload_files() {
  git remote add origin-travis https://${GITHUB_TOKEN}@github.com/francis-piche/kawaii-player.git > /dev/null 2>&1
  git push origin-travis HEAD:master
}

setup_git
commit_website_files
upload_files
