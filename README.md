# software\_workshop\_mate

Program direct:

PS F:\\MATE\\software\_workshop\\software\_workshop\_02> uv run hello.py

OS: Windows

Detail: Windows-11-10.0.26200-SP0

Python: 3.14.6



Through WSL

PS F:\\MATE\\software\_workshop\\software\_workshop\_02> wsl -d Ubuntu-22.04                              

rasyaizzaa@LAPTOP-UP2C6NOU:/mnt/f/MATE/software\_workshop/software\_workshop\_02$ python3 hello.py

OS: Linux

Detail: Linux-6.18.58.1-microsoft-standard-WSL2-x86\_64-with-glibc2.35

Python: 3.10.12



Through Docker

PS F:\\MATE\\software\_workshop\\software\_workshop\_02> docker build -t hello-demo .

\[+] Building 2.2s (9/9) FINISHED                                                                                        docker:desktop-linux

&#x20;=> \[internal] load build definition from dockerfile                                                                                    0.1s

&#x20;=> => transferring dockerfile: 119B                                                                                                    0.0s

&#x20;=> \[internal] load metadata for docker.io/library/python:3.11-slim                                                                     1.8s

&#x20;=> \[auth] library/python:pull token for registry-1.docker.io                                                                           0.0s

&#x20;=> \[internal] load .dockerignore                                                                                                       0.0s

&#x20;=> => transferring context: 2B                                                                                                         0.0s

&#x20;=> \[1/3] FROM docker.io/library/python:3.11-slim@sha256:07d4824036af339fa1b6ef769cc99d9c10a141769538b52b3b597c84f7a7b535               0.0s

&#x20;=> => resolve docker.io/library/python:3.11-slim@sha256:07d4824036af339fa1b6ef769cc99d9c10a141769538b52b3b597c84f7a7b535               0.0s

&#x20;=> \[internal] load build context                                                                                                       0.0s

&#x20;=> => transferring context: 30B                                                                                                        0.0s

&#x20;=> CACHED \[2/3] WORKDIR /app                                                                                                           0.0s

&#x20;=> CACHED \[3/3] COPY hello.py .                                                                                                        0.0s

&#x20;=> exporting to image                                                                                                                  0.1s

&#x20;=> => exporting layers                                                                                                                 0.0s

&#x20;=> => exporting manifest sha256:8642712b537f12e02030685a4be7686d50359dc56add354dda8dbd18f80ab666                                       0.0s

&#x20;=> => exporting config sha256:7e64c955d91f11baf9a976725c0efbc207e0a351b778079dc88bd0cc5e1977bc                                         0.0s

&#x20;=> => exporting attestation manifest sha256:b8d35c0a4635363823f5af00596f77a828124569c1ae25ae990b672276d79ebb                           0.0s

&#x20;=> => exporting manifest list sha256:3c2f566ed354e0f4673fc2224db2ded2b808f44b0a6d6eb19184ab8cef0adb7c                                  0.0s

&#x20;=> => naming to docker.io/library/hello-demo:latest                                                                                    0.0s

&#x20;=> => unpacking to docker.io/library/hello-demo:latest                                                                                 0.0s

PS F:\\MATE\\software\_workshop\\software\_workshop\_02> docker run --rm hello-demo  

OS: Linux

Detail: Linux-6.18.58.1-microsoft-standard-WSL2-x86\_64-with-glibc2.41

Python: 3.11.18

