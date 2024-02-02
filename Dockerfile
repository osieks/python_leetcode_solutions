FROM python
WORKDIR /app
copy . .
CMD ["python","merge_sorted_array.py"]