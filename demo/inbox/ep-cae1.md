# Engineering Physics (EP) — CAE-1 Study Notes (Units 1–3)

> **Units as taught in class (confirmed): Unit 1 LASERS · Unit 2 Band Theory of Solids · Unit 3 Physics of Semiconductors.**

---

# Unit 1: LASERS


> LASER = **Light Amplification by Stimulated Emission of Radiation** — an intense, highly directional, monochromatic, coherent beam of light.

---

## 1. Interaction of Radiation with Matter

Atoms have discrete energy levels: ground E1 and excited E2 (E2 > E1). Light of frequency ν with hν = E2 − E1 interacts in 3 ways:

### (a) Absorption
- Atom in E1 absorbs a photon of energy hν = E2 − E1 → jumps to E2.
- Rate ∝ N1 (ground-state atoms) and energy density ρ.

### (b) Spontaneous Emission
- Atom in E2 falls to E1 **by itself** — photon emitted in **random direction, random phase** → **incoherent** (like a bulb).
- Rate ∝ N2.

### (c) Stimulated Emission
- An incoming photon of energy hν = E2 − E1 hits an atom in E2 → atom drops to E1 emitting a **second photon identical** to the first (same frequency, phase, direction, polarization).
- **One photon in → two photons out.** This cloning process is the basis of laser action.
- Rate ∝ N2 and ρ.

---

## 2. Characteristics of Laser Light

| Property | Ordinary light | Laser light |
|---|---|---|
| Direction | Spreads everywhere | Highly directional (narrow beam) |
| Colour | Many wavelengths | Monochromatic (single λ) |
| Coherence | Incoherent | Coherent — spatial + temporal |
| Intensity | Low | Very high |
| Divergence | Large | Very small |

### Spatial vs temporal coherence
- **Temporal coherence:** the phase stays correlated **along the beam over time** — the wave keeps the same frequency/phase over a long distance (long coherence length). Ordinary light has coherence length ~ mm; lasers ~ metres to km.
- **Spatial coherence:** the phase is correlated **across the beam cross-section** — the wavefront is uniform, so the beam stays tight and can be focused to a tiny spot.

---

## 3. Population Inversion and Pumping

- Normally N1 > N2 (Boltzmann distribution). A laser needs **N2 > N1** → **population inversion**, so stimulated emission beats absorption.
- **Pumping** = raising atoms to the excited state. Methods: optical (flash lamp), electrical discharge, injection (forward current).
- **Metastable state:** a long-lived (~10⁻³ s) excited state where atoms pile up, making inversion possible — the "waiting room".

### Basic requirements of a laser
1. **Active medium** (gain medium) with a metastable upper level.
2. **Pumping mechanism** to create population inversion.
3. **Optical resonator (cavity)** — two parallel mirrors (one fully, one partially reflecting); photons bounce back and forth, get amplified by stimulated emission, and a beam escapes through the partial mirror.

---

## 4. Einstein's Coefficients and Significance

- **A21** — spontaneous emission probability per unit time.
- **B21** — stimulated emission probability.
- **B12** — absorption probability.

Einstein derived (at thermal equilibrium):

```
B12 = B21
A21 / B21 = 8πhν³ / c³
```

**Significance:** B12 = B21 proves stimulated emission must exist alongside absorption; the A/B ratio ∝ ν³ shows spontaneous emission dominates at high frequencies — so visible/UV lasers need strong pumping, and explains why the maser (microwave, low ν) came first.

---

## 5. Types of Lasers

### (a) Ruby Laser (solid-state)
- Active medium: ruby crystal (Al₂O₃:Cr³⁺); pumping: xenon flash lamp (3-level system); λ = 694.3 nm (red), **pulsed** output.
- Uses: holography, range finding.

### (b) He-Ne Laser (gas laser) — syllabus emphasis
- Active medium: He:Ne = 10:1 gas mixture in a discharge tube.
- Pumping: electrical discharge excites He to metastable states; He* collides with Ne, transferring energy → Ne* lases to a lower level.
- λ = 632.8 nm (red), **continuous wave (CW)**, low power (mW), cheap, reliable.
- Uses: barcode scanners, lab alignment, interferometry.

### (c) Semiconductor Diode Laser (injection laser) — syllabus emphasis
- Active medium: p-n junction of a **direct-bandgap** semiconductor (e.g., GaAs).
- Pumping: forward-bias current injects electrons and holes; recombination across the band gap emits photons.
- Tiny, efficient, CW; λ typically 700–1600 nm (IR).
- Uses: fiber-optic communication, CD/DVD/Blu-ray, laser pointers, laser printers.

---

## 6. Branch-Specific Applications of Lasers

- **CSE/IT:** fiber-optic communication (data as laser pulses), optical storage (CD/DVD/Blu-ray), laser printers, barcode/RFID scanning.
- **Mechanical/Civil:** laser cutting, welding, drilling; 3D scanning/LIDAR surveying; alignment in construction.
- **Electrical/Electronics:** photolithography in chip fabrication, laser trimming of circuits, holography.
- **Medical:** LASIK eye surgery, laser therapy, precise tissue cutting.
- **Research/Defence:** spectroscopy, nuclear fusion experiments, target designation, range finding.

---

## 7. Pulsed Laser Deposition (PLD)

- A **high-power pulsed laser** (e.g., excimer/UV) is focused onto a target inside a vacuum chamber.
- Each pulse **ablates** (vaporizes) a tiny amount of target material, forming a plasma plume that deposits as a **thin film** on a substrate.
- Used to grow high-quality thin films (superconductors, ferroelectrics, oxides) for electronics and research.

---

## 8. Important Formulas (Unit 1)

```
Photon energy:        E = hν = hc / λ
Population inversion: N2 > N1 (required for lasing)
Einstein relations:   B12 = B21 ;  A21 / B21 = 8πhν³ / c³
Threshold condition:  gain ≥ losses in the cavity
```

---

## 9. Likely CAE Questions (Unit 1) with short answers

**Q1. Distinguish spontaneous and stimulated emission. Why is stimulated emission essential for lasers?**
Spontaneous emission is random in direction/phase → incoherent light. Stimulated emission produces an exact copy of the triggering photon (same frequency, phase, direction) → coherent, amplifiable light. Only stimulated emission can amplify light, so it is the basis of laser action.

**Q2. Explain spatial and temporal coherence of laser light.**
Temporal coherence = phase correlation along the beam over time (long coherence length, single frequency). Spatial coherence = phase correlation across the beam cross-section (uniform wavefront, tight beam, focuses to a tiny spot).

**Q3. What is population inversion? How is it achieved?**
The abnormal condition N2 > N1 (more atoms excited than in ground state), achieved by pumping (optical/electrical/injection). It is needed so stimulated emission dominates absorption and net light amplification occurs.

**Q4. Write Einstein's coefficients and explain their significance.**
A21 (spontaneous), B21 (stimulated emission), B12 (absorption); B12 = B21 and A21/B21 = 8πhν³/c³. The first relation proves stimulated emission exists; the ν³ dependence shows short-wavelength lasers need stronger pumping.

**Q5. Describe the construction and working of a He-Ne laser.**
He:Ne (10:1) gas tube with electrical discharge pumping: electrons excite He to metastable states, He* transfers energy to Ne by collision, Ne* lases at 632.8 nm (red), CW output. Mirrors at the tube ends form the resonator.

**Q6. Explain the working of a semiconductor diode laser and list its applications.**
Forward-bias current injects electrons and holes into a p-n junction of a direct-bandgap semiconductor; recombination across the gap emits photons (700–1600 nm), amplified in the junction cavity. Tiny, efficient, CW — used in fiber communication, optical discs, laser pointers, printers.

**Q7. What is pulsed laser deposition? Give one use.**
A high-power pulsed laser ablates a target in vacuum; the plasma plume deposits as a thin film on a substrate. Used to grow high-quality thin films of superconductors, oxides, and ferroelectrics.

---

## 10. Quick Revision Checklist (Unit 1)

1. LASER = Light Amplification by Stimulated Emission of Radiation.
2. Three processes: absorption, spontaneous emission, stimulated emission (one in → two identical out).
3. Temporal coherence (along beam) vs spatial coherence (across beam).
4. Population inversion (N2 > N1) by pumping; metastable state = waiting room.
5. Einstein: B12 = B21; A21/B21 = 8πhν³/c³ (short λ needs harder pumping).
6. Laser parts: active medium + pump + resonator (two mirrors).
7. He-Ne: gas, discharge pumping, CW 632.8 nm. Diode: p-n junction, forward current, tiny, IR.
8. Branch applications: fiber comm, cutting/welding, photolithography, LASIK, barcodes.
9. PLD: pulsed laser ablates target → thin film on substrate.

---

---

# Unit 2: Band Theory of Solids

> Why some materials conduct and others don't — energy bands, forbidden gaps, Kronig–Penney model, effective mass, Fermi level.

---

> Band theory explains conductors vs semiconductors vs insulators; then intrinsic/extrinsic semiconductors, Hall effect, and optoelectronic devices.

---

## 1. Formation of Energy Bands

- An isolated atom has sharp discrete levels. When **N atoms** form a solid, each level **splits into N closely spaced levels** (Pauli exclusion principle), merging into a continuous **energy band**.
- Allowed bands (valence band, conduction band) are separated by the **forbidden energy gap Eg**.

**Classification of solids:**

| Type | Band gap Eg | Behaviour |
|---|---|---|
| Conductor | 0 (bands overlap / half-filled) | Free electrons, σ ≈ 10⁷ S/m (Cu, Al) |
| Semiconductor | Small, ~0.1–3 eV (Si: 1.1, Ge: 0.7) | Conducts a little at room T; σ ↑ with T |
| Insulator | Large, > 3–5 eV (diamond ~5.5) | ~Zero conductivity |

**Key ideas (qualitative, for CAE):**
- **Kronig–Penney model:** electron in the periodic potential of the crystal lattice → solving Schrödinger's equation gives allowed bands separated by forbidden gaps at Brillouin zone boundaries — the quantum proof that bands exist.
- **E–k diagram:** free electron gives a parabola E = ℏ²k²/2m; in a crystal, gaps open at zone boundaries, splitting it into band branches.
- **Effective mass** m\* = ℏ²/(d²E/dk²) from the E–k curvature; negative curvature at a band top → negative mass → **hole** concept.
- **Fermi energy Ef:** highest filled state at 0 K; generally the level with 50% occupation probability (Fermi–Dirac function f(E) = 1/[exp((E−Ef)/kT)+1]). Lies **inside the band** for conductors, **mid-gap** for intrinsic semiconductors.

---

## 2. Important Formulas (Unit 2)

```
Effective mass:       m* = ℏ² / (d²E/dk²)
Fermi–Dirac:          f(E) = 1 / [exp((E − Ef)/kT) + 1]
Fermi level:          Ef = (Ec + Ev)/2 (intrinsic)
Si band gap:          Eg(Si) ≈ 1.1 eV ;  Eg(Ge) ≈ 0.7 eV
```

## 3. Likely CAE Questions (Unit 2) with short answers

**Q1. Distinguish conductors, semiconductors, and insulators on the basis of band theory.**
Conductors: valence and conduction bands overlap (or half-filled band) → free electrons. Semiconductors: small gap (~0.1–3 eV) that some electrons cross at room temperature. Insulators: large gap (>3–5 eV) electrons cannot cross → no conduction.

**Q2. What is the Kronig–Penney model? What does it establish?**
It models an electron in the periodic potential of the crystal lattice; solving Schrödinger's equation gives allowed energy bands separated by forbidden gaps at Brillouin zone boundaries — the quantum-mechanical proof that energy bands exist.

## 4. Quick Revision Checklist (Unit 2)

1. N atoms → bands; gap sizes: conductor 0 < semiconductor ~1 eV < insulator > 3 eV.
2. Kronig–Penney: periodic potential → bands + gaps (quantum proof).
3. Effective mass m\* = ℏ²/(d²E/dk²); negative at band top = holes.
4. Fermi level: inside band (conductor), mid-gap (intrinsic semiconductor).

---

# Unit 3: Physics of Semiconductors

> Intrinsic and extrinsic semiconductors, Hall effect, and optoelectronic devices.

---

## 1. Intrinsic Semiconductors

- Pure crystal (no impurities). At 0 K → insulator; at room T, thermal energy breaks bonds → each broken bond gives a **free electron + a hole**.
- **n = p = ni** (electron = hole concentration = intrinsic concentration).

---

## 2. Extrinsic Semiconductors (Doping)

- **n-type:** pentavalent impurity (P, As, Sb) → loosely bound 5th electron; majority carriers = **electrons**; donor level just below CB.
- **p-type:** trivalent impurity (B, Al, Ga) → missing bond electron = hole; majority carriers = **holes**; acceptor level just above VB.

### Fermi level
- Intrinsic: **Ef = (Ec + Ev)/2** (mid-gap; from n = p).
- n-type: Ef shifts **up** toward CB. p-type: Ef shifts **down** toward VB.

### Conductivity
```
σ = e (n·μe + p·μh),   ρ = 1/σ,   J = σE
```
Conductivity **increases with temperature** (opposite of metals).

---

## 3. Hall Effect and Hall Coefficient

- A current-carrying semiconductor slab in a **magnetic field ⊥ current** → carriers deflect sideways (Lorentz force) → transverse **Hall voltage VH**:

```
VH = (I · B) / (n · e · t),     RH = 1 / (n·e)
```

- **Sign of RH** tells the carrier type: **negative → n-type (electrons)**, **positive → p-type (holes)**.
- Magnitude gives carrier concentration n = 1/(e·RH); with conductivity, mobility μ = σ·|RH|.

---

## 4. Optoelectronic Devices (Types)

Devices that convert electrical energy ↔ light:

| Device | Conversion | Working idea |
|---|---|---|
| **LED** | electricity → light | Forward-biased p-n junction: electrons + holes recombine across the gap, emitting photons |
| **Photodiode** | light → electricity | Reverse-biased junction: absorbed photons (hν > Eg) create e–h pairs → photocurrent |
| **Solar (photovoltaic) cell** | light → electricity | Junction field separates photo-generated carriers → usable power |
| **Laser diode** | electricity → coherent light | Stimulated emission in a forward-biased junction (see Unit 2) |
| **Photoconductor / optocoupler** | light ↔ resistance/signal | Light changes conductivity; optocouplers transfer signals with electrical isolation |

---

## 5. OLED — Organic Light-Emitting Diode

- **Structure:** thin organic (carbon-based) emissive layer sandwiched between an **anode** (transparent, e.g., ITO) and a **cathode**, on a glass/plastic substrate.
- **Working:** applied voltage injects electrons (cathode) and holes (anode) into the organic layer; they **recombine in the emissive layer**, releasing energy as **photons** (electroluminescence). Colour depends on the organic material.
- **Advantages:** no backlight needed (each pixel emits its own light) → deeper blacks, higher contrast, thinner, flexible/foldable displays, lower power for dark content.
- **Uses:** smartphone displays, OLED TVs, wearables, flexible screens.

---

## 6. Photovoltaic (Solar) Cell

- **Structure:** a large-area **p-n junction** (usually Si) with anti-reflective coating and metal contacts; the junction's built-in field is the key.
- **Working:** photons with **hν > Eg** are absorbed, creating **electron–hole pairs**; the junction's electric field sweeps electrons to the n-side and holes to the p-side → a **photovoltage/photocurrent** appears across the terminals.
- **Key points:** open-circuit voltage, short-circuit current, fill factor and **efficiency** (fraction of incident light power converted); Si cells ~15–25% efficient; cells are series/parallel-connected into panels.
- **Uses:** rooftop solar panels, calculators, satellites, solar farms.

---

## 7. Important Formulas (Unit 3)

```
Intrinsic:            n = p = ni
Conductivity:         σ = e(n·μe + p·μh),  ρ = 1/σ
Hall voltage:         VH = IB / (net)
Hall coefficient:     RH = 1 / (ne)   [sign → carrier type]
Mobility:             μ = σ · |RH|
Barrier potential:    V₀ ≈ 0.7 V (Si), ≈ 0.3 V (Ge)
```

## 8. Likely CAE Questions (Unit 3) with short answers

**Q1. Distinguish intrinsic and extrinsic semiconductors. Where does the Fermi level lie in each?**
Intrinsic is pure (n = p = ni), Ef mid-gap. n-type (pentavalent donors, electrons majority) → Ef shifts up toward CB; p-type (trivalent acceptors, holes majority) → Ef shifts down toward VB.

**Q2. What is the Hall effect? How is the Hall coefficient used?**
Current I with perpendicular B deflects carriers sideways, producing transverse voltage VH = IB/(net). RH = 1/(ne): its sign identifies n-type (−) vs p-type (+); its magnitude gives carrier concentration; with σ it yields mobility (μ = σ·RH).

**Q3. Explain the working of an OLED. Why are OLED displays better than LCDs?**
Electrons and holes injected into an organic emissive layer recombine, emitting photons. Each pixel emits its own light (no backlight) → deeper blacks, higher contrast, thinner and flexible displays.

**Q4. Explain the working principle of a photovoltaic cell.**
Photons with hν > Eg create electron–hole pairs in a p-n junction; the junction's built-in field separates them (electrons to n-side, holes to p-side), producing a voltage and current at the terminals — converting light directly into electrical power.

**Q5. Name the main types of optoelectronic devices and state one function each.**
LED (electricity→light), photodiode (light→current signal), photovoltaic cell (light→power), laser diode (electricity→coherent light), photoconductor/optocoupler (light-controlled conduction / isolated signal transfer).

## 9. Quick Revision Checklist (Unit 3)

1. Intrinsic: n = p = ni. n-type: donors, Ef up. p-type: acceptors, Ef down.
2. σ = e(nμe + pμh); σ ↑ with temperature.
3. Hall: VH = IB/(net); RH = 1/(ne); sign = carrier type.
4. Optoelectronic devices: LED, photodiode, solar cell, laser diode, optocoupler.
5. OLED: organic layer, recombination → light; self-emissive pixels → better contrast, thin, flexible.
6. Photovoltaic cell: hν > Eg creates e–h pairs; junction field separates them → power.

---

# Appendix: Electron Ballistics and Optics

> In the official syllabus book but **not taught in class** — skim only if you have spare time.

---

> Electron ballistics = the study of the motion of electrons under the action of electric and magnetic fields. It is the basis of electron optics: cathode-ray tubes, CRO, electron microscopes.

---

## 1. Force on a Moving Electron — Lorentz Force

An electron (charge −e, mass m, velocity v) in an electric field **E** and magnetic field **B** experiences:

```
F = −e ( E + v × B )
```

- Electric part −eE: pushes the electron **opposite** to the field direction.
- Magnetic part −e(v × B): acts **perpendicular** to both v and B; it never does work, it only changes the **direction** of motion.

---

## 2. Electron in a Uniform Electric Field (qualitative)

- **Parallel to E:** the electron moves with **uniform acceleration** a = eE/m (towards the positive plate).
- **Perpendicular to E (transverse field):** the electron is pulled sideways while drifting forward → the path is a **parabola**, exactly like a projectile under gravity:

```
y = ( e E x² ) / ( 2 m v² )
```

where v = entry velocity, x = distance along the field plates.

This is the principle behind **electrostatic deflection plates** in a CRO.

---

## 3. Electron in a Uniform Magnetic Field (qualitative)

Direction of velocity decides the path:

| Entry angle | Trajectory |
|---|---|
| v ⊥ B (perpendicular) | **Circle** of radius r = mv/(eB); cyclotron frequency ω = eB/m |
| v ∥ B (parallel) | **Straight line** — magnetic force is zero |
| v at angle θ to B | **Helix** — circular motion in the ⊥ plane plus uniform drift along B |

The helical path is the basis of **magnetic focusing** (all electrons leaving a point with slightly different angles re-meet after one pitch).

---

## 4. Bethe's Law (qualitative)

**Bethe's law:** in a purely **electrostatic** field, the trajectory of an electron depends only on the **field distribution and the initial direction** of the electron — **not on the magnitude of its initial velocity** (nor, for a given energy, on its specific charge).

Why it matters: electron paths through electrostatic fields are purely **geometric**, just like light rays through glass — which is why we can build "electron lenses" that behave like optical lenses. This is the founding statement of **electron optics**.

---

## 5. Electron Lens

Devices that focus electron beams, analogous to glass lenses for light.

### (a) Electrostatic lens
- Made of **coaxial cylindrical electrodes** held at different potentials.
- The non-uniform field near the gaps bends electrons towards the axis → **focusing**, like a convex lens.
- Follows Bethe's law: focusing depends on geometry, not electron speed.

### (b) Magnetic lens
- A short **solenoid (coil)** producing an axisymmetric magnetic field.
- Off-axis electrons get a Lorentz force with an inward component → they spiral in and focus; the image is slightly **rotated**.
- Stronger coil current → shorter focal length. Used in electron microscopes.

---

## 6. Electron Microscope (theoretical outline)

- **Idea:** resolution of a microscope is limited by wavelength. Electrons accelerated through voltage V have de Broglie wavelength:

```
λ = h / √(2 m e V)   ≈ 12.3/√V  Å
```

(e.g., ~0.05 Å at 60 kV — thousands of times smaller than visible light, ~5000 Å).
- **Construction:** electron gun (source) → condenser lens (parallel beam) → specimen → objective lens (magnified image) → projector lens (further magnification) → fluorescent screen/photographic plate.
- **Result:** magnification 10⁵–10⁶, resolves atomic-scale detail. Transmission EM images the interior; magnetic lenses focus the beam throughout.

---

## 7. CRO — Cathode Ray Oscilloscope

An instrument that displays fast-changing voltages as waveforms.

### Block diagram (text)
```
Electron gun → Focusing/anodes → Y-plates (vertical) → X-plates (horizontal) → Fluorescent screen
```

### Working
1. **Electron gun:** heated cathode emits electrons; grid controls beam intensity; accelerating anodes give them high velocity (½mv² = eV).
2. **Deflection:** X-plates receive a **sawtooth (time-base)** voltage sweeping the spot left→right at constant speed; Y-plates receive the **signal** voltage, deflecting the beam vertically.
3. The spot traces the **waveform** of the signal on the fluorescent screen.

### Uses
Measure voltage (amplitude), frequency, time period, and phase difference between two signals; display any electrical waveform.

---

## 8. Important Formulas (Appendix)

```
Lorentz force:          F = −e ( E + v × B )
K.E. gained in V:       ½mv² = eV
Circular path (v ⊥ B):  r = mv / (eB),   cyclotron frequency ω = eB / m
Parabolic path (⊥ E):   y = (eE x²) / (2 m v²)
Electron wavelength:    λ = h / √(2meV)
```

---

## 9. Likely CAE Questions (Appendix) with short answers

**Q1. Describe qualitatively the trajectory of an electron in a uniform magnetic field for different orientations of velocity.**
If v ⊥ B: a circle of radius r = mv/(eB). If v ∥ B: a straight line (no force). If v is at an angle θ: a helix — circular motion in the plane ⊥ B plus uniform drift along B.

**Q2. Show that an electron entering a uniform transverse electric field follows a parabolic path.**
Along the plates it moves uniformly (x = vt); perpendicularly it accelerates uniformly (y = ½at², a = eE/m). Eliminating t gives y = (eEx²)/(2mv²) — a parabola, like projectile motion.

**Q3. State Bethe's law and its significance.**
In an electrostatic field, the electron's trajectory depends only on the field distribution and its initial direction, not on the magnitude of its initial velocity. This makes electron paths purely geometric, like light rays — the foundation of electron optics and electron lenses.

**Q4. Explain the action of a magnetic lens and compare it with a glass convex lens.**
A short solenoid's axisymmetric B-field gives off-axis electrons an inward Lorentz force, focusing them to a point (with slight image rotation). Like a convex glass lens it converges a parallel beam to a focus, and stronger excitation (coil current) shortens the focal length.

**Q5. Describe the construction and working of a CRO.**
An electron gun produces and accelerates a beam; Y-plates deflect it vertically with the signal voltage, X-plates sweep it horizontally with a sawtooth time-base voltage; the spot traces the signal's waveform on a fluorescent screen. Used to measure voltage, frequency, and phase.

**Q6. Why does an electron microscope give much higher resolution than an optical microscope?**
Resolution is limited by wavelength. Electrons accelerated at ~60 kV have λ ≈ 0.05 Å (from λ = h/√(2meV)), thousands of times smaller than visible light (~5000 Å), so the electron microscope resolves atomic-scale detail with magnifications up to ~10⁶.

---

## 10. Quick Revision Checklist (Appendix)

1. Lorentz force: F = −e(E + v × B); magnetic part only changes direction.
2. Transverse E → parabolic path (like projectile).
3. v ⊥ B → circle r = mv/eB; v ∥ B → straight line; angled → helix.
4. Bethe's law: electrostatic trajectories depend only on geometry, not speed → electron optics works.
5. Electron lens: electrostatic (cylinder electrodes) and magnetic (solenoid) types both focus like convex lenses.
6. Electron microscope: λ = h/√(2meV); tiny wavelength → huge resolution.
7. CRO: electron gun + X/Y deflection plates + screen; sawtooth time base; used for voltage/frequency/phase.

---
