from ..connector.client import BaseConnector
import re

class CheckGempa:
  def __init__(self) -> None:
    self.connector = BaseConnector
    self.api = 'https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json'
    self._Tanggal: str
    self._Jam: str
    self._DateTime: str
    self._Coordinates: str
    self._Lintang: str
    self._Bujur: str
    self._Magnitude: str
    self._Kedalaman: str
    self._Wilayah: str
    self._Potensi: str
    self._Dirasakan: str
    self._Shakemap: str
  async def __aenter__(self):
    async with self.connector.get(self.api) as self.client:
      updater = self.client.raw['result']['gempa']
      if self.client.status_code == 200:
        self._Tanggal = updater.get('Tanggal', 'no-Tanggal')
        self._Jam = updater.get('Jam', 'no-Jam')
        self._DateTime = updater.get('DateTime', 'no-DateTime') 
        self._Coordinates = updater.get('Coordinates', 'no-Coordinates')
        self._Lintang = updater.get('Lintang', 'no-Lintang')
        self._Bujur = updater.get('Bujur', 'no-Bujur')
        self._Magnitude = updater.get('Magnitude', 'no-Magnitude')
        self._Kedalaman = updater.get('Kedalaman', 'no-Kedalaman')
        self._Wilayah = updater.get('Wilayah', 'no-Wilayah')
        self._Potensi = updater.get('Potensi', 'no-Potensi')
        self._Dirasakan = updater.get('Dirasakan', 'no-Dirasakan')
        self._Shakemap = f"{re.sub('autogempa.json', '', self.api)}/{updater.get('Shakemap', 'no-Shakemap')}"
        print(self._Shakemap)
      return self
  async def __aexit__(self, exc_type, exc, tb):
    if self.client:
      await self.client.close()
  @property
  def Tanggal(self):
    return self._Tanggal
  @property
  def Jam(self):
    return self._Jam
  @property
  def DateTime(self):
    return self._DateTime
  @property
  def Coordinates(self):
    return self._Coordinates
  @property
  def Lintang(self):
    return self._Lintang
  @property
  def Bujur(self):
    return self._Bujur
  @property
  def Magnitude(self):
    return self._Magnitude
  @property
  def Kedalaman(self):
    return self._Kedalaman
  @property
  def Wilayah(self):
    return self._Wilayah
  @property
  def Potensi(self):
    return self._Potensi
  @property
  def Dirasakan(self):
    return self._Dirasakan
  @property
  def Shakemap(self):
    return self._Shakemap
