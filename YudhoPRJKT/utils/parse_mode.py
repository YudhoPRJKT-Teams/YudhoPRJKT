class ParseMode(str):
  @classmethod
  def Markdown(cls):
    """Return ParseMode Markdown"""
    return cls('Markdown')
  @classmethod
  def MarkdownV2(cls):
    """Return ParseMode MarkdownV2"""
    return cls('MarkdownV2')
  @classmethod
  def HTML(cls):
    """Return ParseMode HTML"""
    return cls('HTML')