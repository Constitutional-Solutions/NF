use pyo3::prelude::*;
use pyo3::types::PyDict;

/// The Rust-side Quantum Harmonic Engine (Existing)
#[pyclass]
struct QuantumEngineRS {}

#[pymethods]
impl QuantumEngineRS {
    #[new]
    fn new() -> Self {
        QuantumEngineRS {}
    }

    fn energy_eigenvalue(&self, n: i32, omega: f64) -> f64 {
        let hbar = 1.0545718e-34;
        hbar * omega * (n as f64 + 0.5)
    }

    fn phi_quantization(&self) -> (i64, i64) {
        (232996, 144)
    }
}

/// The Rust-side Spiral Physics Engine (NEW)
#[pyclass]
struct SpiralEngineRS {
    a: f64,
    b: f64,
}

#[pymethods]
impl SpiralEngineRS {
    #[new]
    fn new(a: f64, b: f64) -> Self {
        SpiralEngineRS { a, b }
    }

    /// Law 1: Growth (Native Rust Speed)
    fn law_of_growth(&self, theta: f64) -> f64 {
        self.a * (self.b * theta).exp()
    }

    /// Law 2: Resonance (Pearson Correlation in O(N))
    fn law_of_resonance(&self, vec_a: Vec<f64>, vec_b: Vec<f64>) -> f64 {
        if vec_a.len() != vec_b.len() || vec_a.is_empty() {
            return 0.0;
        }

        let n = vec_a.len() as f64;
        let mean_a = vec_a.iter().sum::<f64>() / n;
        let mean_b = vec_b.iter().sum::<f64>() / n;

        let mut numerator = 0.0;
        let mut var_a = 0.0;
        let mut var_b = 0.0;

        for (a, b) in vec_a.iter().zip(vec_b.iter()) {
            let diff_a = a - mean_a;
            let diff_b = b - mean_b;
            numerator += diff_a * diff_b;
            var_a += diff_a * diff_a;
            var_b += diff_b * diff_b;
        }

        let std_a = var_a.sqrt();
        let std_b = var_b.sqrt();

        if std_a == 0.0 || std_b == 0.0 {
            return 0.0;
        }

        let correlation = numerator / (std_a * std_b);
        // Normalize to 0-1 for Coherence
        (correlation + 1.0) / 2.0
    }

    /// Law 3: Emergence (State Machine Logic)
    /// Returns a Dictionary so Python can convert it to dataclass
    fn law_of_emergence<'py>(
        &self,
        py: Python<'py>,
        theta: f64,
        vec_a: Vec<f64>,
        vec_b: Vec<f64>,
    ) -> PyResult<&'py PyDict> {
        let r = self.law_of_growth(theta);
        let c = self.law_of_resonance(vec_a, vec_b);
        let h = 1.0 - c;
        let mode = if c >= 0.6 { "ORDER" } else { "CHAOS" };

        let result = PyDict::new(py);
        result.set_item("theta", theta)?;
        result.set_item("radius", r)?;
        result.set_item("coherence", c)?;
        result.set_item("entropy", h)?;
        result.set_item("mode", mode)?;

        Ok(result)
    }
}

/// Module Registration
#[pymodule]
fn legion_core_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<QuantumEngineRS>()?;
    m.add_class::<SpiralEngineRS>()?;
    Ok(())
}
