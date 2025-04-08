import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
# We're using st.components.v1.html instead of streamlit_p5
# from streamlit_p5 import sketch
import random
import plotly.graph_objects as go
import math as Math

# Section 1:

st.set_page_config(page_title="Fine-Tuning the Universe", layout="centered", page_icon="🌌")

st.title("🌌 Fine-Tuning the Universe")
st.subheader("Tweak the **fundamental constants** of physics and see if the universe remains life-permitting.")
st.write("By Brody Bennett - For Physical Science")

# Sidebar for Sliders
st.sidebar.header("🔧 **Fundamental Constants**")
st.sidebar.text("(Loosely Relative Values; 1 = Reality)")

G = st.sidebar.slider("Gravitational Constant (G)", 0.1, 10.0, 1.0, step=0.1)
alpha = st.sidebar.slider("Electromagnetic Force (α)", 0.01, 2.0, 1.0, step=0.01)
strong_force = st.sidebar.slider("Strong Nuclear Force", 0.1, 10.0, 1.0, step=0.1)
lambda_const = st.sidebar.slider("Cosmological Constant (Λ)", 0.0, 2.0, 1.0, step=0.01)

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

# Create HTML with embedded p5.js and improved visualization - Fixed the error with currentState
p5_html = f"""
<div id="universe-sim" style="position: relative; width: 700px; height: 500px;">
  <div id="canvas-container"></div>
  <div id="controls-overlay" style="position: absolute; top: 10px; left: 10px; background: rgba(0,0,0,0.7); padding: 10px; border-radius: 5px; color: white; font-family: monospace;">
  </div>
  <div id="explanation-overlay" style="position: absolute; bottom: 10px; right: 10px; background: rgba(0,0,0,0.7); padding: 10px; border-radius: 5px; color: white; font-family: sans-serif; max-width: 300px; font-size: 12px;">
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/p5.min.js"></script>
<script>
  new p5(function(p) {{
    let particles = [];
    let stars = [];
    let universeAge = 0;
    let universeState = "Forming";
    let starCount = 0;
    let galaxyFormed = false;

    // Constants from sliders
    const G_VALUE = {G};
    const ALPHA_VALUE = {alpha};
    const STRONG_FORCE = {strong_force};
    const LAMBDA_VALUE = {lambda_const};

    class Particle {{
      constructor(x, y) {{
        this.pos = p.createVector(x || p.random(0, p.width), y || p.random(0, p.height));
        this.vel = p.createVector(p.random(-0.5, 0.5), p.random(-0.5, 0.5));
        this.acc = p.createVector(0, 0);
        this.mass = p.random(0.5, 1.5);
        this.size = this.mass * 4;
        this.color = p.color(255, 255, 255);
        this.type = "matter";
        this.lifespan = 1000;
        this.stable = true;
        this.energy = p.random(0, 10);
      }}

      applyForce(force) {{
        // F = ma, so a = F/m
        let f = p5.Vector.div(force, this.mass);
        this.acc.add(f);
      }}

      gravitationalAttraction(other) {{
        // Calculate direction of force
        let force = p5.Vector.sub(other.pos, this.pos);
        let distance = force.mag();

        // Minimum distance to prevent extreme forces
        distance = p.constrain(distance, 10, 1000);

        // Normalize to get direction
        force.normalize();

        // Calculate gravitational force
        let strength = (G_VALUE * this.mass * other.mass) / (distance * distance);
        force.mult(strength);

        return force;
      }}

      expansionForce() {{
        // Direction from center
        let center = p.createVector(p.width/2, p.height/2);
        let force = p5.Vector.sub(this.pos, center);

        if (force.mag() < 1) return p.createVector(0, 0);

        force.normalize();

        // Expansion grows with universe age and is affected by Lambda
        let strength = LAMBDA_VALUE * 0.02 * (1 + universeAge / 1000);
        force.mult(strength);

        return force;
      }}

      update() {{
        // Update position with velocity and acceleration
        this.vel.add(this.acc);
        this.vel.limit(5); // Terminal velocity
        this.pos.add(this.vel);
        this.acc.mult(0); // Reset acceleration

        // Universe age affects particle behavior
        this.lifespan--;

        // Strong and alpha forces affect stability
        if (STRONG_FORCE < 0.3 || ALPHA_VALUE < 0.05) {{
          this.stable = false;
          this.color = p.color(255, 0, 0);  // Unstable - red
          if (p.random(1) < 0.01) this.disintegrate();
        }}
        else if (STRONG_FORCE > 5 || ALPHA_VALUE > 1.5) {{
          this.color = p.color(255, 165, 0);  // Extreme - orange
          if (p.random(1) < 0.005 && stars.length < 15) this.formStar();
        }}
        else {{
          this.color = p.color(0, 255, 255);  // Stable - cyan
          if (p.random(1) < 0.002 && stars.length < 20) this.formStar();
        }}

        // Boundary wrap
        if (this.pos.x < 0) this.pos.x = p.width;
        if (this.pos.x > p.width) this.pos.x = 0;
        if (this.pos.y < 0) this.pos.y = p.height;
        if (this.pos.y > p.height) this.pos.y = 0;
      }}

      formStar() {{
        if (G_VALUE > 0.3 && G_VALUE < 3.0) {{
          stars.push(new Star(this.pos.x, this.pos.y));
          this.lifespan = 0; // Consume the particle
        }}
      }}

      disintegrate() {{
        this.lifespan = 0;
        // Add disintegration effect
        for (let i = 0; i < 5; i++) {{
          particles.push(new DisintegrationParticle(this.pos.x, this.pos.y));
        }}
      }}

      draw() {{
        p.noStroke();
        p.fill(this.color);
        p.ellipse(this.pos.x, this.pos.y, this.size, this.size);
      }}

      isDead() {{
        return this.lifespan <= 0;
      }}
    }}

    class Star {{
      constructor(x, y) {{
        this.pos = p.createVector(x, y);
        this.mass = p.random(3, 8);
        this.size = this.mass * 2;
        this.lifespan = p.random(500, 2000);
        this.color = p.color(255, 255, 100);
        this.pulseRate = p.random(0.02, 0.05);
        this.pulseAmount = 0;
        starCount++;
      }}

      update() {{
        // Star lifecycle based on G and strong force
        this.lifespan -= (G_VALUE * STRONG_FORCE / 1.0);

        // Pulsing effect
        this.pulseAmount = p.sin(universeAge * this.pulseRate) * 2;

        if (this.lifespan <= 100) {{
          // Red giant phase
          this.color = p.color(255, 50, 50);
        }}
      }}

      draw() {{
        // Glow effect
        p.noStroke();
        let glowSize = this.size + this.pulseAmount + 5;
        p.fill(p.red(this.color), p.green(this.color), p.blue(this.color), 50);
        p.ellipse(this.pos.x, this.pos.y, glowSize * 2, glowSize * 2);
        p.fill(p.red(this.color), p.green(this.color), p.blue(this.color), 100);
        p.ellipse(this.pos.x, this.pos.y, glowSize * 1.5, glowSize * 1.5);

        // Star body
        p.fill(this.color);
        p.ellipse(this.pos.x, this.pos.y, this.size + this.pulseAmount, this.size + this.pulseAmount);
      }}

      isDead() {{
        return this.lifespan <= 0;
      }}

      explode() {{
        // Supernova
        for (let i = 0; i < 20; i++) {{
          particles.push(new DisintegrationParticle(this.pos.x, this.pos.y));
        }}

        // Small chance to form black hole
        if (G_VALUE > 2.0 && p.random(1) < 0.3) {{
          let blackHole = new BlackHole(this.pos.x, this.pos.y);
          stars.push(blackHole);
        }}
      }}
    }}

    class BlackHole {{
      constructor(x, y) {{
        this.pos = p.createVector(x, y);
        this.mass = 10;
        this.size = 10;
        this.lifespan = 5000;
        this.color = p.color(0, 0, 0);
        this.accretionDiskColor = p.color(100, 0, 255);
      }}

      update() {{
        // Black holes slowly evaporate
        this.lifespan--;
      }}

      draw() {{
        // Accretion disk
        p.noStroke();
        p.fill(this.accretionDiskColor, 100);
        p.ellipse(this.pos.x, this.pos.y, this.size * 4, this.size * 4);

        // Event horizon
        p.fill(this.color);
        p.ellipse(this.pos.x, this.pos.y, this.size, this.size);
      }}

      isDead() {{
        return this.lifespan <= 0;
      }}
    }}

    class DisintegrationParticle extends Particle {{
      constructor(x, y) {{
        super(x, y);
        this.lifespan = p.random(20, 60);
        this.vel = p5.Vector.random2D().mult(p.random(1, 3));
        this.size = p.random(1, 3);
        this.color = p.color(255, 200, 100);
      }}

      update() {{
        this.pos.add(this.vel);
        this.lifespan--;
        this.color = p.color(255, 200, 100, this.lifespan * 4);
      }}

      draw() {{
        p.noStroke();
        p.fill(this.color);
        p.ellipse(this.pos.x, this.pos.y, this.size, this.size);
      }}
    }}

    function determineUniverseState() {{
      // Determine the state based on constants and current state
      if (universeAge < 100) {{
        return "Big Bang Phase";
      }}

      if (LAMBDA_VALUE > 1.5) {{
        return "Rapid Expansion - Particles Too Dispersed";
      }}

      if (G_VALUE < 0.3) {{
        return "Gravity Too Weak - No Structure Formation";
      }}

      if (G_VALUE > 3.0) {{
        return "Gravity Too Strong - Rapid Collapse";
      }}

      if (STRONG_FORCE < 0.3 || ALPHA_VALUE < 0.05) {{
        return "Unstable Matter - Chemistry Impossible";
      }}

      if (starCount > 10 && galaxyFormed) {{
        return "Stable Universe - Life Permitting";
      }}

      return "Universe Evolving...";
    }}

    function updateExplanation() {{
      const explanationDiv = document.getElementById('explanation-overlay');
      // Fix: store the result of determineUniverseState in a variable
      const currentState = determineUniverseState();

      let explanation = `<strong>Universe State: ${{currentState}}</strong><br><br>`;

      if (G_VALUE < 0.3) {{
        explanation += "Low gravity prevents matter from clumping to form stars.<br>";
      }} else if (G_VALUE > 3.0) {{
        explanation += "Extreme gravity causes rapid collapse of structures.<br>";
      }}

      if (LAMBDA_VALUE > 1.5) {{
        explanation += "High cosmological constant causes universe to expand too quickly.<br>";
      }}

      if (STRONG_FORCE < 0.3) {{
        explanation += "Weak nuclear force prevents stable atomic nuclei.<br>";
      }} else if (STRONG_FORCE > 5.0) {{
        explanation += "Strong nuclear force causes rapid fusion and unstable stars.<br>";
      }}

      if (ALPHA_VALUE < 0.05) {{
        explanation += "Weak electromagnetic force prevents stable atoms.<br>";
      }} else if (ALPHA_VALUE > 1.5) {{
        explanation += "Strong electromagnetic force causes electron orbits to collapse.<br>";
      }}

      explanationDiv.innerHTML = explanation;
    }}

    function updateControls() {{
      const controlsDiv = document.getElementById('controls-overlay');
      // Fix: universeAge is accessible here because it's defined at the top of the p5 function
      let content = `<strong>Universe Age:</strong> ${{Math.floor(universeAge)}}<br>`;
      content += `<strong>Stars:</strong> ${{stars.length}}<br>`;
      content += `<strong>Particles:</strong> ${{particles.length}}<br>`;
      content += `<strong>Constants:</strong><br>`;
      content += `G: ${{G_VALUE.toFixed(1)}} | α: ${{ALPHA_VALUE.toFixed(2)}} | Strong: ${{STRONG_FORCE.toFixed(1)}} | Λ: ${{LAMBDA_VALUE.toFixed(2)}}`;

      controlsDiv.innerHTML = content;
    }}

    p.setup = function() {{
      let canvas = p.createCanvas(700, 500);
      canvas.parent('canvas-container');

      // Initialize particles
      for (let i = 0; i < 80; i++) {{
        particles.push(new Particle());
      }}

      // Create initial central concentration for Big Bang
      for (let i = 0; i < 20; i++) {{
        let angle = p.random(0, p.TWO_PI);
        let radius = p.random(0, 50);
        let x = p.width/2 + p.cos(angle) * radius;
        let y = p.height/2 + p.sin(angle) * radius;
        particles.push(new Particle(x, y));
      }}
    }};

    p.draw = function() {{
      // Space background with subtle nebula effect
      p.background(10, 10, 30);

      // Draw distant stars (background)
      for (let i = 0; i < 100; i++) {{
        p.stroke(255, 255, 255, p.random(100, 255));
        p.point(p.random(p.width), p.random(p.height));
      }}

      // Update universe age
      universeAge += 0.2;

      // Check for galaxy formation
      if (stars.length > 5 && !galaxyFormed && G_VALUE >= 0.3 && G_VALUE <= 3.0) {{
        galaxyFormed = true;
      }}

      // Apply forces between particles
      for (let i = 0; i < particles.length; i++) {{
        // Apply cosmological expansion
        particles[i].applyForce(particles[i].expansionForce());

        // Apply gravity from stars
        for (let j = 0; j < stars.length; j++) {{
          if (stars[j] instanceof BlackHole) {{
            // Black holes have stronger gravity
            let force = particles[i].gravitationalAttraction(stars[j]);
            force.mult(3);
            particles[i].applyForce(force);
          }} else {{
            particles[i].applyForce(particles[i].gravitationalAttraction(stars[j]));
          }}
        }}

        // Apply gravity between particles (simplified - only check every 10th particle)
        if (i % 10 === 0) {{
          for (let j = 0; j < particles.length; j += 10) {{
            if (i !== j) {{
              particles[i].applyForce(particles[i].gravitationalAttraction(particles[j]));
            }}
          }}
        }}
      }}

      // Update and draw stars (behind particles)
      for (let i = stars.length - 1; i >= 0; i--) {{
        stars[i].update();
        stars[i].draw();

        // Handle star death
        if (stars[i].isDead()) {{
          if (!(stars[i] instanceof BlackHole)) {{
            stars[i].explode();
          }}
          stars.splice(i, 1);
        }}
      }}

      // Update and draw particles
      for (let i = particles.length - 1; i >= 0; i--) {{
        particles[i].update();
        particles[i].draw();

        // Remove dead particles
        if (particles[i].isDead()) {{
          particles.splice(i, 1);
        }}
      }}

      // Add new particles occasionally to maintain population
      if (particles.length < 50 && p.frameCount % 30 === 0) {{
        particles.push(new Particle());
      }}

      // Update UI elements
      updateControls();
      updateExplanation();
    }};
  }}, 'universe-sim');
</script>
"""

# Display the improved P5.js sketch using Streamlit components
st.components.v1.html(p5_html, height=550)

# Add explanation for simulation
st.markdown("""
### Simulation Features
- **Particles**: Regular matter that obeys fundamental physics
- **Stars**: Form when matter clumps together under the right conditions
- **Black Holes**: Can form when stars collapse under strong gravity
- **Universe Age**: Shows the progression of the simulated universe
- **Universe State**: Dynamically explains if this universe could support life

### Color Coding
- **Cyan**: Stable atoms and chemistry (life-supporting)
- **Red**: Unstable atoms, chemistry impossible
- **Orange**: Extreme bonding, exotic chemistry
- **Yellow**: Stars (nuclear fusion)
- **Purple glow**: Black hole accretion disk

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