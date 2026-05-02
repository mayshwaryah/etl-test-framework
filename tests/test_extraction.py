from utils.sqlquerycheck import *
from utils.logger import get_logger

logger = get_logger()


def test_no_missing_records():
    result = run_query("""
        SELECT COUNT(*)
        FROM source_db.sales_raw s
        LEFT JOIN staging_db.sales_raw t
          ON s.order_id = t.order_id
        WHERE t.order_id IS NULL
    """)

    count = result[0][0]

    assert count == 0, f" Missing records count: {count}"
