FROM python:3.13.11

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/ 
# after executing this uv becomes available in the image, we can use it to install dependencies

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"
# specify the directory where we want to copy the files and run the commands
COPY pyproject.toml .python-version uv.lock ./   
RUN uv sync --locked 
# this will install the dependencies specified in the uv.lock file, ensuring that we have a consistent environment for our application
COPY ingest_data.py . 

ENTRYPOINT ["python", "ingest_data.py"]
