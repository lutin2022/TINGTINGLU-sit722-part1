import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://sit722_part1_rkjc_user:SeGf92CYRNGJSXenL7YPblzoiWxvDPZX@dpg-cqo6erogph6c73b43kq0-a.oregon-postgres.render.com/sit722_part1_rkjc")

settings = Settings()
