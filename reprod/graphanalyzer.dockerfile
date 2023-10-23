FROM lazzarigioele/python38:latest


COPY graphanalyzer.yml /home/jovyan/
RUN \
conda config --system --prepend channels bioconda && \
mamba env update -n base --file /home/jovyan/graphanalyzer.yml && \
mamba clean --all -f -y && \
rm /home/jovyan/graphanalyzer.yml

