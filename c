set -e

gcc \
    -Wextra \
    -Wall \
    -fbounds-check \
    logmap.c \
    -O3 \
    -o ./logmap.x \
    -nostdlib \
    -masm=intel \
    -Wl,--gc-sections \
    -nostartfiles \
    -static \
    -fomit-frame-pointer \
    -fno-exceptions \
    -fno-asynchronous-unwind-tables \
    -fno-unwind-tables

strip \
    -s logmap.x \
    -R .comment \
    -R .gnu.version \
    -R .note.gnu.build-id \
    --strip-unneeded

./logmap.x

wc -c ./logmap.x
