import time

class ExecutionTime:
  def __init__(self) -> None:
    self._hours = 0
    self._minutes = 0
    self._seconds = 0
  def __enter__(self):
    self.start = time.perf_counter()
    return self
  def __exit__(self, exc_type, exc_val, exc_tb) -> None:
    end = time.perf_counter()
    result = int(end - self.start)
    self._hours, remainder = divmod(result, 3600)
    self._minutes, self._seconds = divmod(remainder, 60)
  @property
  def hours(self) -> int:
    return int(self._hours)
  @property
  def minutes(self) -> int:
    return int(self._minutes)
  @property
  def seconds(self) -> int:
    return int(self._seconds)