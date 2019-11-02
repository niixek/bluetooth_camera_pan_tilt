# deleting and moving of files to clean up after install
cd &&
mv PS3_connect_controller.sh ~/PS3control/ &&

cd ~/PS3control &&
rm -r QtSixA-1.5.1-src.tar.gz &&
rm -r compilation_sid.patch &&

rm -r 1-dependencies.sh &&
rm -r 2-downloads.sh &&
rm -r 3-buildfromsource.sh &&
rm -r 4-tidyup.sh 
