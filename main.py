from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/stats")
def get_stats():
    # Worldometers verilerine dayanan saniyelik yaklaşık oranlar:
    # Doğum hızı: Saniyede ~4.3 bebek
    # Ölüm hızı: Saniyede ~1.9 kişi
    # Net nüfus artışı: Saniyede ~2.4 kişi
    
    return {
        "base_pop": 8190000000,          # Toplam nüfus başlangıç
        "births_today_base": 145000,     # Günün bu saatine kadar ortalama doğum
        "deaths_today_base": 62000,      # Günün bu saatine kadar ortalama ölüm
        "rates": {
            "pop_sec": 2.42,
            "birth_sec": 4.35,
            "death_sec": 1.93
        },
        "timestamp": time.time()
    }