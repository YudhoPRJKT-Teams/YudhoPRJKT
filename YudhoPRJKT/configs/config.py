from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import json


class AuthManager:
  _key = bytes.fromhex("00112233445566778899aabbccddeeff")
  _filename = "auth.session"
  _PREFIX_MAGIC = b"\x00\xFF\xAA\x55CORRUPT\x00\x13\x37"
  _SUFFIX_MAGIC = b"\xDE\xAD\xBE\xEF"
  _NOISE_HEAD = 256
  _NOISE_TAIL = 256

  @classmethod
  def _encrypt(cls, data: bytes) -> bytes:
    aesgcm = AESGCM(cls._key)
    inner_prefix = os.urandom(32)
    inner_suffix = os.urandom(32)
    payload = inner_prefix + data + inner_suffix

    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, payload, None)
    core = nonce + ct
    head_noise = os.urandom(cls._NOISE_HEAD)
    tail_noise = os.urandom(cls._NOISE_TAIL)

    blob = (
        cls._PREFIX_MAGIC +
        head_noise +
        core +
        tail_noise +
        cls._SUFFIX_MAGIC
    )
    return blob

  @classmethod
  def _decrypt(cls, blob: bytes) -> bytes:
    if not blob.startswith(cls._PREFIX_MAGIC):
      raise ValueError("auth.session corrupted (bad prefix)")
    if not blob.endswith(cls._SUFFIX_MAGIC):
      raise ValueError("auth.session corrupted (bad suffix)")

    blob = blob[len(cls._PREFIX_MAGIC):-len(cls._SUFFIX_MAGIC)]

    if len(blob) <= (cls._NOISE_HEAD + cls._NOISE_TAIL + 12 + 16):
      raise ValueError("auth.session too small / corrupted")

    core = blob[cls._NOISE_HEAD:-cls._NOISE_TAIL]
    nonce = core[:12]
    ct = core[12:]

    aesgcm = AESGCM(cls._key)
    payload = aesgcm.decrypt(nonce, ct, None)

    if len(payload) <= 64:
      raise ValueError("payload too small / corrupted")

    data = payload[32:-32]
    return data

  @classmethod
  def SetupConfig(cls):
    token = input("Input your telegram bot token: ").strip()
    endpoint_selector = input("Use Custom API telegram bots? (y/n): ").strip()
    endpoint = None
    if endpoint_selector == "y":
      prompt_custom_api = input("Input your custom api telegram bots without /bot: ")
      endpoint = f"{prompt_custom_api}/bot{token}"
    elif endpoint_selector == "n":
      endpoint = f"https://api.telegram.org/bot{token}"
    conf = {"token": token, "api": endpoint}
    raw = json.dumps(conf, separators=(",", ":")).encode("utf-8")
    blob = cls._encrypt(raw)
    with open(cls._filename, "wb") as f:
      f.write(blob)

  @classmethod
  def ReadConfig(cls):
    if not os.path.exists(cls._filename):
      cls.SetupConfig()

    try:
      with open(cls._filename, "rb") as f:
        blob = f.read()
      raw = cls._decrypt(blob)
      return json.loads(raw.decode("utf-8"))
    except Exception:
      return {}

  @classmethod
  def WriteConfig(cls, data_value: dict):
    if not os.path.exists(cls._filename):
      cls.SetupConfig()

    cfg = cls.ReadConfig()
    cfg.update(data_value)
    raw = json.dumps(cfg, separators=(",", ":")).encode("utf-8")
    blob = cls._encrypt(raw)
    with open(cls._filename, "wb") as f:
      f.write(blob)
