# Installing Shiny server into RStudio Image

https://hub.docker.com/r/rocker/rstudio/

Use a custom password by specifying the PASSWORD environmental variable
`docker run -d -p 8787:8787 -e PASSWORD=yourpasswordhere rocker/rstudio`

Give the user root permissions (add to sudoers)
`docker run -d -p 8787:8787 -e ROOT=TRUE rocker/rstudio`

Link a local volume (in this example, the current working directory, $(pwd)) to the rstudio container:
`docker run -d -p 8787:8787 -v $(pwd):/home/rstudio rocker/rstudio`

Add shiny server on start up with e ADD=shiny
`docker run -d -p 3838:3838 -p 8787:8787 -e ADD=shiny rocker/rstudio`

shiny server is now running on localhost:3838 and RStudio on localhost:8787.

Note: this triggers shiny install at runtime, which may require a few minutes to execute before services come up.
If you are building your own Dockerfiles on top of this stack, you should simply include the RUN command:

`RUN export ADD=shiny && bash /etc/cont-init.d/add`

Then omit the -e ADD=shiny when running your image and shiny should be installed and waiting on port 3838.