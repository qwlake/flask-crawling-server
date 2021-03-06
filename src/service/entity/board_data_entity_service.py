from typing import List

from src.entity.BoardData import BoardData


def find_all_by_crawling_status(session, crawling_status: str) -> List[BoardData]:
    query_result = session.query(BoardData)
    return query_result.filter_by(crawling_status=crawling_status).all()


def find_by_code(session, code: str) -> BoardData:
    query_result = session.query(BoardData)
    return query_result.filter_by(code=code).first()
