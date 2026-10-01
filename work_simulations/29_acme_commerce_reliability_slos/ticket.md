# DATA-1313 — Reliability target and error-budget decision

**Workstream:** Production Engineering  
**Role:** Platform Engineer  
**Decision:** SLO → operating policy

## Mission

Checkout support depends on a service that occasionally fails. Product wants fewer visible failures; engineering wants room to release changes. The disagreement is about the reliability target, not merely the latest incident.

Translate the user-facing expectation into an SLO, calculate the error budget, reconstruct recent consumption, and recommend an operating policy for releases and recovery.

## What makes this situation real

- Reliability is a product promise, not only an infrastructure metric.
- A stricter SLO has engineering and cost consequences.
- Incident history may be incomplete or differently classified.
- The correct response may be to change the target, the system, or the operating policy.

## Investigation discipline

Write at least two competing hypotheses before selecting an explanation.

## Verification

Include at least one regression or guardrail check for the failure mode you identify.

## Definition of done

1. Define the service-level indicator and SLO in user-visible terms.
2. Calculate the corresponding error budget.
3. Attribute recent failures consistently.
4. Show what the budget implies for release velocity.
5. Define an escalation threshold and recovery expectation.
6. Explain the business consequence of both under- and over-targeting reliability.

## Notebook bridge

**Prepare with these notebooks:**
- **50 — Reliability, SLOs & Failure Budgets** → [`09_production_architecture_capstones/50_reliability_slos_failure_budgets.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/09_production_architecture_capstones/50_reliability_slos_failure_budgets.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
