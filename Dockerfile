FROM python
WORKDIR /app
copy . .
CMD ["python","main.py"]