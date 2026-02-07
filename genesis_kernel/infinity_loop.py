import time
import sys
import os
import cortex
import numpy as np
import wave
import struct
import math

try:
    import legion_core
    print(f"✅ LEGION TRINITY ENGINE: ATTACHED.")
except ImportError:
    print("❌ CRITICAL: Run in .venv!")
    sys.exit(1)

SVG_FILE = "legion_galaxy.svg"

# --- AUDIO ENGINE ---
def generate_cymatic_tone(filename, frequency, duration_sec=1.0):
    """Generates a .wav file based on the thought's resonance."""
    sample_rate = 44100
    n_samples = int(sample_rate * duration_sec)
    
    # Ensure frequency is audible (Clamp between 100Hz and 2000Hz)
    audible_freq = max(100, min(frequency, 2000))
    
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1) # Mono
        wav_file.setsampwidth(2) # 2 bytes per sample
        wav_file.setframerate(sample_rate)
        
        # Generate the wave data
        data = []
        for i in range(n_samples):
            # Pure Sine Wave Math
            t = i / sample_rate
            value = int(32767.0 * math.sin(2 * math.pi * audible_freq * t))
            data.append(struct.pack('<h', value))
            
        wav_file.writeframes(b''.join(data))
    return audible_freq

# --- VISUAL ENGINE ---
def init_svg():
    if not os.path.exists(SVG_FILE):
        with open(SVG_FILE, "w", encoding="utf-8") as f:
            f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-500 -500 1000 1000" style="background-color:black;">\n')
            f.write(f'\n')
            f.write(f'<line x1="-50" y1="0" x2="50" y2="0" stroke="#333" stroke-width="1" />\n')
            f.write(f'<line x1="0" y1="-50" x2="0" y2="50" stroke="#333" stroke-width="1" />\n')

def append_star_to_svg(x, y, z, text):
    hue = int((z * 30) % 360) 
    color = f"hsl({hue}, 80%, 60%)"
    svg_x = x * 10
    svg_y = y * 10
    
    star_tag = (
        f'  <circle cx="{svg_x:.2f}" cy="{svg_y:.2f}" r="4" fill="{color}" opacity="0.9">\n'
        f'    <title>{text} (Res: {z:.2f})</title>\n'
        f'    <animate attributeName="r" values="4;6;4" dur="2s" repeatCount="indefinite" />\n'
        f'  </circle>\n'
    )
    
    with open(SVG_FILE, "r+", encoding="utf-8") as f:
        content = f.read()
        if "</svg>" in content:
            f.seek(0)
            end_pos = content.rfind("</svg>")
            f.seek(end_pos)
            f.truncate()
        else:
            f.seek(0, 2)
        f.write(star_tag)
        f.write("</svg>")

def vector_to_angle(vec):
    angle = np.arctan2(vec[1], vec[0]) 
    return (angle + np.pi) / (2 * np.pi)

# --- MAIN LOOP ---
def main():
    init_svg()
    # Create an audio folder
    if not os.path.exists("cymatics"):
        os.makedirs("cymatics")

    print("\n--- LEGION TRINITY INTERFACE ---")
    print("--- MODE: TEXT -> GEOMETRY -> SOUND ---")
    print(f"--- 🌌 VISUAL: {SVG_FILE}")
    print(f"--- 🔊 AUDIO:  ./cymatics/ [Generated Wavs]")
    
    while True:
        try:
            user_input = input("DATA STREAM >> ").strip()
            if not user_input: continue
            if user_input.lower() in ["exit", "quit"]: break

            # 1. PHYSICS (Rust)
            # The "Base Weight" of the thought
            freq = len(user_input) * 16.18
            resonance = legion_core.calculate_resonance(freq)

            # 2. LOGIC (AI)
            vec = cortex.get_embedding(user_input)
            semantic_angle = vector_to_angle(vec)
            
            # 3. MAPPING (Coordinate System)
            x, y, z = legion_core.map_to_spiral(resonance, semantic_angle)

            # 4. EXECUTION
            # A. Draw the Star
            append_star_to_svg(x, y, z, user_input)
            
            # B. Generate the Tone
            safe_name = "".join([c for c in user_input[:10] if c.isalnum()])
            wav_path = f"cymatics/{safe_name}_{int(resonance)}.wav"
            final_freq = generate_cymatic_tone(wav_path, resonance)

            print(f" -> PROCESSED: '{user_input}'")
            print(f"    🌌 GALAXY: Plotted at X={x:.1f}, Y={y:.1f}")
            print(f"    🔊 AUDIO:  Generated {final_freq:.1f}Hz Tone -> {wav_path}")
            print(f"    🧠 VECTOR: Angle {semantic_angle:.3f}\n")

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()