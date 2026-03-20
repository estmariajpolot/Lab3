import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt
import pandas as pd

archivos = [
    "mujer1.wav", "mujer2.wav", "mujer3.wav",
    "hombre1.wav", "hombre2.wav", "hombre3.wav"
]

cortes = {
    "mujer1.wav":  (0.76, 5.49),
    "mujer2.wav":  (0.5,  5.0),
    "mujer3.wav":  (0.39, 4.88),
    "hombre1.wav": (0.0,  5.24),
    "hombre2.wav": (0.0,  5.09),
    "hombre3.wav": (1.0,  5.0),
}

ventanas_usuario = {
    "mujer1.wav":  2.00,
    "mujer2.wav":  1.80,
    "mujer3.wav":  1.60,
    "hombre1.wav": 0.16,
    "hombre2.wav": 2.00,
    "hombre3.wav": 0.28,
}

# ─────────────────────────────────────────────
# TABLA RESUMEN
# ─────────────────────────────────────────────
resumen = {
    "Archivo":         [],
    "F0 (Hz)":         [],
    "Frec. Media (Hz)":[],
    "Brillo (Hz)":     [],
    "RMS":             [],
    "Ciclos":          [],
    "Jitter abs (s)":  [],
    "Jitter rel (%)":  [],
    "Shimmer abs":     [],
    "Shimmer rel (%)": [],
}

# ─────────────────────────────────────────────
# BUCLE PRINCIPAL
# ─────────────────────────────────────────────
for archivo in archivos:

    # ── Lectura y recorte ──────────────────────
    fs, senal = wavfile.read(archivo)
    senal = senal.astype(float)

    i1, i2 = cortes[archivo]
    senal = senal[int(i1 * fs): int(i2 * fs)]

    # ── Normalización [-1, 1] ──────────────────
    senal = senal / (np.max(np.abs(senal)) + 1e-8)

    print(f"\n{'='*50}")
    print(f"Archivo: {archivo}")
    print(f"  Max: {np.max(senal):.4f}  |  Min: {np.min(senal):.4f}")

    t_full = np.arange(len(senal)) / fs

    # ── Rango de frecuencias según género ─────
    if "hombre" in archivo:
        fmin, fmax = 80, 400
    else:
        fmin, fmax = 150, 500

    # ═══════════════════════════════════════════
    # 1. SEÑAL ORIGINAL
    # ═══════════════════════════════════════════
    plt.figure(figsize=(10, 4))
    plt.plot(t_full, senal, linewidth=0.8)
    plt.title(f"Señal original: {archivo}")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud normalizada")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # ═══════════════════════════════════════════
    # 2. FFT SEÑAL ORIGINAL
    # ═══════════════════════════════════════════
    N_orig = len(senal)
    fft_orig = np.fft.fft(senal)
    frec_orig = np.fft.fftfreq(N_orig, 1 / fs)[:N_orig // 2]
    mag_orig  = np.abs(fft_orig)[:N_orig // 2]

    plt.figure(figsize=(12, 4))
    plt.semilogx(frec_orig, mag_orig, linewidth=0.8)
    plt.xlim(20, 4000)
    plt.title(f"Espectro señal original: {archivo}")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # ── F0 sobre señal original ────────────────
    idx_f0 = np.where((frec_orig >= fmin) & (frec_orig <= fmax))[0]
    f0_orig = frec_orig[idx_f0[np.argmax(mag_orig[idx_f0])]]
    print(f"  F0 (señal original): {f0_orig:.2f} Hz")

    # ── Características espectrales globales ──
    f_media = np.sum(frec_orig * mag_orig) / (np.sum(mag_orig) + 1e-8)
    brillo  = f_media          # centroide espectral = brillo
    rms     = np.sqrt(np.mean(senal ** 2))

    print(f"  Frecuencia media (brillo/centroide): {f_media:.2f} Hz")
    print(f"  Intensidad RMS: {rms:.4f}")

    # ═══════════════════════════════════════════
    # 3. FILTRO PASA-BANDA
    # ═══════════════════════════════════════════
    nyquist = fs / 2
    b, a = butter(4, [fmin / nyquist, fmax / nyquist], btype='band')
    senal_f = filtfilt(b, a, senal)
    senal_f = senal_f / (np.max(np.abs(senal_f)) + 1e-8)

    # ── Señal original vs filtrada ─────────────
    plt.figure(figsize=(10, 4))
    plt.plot(t_full, senal,   label="Original",  alpha=0.5, linewidth=0.8)
    plt.plot(t_full, senal_f, label="Filtrada",  linewidth=0.9)
    plt.legend()
    plt.title(f"Señal filtrada: {archivo}  [{fmin}–{fmax} Hz]")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud normalizada")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # ═══════════════════════════════════════════
    # 4. FFT SEÑAL FILTRADA
    # ═══════════════════════════════════════════
    N_filt = len(senal_f)
    fft_filt  = np.fft.fft(senal_f)
    frec_filt = np.fft.fftfreq(N_filt, 1 / fs)[:N_filt // 2]
    mag_filt  = np.abs(fft_filt)[:N_filt // 2]

    plt.figure(figsize=(12, 4))
    plt.semilogx(frec_filt, mag_filt, linewidth=0.8, color='tab:orange')
    plt.xlim(20, 4000)
    plt.title(f"Espectro señal filtrada: {archivo}")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # ═══════════════════════════════════════════
    # 5. VENTANA SOBRE SEÑAL FILTRADA
    # ═══════════════════════════════════════════
    ventana_ms = 60
    Nw = int(fs * ventana_ms / 1000)
    idx_inicio = int(ventanas_usuario[archivo] * fs)

    # Seguridad: que la ventana no se salga
    idx_inicio = min(idx_inicio, len(senal_f) - Nw - 1)

    plt.figure(figsize=(10, 4))
    plt.plot(t_full, senal_f, linewidth=0.8)
    plt.axvspan(idx_inicio / fs, (idx_inicio + Nw) / fs,
                color='red', alpha=0.3, label="Ventana 60 ms")
    plt.legend()
    plt.title(f"Señal filtrada + ventana: {archivo}")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud normalizada")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # ── Extraer ventana ────────────────────────
    ventana = senal_f[idx_inicio: idx_inicio + Nw]
    t_win   = np.arange(len(ventana)) / fs

    # ═══════════════════════════════════════════
    # 6. FFT DE LA VENTANA  ← NUEVA GRÁFICA
    # ═══════════════════════════════════════════
    N_win    = len(ventana)
    fft_win  = np.fft.fft(ventana)
    frec_win = np.fft.fftfreq(N_win, 1 / fs)[:N_win // 2]
    mag_win  = np.abs(fft_win)[:N_win // 2]

    # F0 a partir de la ventana
    idx_win = np.where((frec_win >= fmin) & (frec_win <= fmax))[0]
    f0_ventana = frec_win[idx_win[np.argmax(mag_win[idx_win])]]
    print(f"  F0 (ventana): {f0_ventana:.2f} Hz")

    plt.figure(figsize=(12, 4))
    plt.semilogx(frec_win, mag_win, linewidth=0.9, color='tab:green')
    plt.axvline(f0_ventana, color='red', linestyle='--',
                label=f"F0 = {f0_ventana:.1f} Hz")
    plt.xlim(20, 4000)
    plt.title(f"Espectro de la ventana (60 ms): {archivo}")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # ═══════════════════════════════════════════
    # 7. DETECCIÓN DE PICOS Y CICLOS
    # ═══════════════════════════════════════════
    periodo = int(fs / f0_ventana) if f0_ventana > 0 else int(fs / 200)
    desfase = int(periodo * 0.2)

    picos_idx = []
    picos_amp = []

    i = desfase
    while i + periodo < len(ventana):
        segmento  = ventana[i: i + periodo]
        idx_local = np.argmax(segmento)
        picos_idx.append(i + idx_local)
        picos_amp.append(segmento[idx_local])
        i += periodo

    tiempos   = np.array(picos_idx) / fs
    picos_amp = np.array(picos_amp)
    print(f"  Ciclos detectados: {len(picos_idx)}")

    plt.figure(figsize=(8, 3))
    plt.plot(t_win, ventana, linewidth=0.9)
    plt.plot(tiempos, picos_amp, "ro", markersize=5, label="Picos")
    plt.legend()
    plt.title(f"Detección de picos (ventana): {archivo}")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # ═══════════════════════════════════════════
    # 8. JITTER & SHIMMER
    # ═══════════════════════════════════════════
    Ti = np.diff(tiempos)
    Ai = picos_amp

    # Filtrar outliers en periodos (±2σ)
    Ti = Ti[np.abs(Ti - np.mean(Ti)) < 2 * np.std(Ti)]

    # Jitter
    jitter_abs = np.mean(np.abs(np.diff(Ti)))
    jitter_rel = (jitter_abs / np.mean(Ti)) * 100

    # Shimmer
    shimmer_abs = np.mean(np.abs(np.diff(Ai)))
    shimmer_rel = (shimmer_abs / np.mean(np.abs(Ai))) * 100

    print(f"  Jitter  abs: {jitter_abs:.6f} s  |  rel: {jitter_rel:.4f} %")
    print(f"  Shimmer abs: {shimmer_abs:.6f}    |  rel: {shimmer_rel:.4f} %")

    # ── Guardar en resumen ─────────────────────
    resumen["Archivo"].append(archivo)
    resumen["F0 (Hz)"].append(round(f0_ventana, 2))
    resumen["Frec. Media (Hz)"].append(round(f_media, 2))
    resumen["Brillo (Hz)"].append(round(brillo, 2))
    resumen["RMS"].append(round(rms, 4))
    resumen["Ciclos"].append(len(picos_idx))
    resumen["Jitter abs (s)"].append(round(jitter_abs, 6))
    resumen["Jitter rel (%)"].append(round(jitter_rel, 4))
    resumen["Shimmer abs"].append(round(shimmer_abs, 6))
    resumen["Shimmer rel (%)"].append(round(shimmer_rel, 4))


# ═══════════════════════════════════════════════
# TABLA RESUMEN FINAL
# ═══════════════════════════════════════════════
df = pd.DataFrame(resumen)
df["Género"] = df["Archivo"].apply(lambda x: "Mujer" if "mujer" in x else "Hombre")

print("\n" + "=" * 70)
print("TABLA RESUMEN DE PARÁMETROS ESPECTRALES")
print("=" * 70)
print(df.drop(columns=["Género"]).to_string(index=False))

# ═══════════════════════════════════════════════
# BOXPLOTS COMPARATIVOS HOMBRES vs MUJERES
# ═══════════════════════════════════════════════
parametros = [
    ("F0 (Hz)",          "Frecuencia Fundamental F0 (Hz)"),
    ("Frec. Media (Hz)", "Frecuencia Media / Brillo (Hz)"),
    ("RMS",              "Intensidad RMS"),
    ("Jitter rel (%)",   "Jitter relativo (%)"),
    ("Shimmer rel (%)",  "Shimmer relativo (%)"),
]

fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle("Comparación Hombres vs Mujeres — Parámetros Espectrales",
             fontsize=14, fontweight='bold')

for ax, (col, titulo) in zip(axes.flatten(), parametros):
    mujeres  = df[df["Género"] == "Mujer"][col].values
    hombres  = df[df["Género"] == "Hombre"][col].values
    bp = ax.boxplot([mujeres, hombres],
                    labels=["Mujer", "Hombre"],
                    patch_artist=True,
                    medianprops=dict(color='black', linewidth=2))
    bp['boxes'][0].set_facecolor('#f4a0b0')   # rosa para mujeres
    bp['boxes'][1].set_facecolor('#a0c4f4')   # azul para hombres
    ax.set_title(titulo, fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.6)

axes.flatten()[-1].axis("off")   # ocultar subplot sobrante
plt.tight_layout()
plt.show()

# ═══════════════════════════════════════════════
# GRÁFICO DE BARRAS AGRUPADAS — F0 por archivo
# ═══════════════════════════════════════════════
colores = ['#e07b9a' if 'mujer' in a else '#5b9bd5' for a in df["Archivo"]]

plt.figure(figsize=(10, 5))
bars = plt.bar(df["Archivo"], df["F0 (Hz)"], color=colores, edgecolor='black', linewidth=0.7)
plt.title("Frecuencia Fundamental F0 por grabación", fontsize=13)
plt.ylabel("F0 (Hz)")
plt.xlabel("Archivo")
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Etiquetas de valor encima de cada barra
for bar, val in zip(bars, df["F0 (Hz)"]):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
             f"{val:.0f}", ha='center', va='bottom', fontsize=9)

# Leyenda manual
from matplotlib.patches import Patch
leyenda = [Patch(facecolor='#e07b9a', label='Mujer'),
           Patch(facecolor='#5b9bd5', label='Hombre')]
plt.legend(handles=leyenda)
plt.tight_layout()
plt.show()

print("\nAnálisis completado.")


#%%

archivos = [
    "mujer1.wav", "mujer2.wav", "mujer3.wav",
    "hombre1.wav", "hombre2.wav", "hombre3.wav"
]

cortes = {
    "mujer1.wav":  (0.76, 5.49),
    "mujer2.wav":  (0.5,  5.0),
    "mujer3.wav":  (0.39, 4.88),
    "hombre1.wav": (0.0,  5.24),
    "hombre2.wav": (0.0,  5.09),
    "hombre3.wav": (1.0,  5.0),
}

resumen = {
    "Archivo": [],
    "SNR (dB)": [],
}

for archivo in archivos:

    fs, senal = wavfile.read(archivo)
    senal = senal.astype(float)

    i1, i2 = cortes[archivo]

    idx_inicio = int(i1 * fs)
    idx_fin    = int(i2 * fs)

    # Definición de ruido y señal
    ruido = senal[:idx_inicio]
    senal_util = senal[idx_inicio:idx_fin]

    # Potencias
    if len(ruido) > 0:
        potencia_ruido = np.mean(ruido**2)
    else:
        potencia_ruido = 1e-10

    potencia_senal = np.mean(senal_util**2)

    # SNR
    snr = 10 * np.log10(potencia_senal / (potencia_ruido + 1e-10))

    # Guardar
    resumen["Archivo"].append(archivo)
    resumen["SNR (dB)"].append(round(snr, 2))

# Tabla final
df = pd.DataFrame(resumen)
df["Género"] = df["Archivo"].apply(lambda x: "Mujer" if "mujer" in x else "Hombre")

print("\nSNR POR ARCHIVO")
print(df.to_string(index=False))

# Promedios
mujeres = df[df["Género"]=="Mujer"]["SNR (dB)"]
hombres = df[df["Género"]=="Hombre"]["SNR (dB)"]

print("\nPROMEDIOS SNR")
print(f"Mujeres: {np.mean(mujeres):.2f} dB")
print(f"Hombres: {np.mean(hombres):.2f} dB")