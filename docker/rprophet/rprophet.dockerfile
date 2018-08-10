FROM rocker/verse:latest

# MAINTAINER Winston Chang "winston@rstudio.com"
MAINTAINER Mat Brunt "matbrunt@gmail.com"

# Install dependencies and Download and install shiny server
# RUN apt-get update && apt-get install -y \
#     sudo \
#     gdebi-core \
#     pandoc \
#     pandoc-citeproc \
#     libcurl4-gnutls-dev \
#     libcairo2-dev \
#     libxt-dev && \
#     wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \
#     VERSION=$(cat version.txt)  && \
#     wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb && \
#     gdebi -n ss-latest.deb && \
#     rm -f version.txt ss-latest.deb && \
#     R -e "install.packages(c('shiny', 'rmarkdown', 'prophet'), repos='https://cran.rstudio.com/')" && \
#     cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/ && \
#     rm -rf /var/lib/apt/lists/*

RUN export ADD=shiny && bash /etc/cont-init.d/add

RUN R -e "install.packages(c('rmarkdown', 'forecast', 'prophet'), repos='https://cran.rstudio.com/')"

EXPOSE 3838 8787

# COPY shiny-server.sh /usr/bin/shiny-server.sh
# RUN chmod +x /usr/bin/shiny-server.sh

# CMD ["/usr/bin/shiny-server.sh"]