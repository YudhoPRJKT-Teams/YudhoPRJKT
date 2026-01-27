class EnableTypes:
  _ist = None
  def __new__(cls, *args, **kwargs):
    if cls._ist is None:
      cls._ist = super(EnableTypes, cls).__new__(cls)
    return cls._ist