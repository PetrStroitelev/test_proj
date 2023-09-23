from sqlalchemy import Integer, Column, String
from dal.db_connection import Base, db_connection, Session
from typing import List

from dal.dto.task_dto import TaskDto


class Task(Base):
    __tablename__ = 't_task'
    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String(), nullable=False)

    @staticmethod
    @db_connection
    def create_task(message: str) -> int:
        session = Session()
        message = Task(message=message)
        session.add(message)
        session.flush()
        return message.id

    @staticmethod
    @db_connection
    def get_all_tasks() -> List[TaskDto]:
        session = Session()
        result = session.query(Task).all()

        list_ = []
        for message in result:
            list_.append(message.convert_to_dto())

        return list_

    @staticmethod
    @db_connection
    def delete_task(id_: int) -> None:
        session = Session()
        result = session.query(Task).filter(Task.id == id_).first()
        session.delete(result)

    def convert_to_dto(self) -> TaskDto:
        return TaskDto(id=self.id, message=self.message)
