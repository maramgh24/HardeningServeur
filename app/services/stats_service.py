from threading import Lock

from app.database import Base, SessionLocal, engine
from app.models.stats_model import Statistics


class StatsService:

    def __init__(self):

        self._lock = Lock()

        self._initialize_database()


    def _initialize_database(self):

        Base.metadata.create_all(
            bind=engine
        )

        db = SessionLocal()

        try:

            statistics = (
                db.query(Statistics)
                .filter(
                    Statistics.id == 1
                )
                .first()
            )

            if statistics is None:

                statistics = Statistics(
                    id=1,
                    automations=0,
                    successful_automations=0,
                    failed_automations=0,
                    ai_corrections=0,
                    successful_corrections=0,
                    failed_corrections=0,
                    rollbacks=0,
                    successful_rollbacks=0,
                    failed_rollbacks=0
                )

                db.add(statistics)
                db.commit()

        finally:

            db.close()


    # ==================================================
    # AUTOMATION
    # ==================================================

    def record_automation(self, success: bool):

        with self._lock:

            db = SessionLocal()

            try:

                statistics = (
                    db.query(Statistics)
                    .filter(
                        Statistics.id == 1
                    )
                    .first()
                )

                statistics.automations += 1

                if success:

                    statistics.successful_automations += 1

                else:

                    statistics.failed_automations += 1

                db.commit()

            finally:

                db.close()


    # ==================================================
    # AI CORRECTION
    # ==================================================

    def record_ai_correction(self):

        with self._lock:

            db = SessionLocal()

            try:

                statistics = (
                    db.query(Statistics)
                    .filter(
                        Statistics.id == 1
                    )
                    .first()
                )

                statistics.ai_corrections += 1

                db.commit()

            finally:

                db.close()


    # ==================================================
    # CORRECTION EXECUTION
    # ==================================================

    def record_correction_execution(
        self,
        success: bool
    ):

        with self._lock:

            db = SessionLocal()

            try:

                statistics = (
                    db.query(Statistics)
                    .filter(
                        Statistics.id == 1
                    )
                    .first()
                )

                if success:

                    statistics.successful_corrections += 1

                else:

                    statistics.failed_corrections += 1

                db.commit()

            finally:

                db.close()


    # ==================================================
    # ROLLBACK
    # ==================================================

    def record_rollback(
        self,
        success: bool
    ):

        with self._lock:

            db = SessionLocal()

            try:

                statistics = (
                    db.query(Statistics)
                    .filter(
                        Statistics.id == 1
                    )
                    .first()
                )

                statistics.rollbacks += 1

                if success:

                    statistics.successful_rollbacks += 1

                else:

                    statistics.failed_rollbacks += 1

                db.commit()

            finally:

                db.close()


    # ==================================================
    # GET STATISTICS
    # ==================================================

    def get_stats(self):

        with self._lock:

            db = SessionLocal()

            try:

                statistics = (
                    db.query(Statistics)
                    .filter(
                        Statistics.id == 1
                    )
                    .first()
                )

                total_successful = (
                    statistics.successful_automations
                    + statistics.successful_corrections
                    + statistics.successful_rollbacks
                )

                total_failed = (
                    statistics.failed_automations
                    + statistics.failed_corrections
                    + statistics.failed_rollbacks
                )

                return {

                    "automations":
                        statistics.automations,

                    "successful":
                        total_successful,

                    "failed":
                        total_failed,

                    "ai_corrections":
                        statistics.ai_corrections,

                    "successful_automations":
                        statistics.successful_automations,

                    "failed_automations":
                        statistics.failed_automations,

                    "successful_corrections":
                        statistics.successful_corrections,

                    "failed_corrections":
                        statistics.failed_corrections,

                    "rollbacks":
                        statistics.rollbacks,

                    "successful_rollbacks":
                        statistics.successful_rollbacks,

                    "failed_rollbacks":
                        statistics.failed_rollbacks
                }

            finally:

                db.close()


stats_service = StatsService()