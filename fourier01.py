import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftshift

# this is the number of points used to plot the analytically calculated Fourier Transform
N0 = 2048
tRange = 8 * np.arange(-N0, N0) * (1 / N0)
fRange = 0.125 * np.arange(-N0, N0) * (1 / (len(tRange) / N0))
tau = 0.25
g = np.exp(-(tRange**2) / tau**2)
G = np.exp(-np.pi**2 * fRange**2 * tau**2) * tau * np.sqrt(np.pi)

# Number of samples 
N = 24
tStep = 2 / N
tSpan = N * tStep
fStep = 1 / tSpan
fSpan = N * fStep

tSamples = np.arange(-np.floor(N / 2), np.ceil(N / 2)) * tStep
gSamples = np.exp(-(tSamples**2) / tau**2)
fSamples = np.arange(-np.floor(N / 2), np.ceil(N / 2)) * fStep
GSamples = fftshift(fft(gSamples))

GSamplesCalc = np.exp(-np.pi**2 * fSamples**2 * tau**2) * tau * np.sqrt(np.pi)
gReconst = np.zeros_like(tRange, dtype=complex)
for i in range(N):
    gReconst = gReconst + GSamplesCalc[i] * np.exp(
        1j * 2 * np.pi * fSamples[i] * tRange
    )
GReconst = np.zeros_like(tRange, dtype=complex)
for i in range(N):
    GReconst = GReconst + gSamples[i] * np.exp(-1j * 2 * np.pi * tSamples[i] * fRange)*tStep

# Plot 
plt.figure(figsize=(8, 4.5))

# Time domain 
plt.subplot(2, 1, 1)
plt.plot(tRange, g, color="midnightblue", label = r"function $g(t)$")
plt.xlabel("$t$ (s)")
plt.ylabel("$g(t)$")
plt.plot(tSamples, gSamples, "o", color="firebrick", markersize=6, label = "Samples")
# plt.plot(tRange, np.real((gReconst*fStep)))
plt.xlim(-2.0, 2.0)
plt.legend()

# Frequency domain
plt.subplot(2, 1, 2)
plt.plot(fRange, np.abs(G), label = "Fourier transform")
plt.plot(fRange, np.abs(GReconst), label = "DTFT")
plt.plot(fSamples, np.abs(GSamples * tStep), "o", color="steelblue", markersize=6, label = "DFT")
plt.xlim(-10, 10)
plt.xlabel(r"$\nu$ (Hz)")
plt.ylabel(r"$|G(\nu)|$")
plt.legend()

plt.suptitle("Sampling rate {:.2f} samples per second".format(1/tStep))
plt.tight_layout()
plt.savefig("fourier.png", dpi = 150)