rm -r ./docs
make html
mv _build/html ./docs
rm -r ./_build
cp ./404.html ./docs/
cp ./CNAME ./docs/
