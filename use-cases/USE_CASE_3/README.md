# USE_CASE_3: Citizen Identification

## Description

Citizen identification for natural persons, legal persons, and European persons. This use case covers integration with providers such as electronic certificate and Cl@ve system, as well as the evaluation of username/password (subject to ENS level requirements).

## External Repository

This use case is implemented and maintained in an external repository:

> ## 🔗 [https://github.com/manabcodes/Keycloak-Tests-7](https://github.com/manabcodes/Keycloak-Tests-7)

Please refer to that repository for full source code, configuration, and deployment instructions.

---

## Scope

| Aspect | Detail |
|--------|--------|
| Identity providers | Electronic certificate, Cl@ve system |
| Person types | Natural persons, legal persons, European persons |
| ENS Level | Critical — must comply with National Security Scheme |
| Optional provider | Username/password (requires ENS level evaluation) |

## Objectives

- Integrate multiple identity providers:
  - Electronic certificate
  - Cl@ve system
  - Username/password (to be evaluated according to ENS level)
- Support citizen identification for:
  - Natural persons
  - Legal persons
  - European persons

## Security Considerations

- **ENS Level**: Critical — any implementation must comply with Spain's National Security Scheme (ENS) requirements
- **Current providers**: Electronic certificate and Cl@ve system are the primary trusted providers
- **Username/password**: Only to be considered if ENS level permits; requires thorough risk assessment

## References

- External implementation: [https://github.com/manabcodes/Keycloak-Tests-7](https://github.com/manabcodes/Keycloak-Tests-7)
- Main use cases document: [../../USE_CASES.md](../../USE_CASES.md)
- Project README: [../../README.md](../../README.md)
