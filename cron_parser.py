from croniter import croniter
from datetime import datetime

def parse_cron(cron_expr, count=5):
    try:
        base = datetime.now()
        iter = croniter(cron_expr, base)
        return [iter.get_next(datetime).isoformat() for _ in range(count)]
    except Exception as e:
        return {"error": str(e)}
