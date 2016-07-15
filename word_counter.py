class WordCounter():
  _content = ''
  _encoding = 'utf-8'
  _method = ''
  TYPE_CHAR, TYPE_WORD = range(2)
  @classmethod
  def set_content(cls, _content):
    cls._content = _content
    return cls

  # @classmethod
  # def set_encoding(cls, _encoding):
  #   cls._encoding = _encoding
  #   return cls

  @classmethod
  def character(cls):
    cls._method = WordCounter.TYPE_CHAR
    return cls

  @classmethod
  def word(cls):
    cls._method = WordCounter.TYPE_WORD
    return cls

  @classmethod
  def count(cls):
    if (cls._method == WordCounter.TYPE_CHAR):
      return cls._count_char()
    else:
      return cls._count_word()

  @classmethod
  def _count_char(cls):
    content = cls._content
    chi = re.sub(r"[a-zA-Z0-9 ]+", '', cls._content)
    total = len(content)-len(chi)/3
    return (chi, total)
