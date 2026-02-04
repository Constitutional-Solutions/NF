"""Pattern-first mathematical representations without variable placeholders."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional

from .rust_bridge import load_legion_core_rs


@dataclass(frozen=True)
class PatternTransformation:
    """Describe a transformation pattern by intent and steps."""

    name: str
    steps: List[str]

    def describe(self) -> str:
        """Return a human-readable pattern description."""
        return f"{self.name}: " + " → ".join(self.steps)


@dataclass(frozen=True)
class PatternComposition:
    """Compose multiple transformations into a single pipeline."""

    transformations: List[PatternTransformation]

    def describe(self) -> str:
        """Return the composed transformation narrative."""
        names = " then ".join(t.name for t in self.transformations)
        return f"Compose: {names}"


@dataclass(frozen=True)
class StructuralProperty:
    """Structural property for pattern-based algebraic rules."""

    name: str
    description: str


@dataclass(frozen=True)
class PatternMetadata:
    """Metadata to describe pattern intent, invariants, and constraints."""

    intent: str
    invariants: List[str] = field(default_factory=list)
    constraints: List[str] = field(default_factory=list)


@dataclass
class PatternRegistry:
    """Registry of named patterns with metadata and structural properties."""

    patterns: List[PatternTransformation] = field(default_factory=list)
    properties: List[StructuralProperty] = field(default_factory=list)
    pattern_metadata: Dict[str, PatternMetadata] = field(default_factory=dict)

    def register(
        self,
        pattern: PatternTransformation,
        metadata: Optional[PatternMetadata] = None,
    ) -> None:
        if pattern.name in {existing.name for existing in self.patterns}:
            raise ValueError(f"Pattern '{pattern.name}' already registered.")
        self.patterns.append(pattern)
        if metadata:
            self.pattern_metadata[pattern.name] = metadata

    def register_property(self, prop: StructuralProperty) -> None:
        self.properties.append(prop)

    def summary(self) -> str:
        pattern_names = ", ".join(p.name for p in self.patterns) or "none"
        property_names = ", ".join(p.name for p in self.properties) or "none"
        metadata_count = len(self.pattern_metadata)
        return (
            f"patterns: {pattern_names}; properties: {property_names}; "
            f"metadata: {metadata_count}"
        )

    def metadata_snapshot(self) -> Dict[str, Dict[str, List[str]]]:
        """Return a JSON-serializable view of registered pattern metadata."""
        return {
            name: {
                "intent": meta.intent,
                "invariants": list(meta.invariants),
                "constraints": list(meta.constraints),
            }
            for name, meta in self.pattern_metadata.items()
        }


def pattern_commutativity() -> StructuralProperty:
    return StructuralProperty(
        name="commutativity",
        description="order-independence in transformation application",
    )


def pattern_associativity() -> StructuralProperty:
    return StructuralProperty(
        name="associativity",
        description="grouping-independence in sequential operations",
    )


def pattern_distributivity() -> StructuralProperty:
    return StructuralProperty(
        name="distributivity",
        description="pattern-spread across combined inputs",
    )


def build_quadratic_pattern() -> PatternTransformation:
    """Example transformation for quadratic-growth without variables."""
    return PatternTransformation(
        name="quadratic-growth-pattern",
        steps=[
            "receive",
            "duplicate",
            "multiply-with-self",
            "double-original",
            "combine",
            "add-unity",
        ],
    )


def summarize_properties(properties: Iterable[StructuralProperty]) -> str:
    """Summarize structural properties into a single narrative string."""
    return "; ".join(f"{prop.name}: {prop.description}" for prop in properties)


def compose_patterns(*patterns: PatternTransformation) -> PatternComposition:
    """Compose multiple patterns into a single pipeline."""
    return PatternComposition(transformations=list(patterns))


def quadratic_growth_stream(input_val: float) -> List[float]:
    """Return a variable-less execution trace for quadratic growth."""
    module = load_legion_core_rs()
    if module is not None:
        try:
            return list(module.PatternEngineRS.quadratic_growth_stream(input_val))
        except Exception:
            pass
    dup = input_val
    square = input_val * input_val
    double = input_val * 2.0
    combine = square + double
    unity = combine + 1.0
    return [dup, square, double, combine, unity]
