FROM gcc:latest

WORKDIR /app
COPY app /app
RUN gcc -o vulnerable_app buffer_overflow.c -fno-stack-protector -z execstack

CMD ["./vulnerable_app", "test"]
