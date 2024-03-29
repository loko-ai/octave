FROM gnuoctave/octave:6.2.0
EXPOSE 8080
ADD ./requirements.txt /
RUN pip install -r /requirements.txt
ADD ./requirements_octave.txt /
ADD ./octave.sh /
RUN sh "/octave.sh"
ARG GATEWAY
ENV GATEWAY=$GATEWAY
ADD . /plugin
ENV PYTHONPATH=$PYTHONPATH:/plugin
WORKDIR /plugin/services
CMD python3 services.py