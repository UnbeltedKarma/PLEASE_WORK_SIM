import pylab as p
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
# We're using st.components.v1.html instead of streamlit_p5
# from streamlit_p5 import sketch
import random
import plotly.graph_objects as go
import math as Math

from pyparsing import oneOf

# Section 1:

st.set_page_config(page_title="Fine-Tuning the Universe", layout="centered", page_icon="🌌")

st.title("🌌 Fine-Tuning the Universe")
st.subheader("Tweak the **fundamental constants** of physics and see if the universe remains life-permitting.")
st.write("By Brody Bennett - For Physical Science")

# Sidebar for Sliders
st.sidebar.header("🔧 **Fundamental Constants**")
st.sidebar.text("(Loosely Relative Values; 1 = Reality)")


# Function to reset values
def reset_to_real_universe():
    # This resets the session state values for all sliders
    st.session_state.gravity = 1.0
    st.session_state.em_force = 1.0
    st.session_state.strong = 1.0
    st.session_state.lambda_val = 1.0


# Add the reset button to the sidebar
st.sidebar.button("🔄 Reset to Real Universe", on_click=reset_to_real_universe)

# Initialize session state for slider values if they don't exist
if 'gravity' not in st.session_state:
    st.session_state.gravity = 1.0
if 'em_force' not in st.session_state:
    st.session_state.em_force = 1.0
if 'strong' not in st.session_state:
    st.session_state.strong = 1.0
if 'lambda_val' not in st.session_state:
    st.session_state.lambda_val = 1.0

# Updated sliders that use session_state
G = st.sidebar.slider("Gravitational Constant (G)", 0.1, 10.0, st.session_state.gravity, key="gravity", step=0.1)
alpha = st.sidebar.slider("Electromagnetic Force (α)", 0.01, 2.0, st.session_state.em_force, key="em_force", step=0.01)
strong_force = st.sidebar.slider("Strong Nuclear Force", 0.1, 10.0, st.session_state.strong, key="strong", step=0.1)
lambda_const = st.sidebar.slider("Cosmological Constant (Λ)", 0.0, 2.0, st.session_state.lambda_val, key="lambda_val",
                                 step=0.01)

st.markdown("---")
st.header("📏 Real-World Physical Constants")
st.write("Compare your adjustments to the actual measured values in our universe.")

with st.expander("ℹ️ View Real-World Constants", expanded=True):
    # Create a dataframe for better table formatting
    import pandas as pd

    # Define the data
    data = {
        "Constant": [
            "Gravitational Constant (G)",
            "Fine Structure Constant (α)",
            "Strong Nuclear Force Coupling (αs)",
            "Cosmological Constant (Λ)"
        ],
        "Value": [
            "6.674 × 10⁻¹¹ m³/kg·s²",
            "≈ 1/137 (0.007297)",
            "≈ 0.1181 at Z boson mass",
            "≈ 1.1056 × 10⁻⁵²m⁻²"
        ],
        "Significance": [
            "Determines strength of gravity. If altered by just 1 part in 10³⁴, stars suitable for life couldn't exist.",
            "Controls electromagnetic interactions. If changed by just 4%, stellar fusion would be impossible.",
            "Binds nuclei together. A 2% change would prevent stable elements needed for life.",
            "Drives cosmic expansion. Fine-tuned to 1 part in 10¹²⁰, otherwise galaxies couldn't form."
        ]
    }

    # Create and display the dataframe as a styled table
    df = pd.DataFrame(data)
    st.table(df)

    st.info(
        "The sliders in this simulation represent relative values, where 1.0 equals our universe's actual constants.")

# Add a visual representation of the fine-tuning ranges
st.subheader("📊 Fine-Tuning Precision")

fine_tuning_data = {
    "Constant": ["Gravitational Constant (G)", "Fine Structure Constant (α)",
                 "Strong Nuclear Force", "Cosmological Constant (Λ)"],
    "Viable Range": ["±1 part in 10³⁴", "±1 part in 25",
                     "±2%", "±1 part in 10¹²⁰"],
    "Visualization": [0.00000000000000000000000000000001, 0.04, 0.02,
                      0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001]
}

# Create a logarithmic visualization of these incredibly small ranges
import math

# Calculate bars with logarithmic scale for visualization
log_values = []
for val in fine_tuning_data["Visualization"]:
    if val > 0:
        log_val = -math.log10(val)
    else:
        log_val = 0
    log_values.append(log_val)

# Create horizontal bars showing precision (higher = more fine-tuned)
fig, ax = plt.subplots(figsize=(8, 3))
bars = ax.barh(fine_tuning_data["Constant"], log_values, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

# Add labels showing the precision values
for i, bar in enumerate(bars):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
            fine_tuning_data["Viable Range"][i],
            va='center', color='black')

ax.set_xlabel('Fine-Tuning Precision (log scale)')
ax.set_title('Relative Fine-Tuning Precision of Fundamental Constants')
st.pyplot(fig)

st.markdown("""
### What does this mean?

The fundamental constants of physics appear to be incredibly fine-tuned for life to exist:

- **Gravitational Constant**: If G were slightly stronger, stars would burn too quickly for life to evolve. If weaker, stars wouldn't form at all.

- **Fine Structure Constant**: Controls how atoms hold their electrons and interact with light. Small changes would prevent stable atoms or complex chemistry.

- **Strong Nuclear Force**: Holds protons and neutrons together against electromagnetic repulsion. Slight changes would prevent elements heavier than hydrogen or cause all hydrogen to fuse immediately after the Big Bang.

- **Cosmological Constant**: Drives the expansion of space. The observed value is extremely small but positive. If even slightly larger, matter would disperse too quickly for galaxies to form.

This remarkable fine-tuning has led some physicists to propose the Anthropic Principle, which suggests that these values appear fine-tuned because only in such universes could intelligent observers exist to measure them.
""")

st.subheader("Effect of Chaning Constants:")
# Columns for categories
col1, col2 = st.columns(2)

score = 0

with col1:
    st.subheader("🪐 Gravity (G)")
    if G < 0.3:
        st.error("❌ Too weak — No stars or galaxies form.")
    elif G > 3.0:
        st.error("❌ Too strong — Stars collapse quickly.")
    else:
        st.success("✅ Gravity supports stable star formation.")
        score += 1
    with st.expander("What This Means"):
        st.write(
            "Gravity affects how matter clumps together. Too little, and stars never ignite. Too much, and everything collapses rapidly.")

with col2:
    st.subheader("⚡ Electromagnetism (α)")
    if alpha < 0.05:
        st.error("❌ Atoms unstable — chemistry fails.")
    elif alpha > 1.5:
        st.error("❌ Electron orbits collapse.")
    else:
        st.success("✅ Supports stable atoms and chemistry.")
        score += 1
    with st.expander("What This Means"):
        st.write("This force holds atoms together. Tweak it too much, and atoms can't exist.")

with col1:
    st.subheader("💥 Strong Nuclear Force")
    if strong_force < 0.3:
        st.error("❌ No nuclei form — just protons.")
    elif strong_force > 5.0:
        st.error("❌ Hydrogen fuses instantly — stars don't last.")
    else:
        st.success("✅ Enables atomic nuclei and fusion.")
        score += 1
    with st.expander("What This Means"):
        st.write("This force binds protons and neutrons. Without it, matter can't exist beyond hydrogen.")

with col2:
    st.subheader("🌌 Cosmological Constant (Λ)")
    if lambda_const < 0.01:
        st.warning("⚠️ Universe collapses early.")
    elif lambda_const > 1.5:
        st.error("❌ Expands too fast — no galaxies form.")
    else:
        st.success("✅ Balanced cosmic expansion.")
        score += 1
    with st.expander("What This Means"):
        st.write("This controls the expansion of the universe. It must be finely tuned to allow structure to form.")

# Universe Viability Indicator
st.markdown("### 🌟 Universe Viability Score")
status = {
    4: "🟢 Life-Permitting Universe",
    3: "🟡 Marginally Habitable",
    2: "🟠 Highly Unstable",
    1: "🔴 Hostile Universe",
    0: "💀 Completely Inhospitable"
}
st.markdown(f"## {status[score]} ({score}/4)")

# Visualizing Parameter Differences
st.markdown("### 📊 How Far From Home?")
params = ["Gravity (G)", "Electromagnetism (α)", "Strong Force", "Cosmological Const. (Λ)"]
values = [G, alpha, strong_force, lambda_const]
real_values = [1, 1, 1, 1]

fig, ax = plt.subplots(figsize=(6, 3))
bar_width = 0.35
x = np.arange(len(params))
ax.bar(x - bar_width / 2, real_values, bar_width, label='Real Universe')
ax.bar(x + bar_width / 2, values, bar_width, label='Your Universe', color='coral')
ax.set_ylabel("Relative Value (Scaled)")
ax.set_title("Comparison of Constants")
ax.set_xticks(x)
ax.set_xticklabels(params, rotation=15)
ax.legend()
st.pyplot(fig)

# Footer
st.markdown("---")
st.info(
    "These are simplified approximations based on physics insights from cosmology and fine-tuning arguments. In reality, the interactions between constants are complex and non-linear.")

# Section 2:
# Combined "health scores"
star_score = 1.0 / (G * strong_force)
atom_score = alpha / (strong_force + 0.1)
cosmos_score = G / (lambda_const + 0.1)

life_score = (star_score * atom_score * cosmos_score) ** (1 / 3)

st.header("🔎 Interdependent Effects")

# Calculate health scores (simplified)
star_score = 1.0 / (G * strong_force)
atom_score = alpha / (strong_force + 0.1)
cosmos_score = G / (lambda_const + 0.1)
life_score = (star_score * atom_score * cosmos_score) ** (1 / 3)

# Star system viability
st.subheader("⭐ Star Formation & Stability")
if star_score < 0.1:
    st.error("Too little star formation — gravity or fusion is failing.")
elif star_score > 10:
    st.error("Stars form too rapidly and burn out instantly.")
else:
    st.success("Star formation occurs at a stable, life-supporting rate.")

# Atomic bonding
st.subheader("🧪 Atomic & Chemical Stability")
if atom_score < 0.05:
    st.error("No stable atoms — chemistry collapses.")
elif atom_score > 5.0:
    st.warning("Extreme bonding — weird chemistry may dominate.")
else:
    st.success("Atoms can form stable, diverse chemical structures.")

# Cosmic expansion
st.subheader("🌠 Cosmic Expansion Balance")
if cosmos_score < 0.2:
    st.error("Universe collapses too soon — gravity dominates.")
elif cosmos_score > 10:
    st.error("Universe expands too fast — no structures can form.")
else:
    st.success("Expansion is balanced with gravitational pull.")

# Overall Life-Permitting Score
st.subheader("🌱 Life Potential")
if life_score > 0.5 and life_score < 5.0:
    st.success("This universe might support life!")
else:
    st.warning("Too many physical extremes — unlikely to be life-permitting.")

st.markdown("---")
st.info(
    "These interdependent models are simplified. Real physics is vastly more complex, but this gives a glimpse into how delicate the balance is.")

# Section 3:
st.subheader("🧠 Why This Universe Behaves This Way")

explanation = []

# Gravity and strong force impact star formation
if star_score < 0.1:
    explanation.append("Gravity or the strong force is too weak — stars cannot form or sustain fusion.")
elif star_score > 10:
    explanation.append("Stars form too rapidly and burn out quickly due to overly strong gravity or fusion forces.")
else:
    explanation.append("Star formation appears stable and sustained.")

# Electromagnetic + strong force impact atoms
if atom_score < 0.05:
    explanation.append("The electromagnetic force is too weak to bind electrons to nuclei — chemistry collapses.")
elif atom_score > 5.0:
    explanation.append("Bonding is too intense — exotic chemistry may dominate.")
else:
    explanation.append("Atomic structure is stable, allowing for complex molecules.")

# G and Λ impact cosmic structure
if cosmos_score < 0.2:
    explanation.append("Gravity overwhelms expansion — the universe collapses prematurely.")
elif cosmos_score > 10:
    explanation.append("Expansion dominates — matter never forms galaxies.")
else:
    explanation.append("Cosmic expansion and gravitational attraction are well-balanced.")

# Combine explanations
st.markdown(" ".join(explanation))

# Section 4:
st.subheader("📈 Life Potential Across G and Λ")

G_vals = np.linspace(0.1, 10, 50)
L_vals = np.linspace(0.01, 2.0, 50)
Z = []

for g in G_vals:
    row = []
    for lam in L_vals:
        star = 1.0 / (g * strong_force)
        cosmos = g / (lam + 0.1)
        atom = alpha / (strong_force + 0.1)
        life = (star * atom * cosmos) ** (1 / 3)
        row.append(life)
    Z.append(row)

fig = go.Figure(data=go.Heatmap(
    z=Z,
    x=L_vals,
    y=G_vals,
    colorscale="Viridis",
    colorbar=dict(title="Life Score")
))
fig.update_layout(
    xaxis_title="Cosmological Constant (Λ)",
    yaxis_title="Gravitational Constant (G)",
    title="Life Potential as G and Λ Vary",
    height=500
)
st.plotly_chart(fig, use_container_width=True)

# Universe Simulation Section
st.title("⚛️ Interactive Universe Simulation")

# Display the html document
file_path = "C:/Users/dan/PycharmProjects/PLEASE_WORK_SIM/universe_sim.html"
with open(file_path, "r", encoding="utf-8") as f:
    html_template = f.read()
html_string = html_template.replace("{G}", str(G)) \
                           .replace("{alpha}", str(alpha)) \
                           .replace("{strong_force}", str(strong_force)) \
                           .replace("{lambda_const}", str(lambda_const))
st.components.v1.html(html_string, height=550, scrolling=False)


st.title("☀️ Sun Simulator ")

file_path = "C:/Users/dan/PycharmProjects/PLEASE_WORK_SIM/universe_sim3.html"
with open(file_path, "r", encoding="utf-8") as f:
    html_template = f.read()
html_string = html_template.replace("{G}", str(G)) \
                           .replace("{alpha}", str(alpha)) \
                           .replace("{strong_force}", str(strong_force)) \
                           .replace("{lambda_const}", str(lambda_const))
st.components.v1.html(html_string, height=550, scrolling=False)

# Add explanation for simulation
st.markdown("""
### Simulation Features
- **Particles**: Regular matter that obeys fundamental physics
- **Stars**: Form when matter clumps together under the right conditions
- **Black Holes**: Can form when stars collapse under strong gravity
- **Universe Age**: Shows the progression of the simulated universe
- **Universe State**: Dynamically explains if this universe could support life

### Color Coding by Element
- 💧 **Hydrogen**: Light blue (💠)
- 🎈 **Helium**: Pale blue (🔵)
- 🌿 **Carbon**: Green (🟢)
- ⚙️ **Iron**: Orange (🟠)
- ☀️ **Stars**: Yellow-white to red, depending on their stage
- 🌀 **Black Holes**: Black center with purple glow (accretion disk)
- 🧬 **Bonded Carbon Molecules**: Bright green

### What's Happening
This simulation shows how the fundamental constants affect the formation and behavior of matter in the universe. Try these combinations:
- **Life-Supporting**: G ≈ 1.0, α ≈ 1.0, Strong Force ≈ 1.0, Λ ≈ 1.0
- **Rapid Expansion**: Increase Λ to see particles disperse too quickly
- **Gravitational Collapse**: Increase G to see matter clump aggressively
- **Unstable Matter**: Decrease Strong Force or α to see particles disintegrate
""")

# Footer for entire app
st.markdown("---")
st.info(
    "This interactive simulation loosely demonstrates how finely tuned our universe must be to support life. Even small changes to fundamental constants can create universes where stars can't form, atoms are unstable, or expansion happens too rapidly for complex structures to emerge.")
