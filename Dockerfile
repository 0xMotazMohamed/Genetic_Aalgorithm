FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create writable directory and set permissions
RUN mkdir -p /tmp/.streamlit && chmod -R 777 /tmp/.streamlit

# Set environment variables
ENV STREAMLIT_CONFIG_DIR=/tmp/.streamlit
ENV STREAMLIT_DISABLE_METRICS=true
ENV HOME=/tmp

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]