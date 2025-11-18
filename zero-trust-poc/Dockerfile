FROM python:3.11-slim
WKDIR /app
#Copy pipeline code
COPY pipeline/ /app/pipeline/
COPY pipeline/ /app/policies/
#Install dependencies
RUN pip install pyyaml coloroma

CMD ["python", "pipeline/cicd_pipeline.py"]
