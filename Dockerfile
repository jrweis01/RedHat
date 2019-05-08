FROM python:2.7.11
RUN pip install pytest
CMD python ./index.py \d{2}:\d{2}:\d{2}.\d{5} -c -