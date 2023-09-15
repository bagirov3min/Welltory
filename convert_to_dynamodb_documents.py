from datetime import datetime, timedelta
from typing import List, Dict


def convert_to_dynamodb_documents(
        user_id: int,
        day: datetime.date,
        activity_scores: List[int]
) -> List[Dict]:
    documents = []
    timestamp = int(day.timestamp())  # Unix timestamp начала дня

    # Разделяем activity_scores на часовые интервалы и создаем документы
    for hour in range(24):
        start_time = timestamp + (hour * 3600)  # Начало текущего часа
        end_time = start_time + 3600  # Конец текущего часа
        doc = {
            "u": user_id,
            "t": start_time,
            "v": activity_scores[hour * 2880 // 24: (hour + 1) * 2880 // 24]
        }
        documents.append(doc)

    # Создаем документ за 12 часов (весь день)
    doc = {
        "u": user_id,
        "t": timestamp,
        "v": activity_scores
    }
    documents.append(doc)

    return documents
