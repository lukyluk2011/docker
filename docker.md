# Docker

## build

docker build -t TAG -f Dockerfile .

## spuštění

docker run -it -v c:\"nevim":\workdir TAG
\\ "nevim" je cesta k souboru, nebo složce co k ní má pak docker kontejner přístup
\\ c:\ je značka disku na které soubor nebo sloška jsou
\\ za dvojtečkou je cesta k souboru uvnitř kontejneru
