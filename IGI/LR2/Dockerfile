FROM python:3

RUN git clone https://github.com/smartiqaorg/geometric_lib.git /app/geometric_lib

WORKDIR /app/geometric_lib

ENV ARGUMENT value

CMD python -c "from circle import area; print(area(int($ARGUMENT))); from circle import perimeter; print (perimeter(int ($ARGUMENT)))"