from sqlalchemy import Column, Integer

from app.database import Base


class Statistics(Base):

    __tablename__ = "statistics"

    id = Column(
        Integer,
        primary_key=True
    )

    automations = Column(
        Integer,
        default=0,
        nullable=False
    )

    successful_automations = Column(
        Integer,
        default=0,
        nullable=False
    )

    failed_automations = Column(
        Integer,
        default=0,
        nullable=False
    )

    ai_corrections = Column(
        Integer,
        default=0,
        nullable=False
    )

    successful_corrections = Column(
        Integer,
        default=0,
        nullable=False
    )

    failed_corrections = Column(
        Integer,
        default=0,
        nullable=False
    )

    rollbacks = Column(
        Integer,
        default=0,
        nullable=False
    )

    successful_rollbacks = Column(
        Integer,
        default=0,
        nullable=False
    )

    failed_rollbacks = Column(
        Integer,
        default=0,
        nullable=False
    )