set -ex
gcc -Wall -fbounds-check -O3 logmap.c -o ./logmap.x
./logmap.x
