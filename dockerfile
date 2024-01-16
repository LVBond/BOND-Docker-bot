FROM python:3.10-slim
ENV TOKEN="Твой токен от папы"
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py" ]


