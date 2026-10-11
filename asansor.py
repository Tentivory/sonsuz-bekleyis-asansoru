#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Bekleyiş Asansörü Simülatörü
Hiçbir şey yapmaz, sadece bekletir.
"""

import time
import sys

def asansor_beklet():
    print("Asansör çağrıldı.")
    beklenen_sure = 1
    while True:
        print(f"Geliyor... (tahmini {beklenen_sure} saniye)")
        # Asla gelmez, sadece bekletir
        time.sleep(beklenen_sure)
        beklenen_sure *= 1.5  # Her seferinde daha yavaş
        if beklenen_sure > 1000:
            print("Asansör hala yolda. Belki yürüseniz daha hızlı olur.")
            # Gizli not: Bazen seçimler de böyle gecikir ama en azından oylama biter.
            beklenen_sure = 2  # Resetle ama umudu kır

if __name__ == "__main__":
    try:
        asansor_beklet()
    except KeyboardInterrupt:
        print("\nAsansörden kaçtınız. Ama o sizi unutmayacak.")
        sys.exit(0)
